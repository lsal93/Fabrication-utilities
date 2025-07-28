from typing import (
    TYPE_CHECKING,
)

import numpy as np
from ase.data import atomic_masses as am
from ase.data import atomic_numbers as an
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.datamodel.metainfo.eln import Chemical
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from fabrication_facilities.schema_packages.steps.utils import (
    Carrier,
    Chuck,
    ICP_Column,
    Massflow_controller,
)
from fabrication_facilities.schema_packages.utils import (
    TimeRampPressure,
    TimeRampTemperature,
    TimeRampRotation,
    parse_chemical_formula,
    generate_elementality,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Add processes schema')


class SynthesisOutputs(ArchiveSection):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'duration_measured',
                ],
            }
        },
        description='Class describing all possible output data in synthesis steps',
    )

    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )

    duration_measured = Quantity(
        type=np.float64,
        description='Real time employed',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    control_parameter_profile = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class LPCVDbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a general LPCVD step',
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'short_name',
                    'target_material_formula',
                    'chamber_temperature',
                    'chamber_pressure',
                    'number_of_loops',
                    'notes',
                ],
            },
        },
    )

    short_name = Quantity(
        type=str,
        description='Material to be deposited',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'target material',
        },
    )

    target_material_formula = Quantity(
        type=str,
        description='Formula of the material target. Insert only if known',
        a_eln={'component': 'StringEditQuantity'},
    )

    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )

    chamber_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    number_of_loops = Quantity(
        type=int,
        description='Times for which this step is repeated with equal parameters',
        a_eln={'component': 'NumberEditQuantity'},
    )

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    material_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
    )

    item_carrier = SubSection(section_def=Carrier, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.target_material_formula:
            elements, counts = parse_chemical_formula(self.target_material_formula)
            total = 0
            for token in counts:
                total += int(token)
            mass = sum(am[an[el]] * cou for el, cou in zip(elements, counts))
            if total != 0:
                elemental_fraction = np.array(counts) / total
                elementality = []
                i = 0
                for entry in elements:
                    elemental_try = ElementalComposition()
                    elemental_try.element = entry
                    elemental_try.atomic_fraction = elemental_fraction[i]
                    mass_frac = (am[an[entry]] * counts[i]) / mass
                    elemental_try.mass_fraction = mass_frac
                    i += 1
                    elementality.append(elemental_try)
            else:
                print('No elements provided')
            self.material_elemental_composition = elementality


class PECVDbase(LPCVDbase):
    m_def = Section(
        description='Atomistic component of a PECVD step',
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'short_name',
                    'target_material_formula',
                    'chamber_temperature',
                    'chamber_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )

    LPCVDbase.chamber_temperature.description = 'Temperature of the wall of the chamber'

    chuck = SubSection(section_def=Chuck, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.target_material_formula:
            super().normalize(archive, logger)


class ICP_CVDbase(PECVDbase, ArchiveSection):
    m_def = Section(
        description='Atomistic component of an ICP CVD step',
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'short_name',
                    'target_material_formula',
                    'chamber_temperature',
                    'chamber_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )

    icp_column = SubSection(
        section_def=ICP_Column,
        repeats=False,
    )


class LPCVD(FabricationProcessStep):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of
        a gaseous precursor or mixture of precursors, commonly initiated by heat.
        """,
        a_eln={
            'hide': [
                'tag',
                'duration',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'thickness_target',
                    'duration_target',
                    'deposition_rate_target',
                    'notes',
                ]
            },
        },
    )

    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )

    duration_target = Quantity(
        type=np.float64,
        description='Duration required of the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    deposition_rate_target = Quantity(
        type=np.float64,
        description='Deposition rate desired',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm/minute',
        },
        unit='nm/minute',
    )

    synthesis_steps = SubSection(
        section_def=LPCVDbase,
        repeats=True,
    )

    outputs = SubSection(
        section_def=SynthesisOutputs,
        repeats=False,
    )


class PECVD(LPCVD):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of a
        gaseous precursor or mixture of precursors, commonly initiated by heat to create
        a plasma. PECVD uses temperature tipically lower of LPCVD but relyies on an
        electrode system on the sample.
        """,
        a_eln={
            'hide': [
                'tag',
                'duration',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'wafer_side',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'thickness_target',
                    'duration_target',
                    'deposition_rate_target',
                    'notes',
                ]
            },
        },
    )

    wafer_side = Quantity(
        type=MEnum(
            'front',
            'back',
        ),
        description='Side exposed in the process',
        a_eln={'component': 'EnumEditQuantity'},
    )

    synthesis_steps = SubSection(
        section_def=PECVDbase,
        repeats=True,
    )


class ICP_CVD(PECVD):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of a
        gaseous precursor or mixture of precursors, commonly initiated by heat to create
        a plasma. To generate the plasma the ICP CVD procedure uses a current in
        addition to the lower electrodes to enanche by magnetic field the generation.
        """,
        a_eln={
            'hide': [
                'tag',
                'duration',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'thickness_target',
                    'duration_target',
                    'deposition_rate_target',
                    'notes',
                ]
            },
        },
    )

    synthesis_steps = SubSection(
        section_def=ICP_CVDbase,
        repeats=True,
    )


class Coating(FabricationProcessStep):
    m_def = Section(
        a_eln={
            'hide': [
                'tag',
                'duration',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'wafer_side',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'notes',
                ]
            },
        }
    )

    wafer_side = Quantity(
        type=MEnum(
            'front',
            'back',
        ),
        description='Side exposed in the process',
        a_eln={'component': 'EnumEditQuantity'},
    )


class Spin_Coating(FabricationProcessStep):
    m_def = Section(
        a_eln={
            'hide': [
                'duration',
                'tag',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'short_name',
                    'chemical_formula',
                    'thickness_target',
                    'hdms_required',
                    'hdms_temperature',
                    'priming_duration',
                    # 'exposure_required',
                    # 'exposure_intensity',
                    # 'exposure_duration',
                    # 'peb_required',
                    # 'peb_duration',
                    # 'peb_temperature',
                    # 'dewetting_duration',
                    # 'dewetting_temperature',
                    'dispensing_mode',
                    'dispensing_locus',
                    'spin_dispensed_volume',
                    'spin_frequency',
                    'spin_angular_acceleration',
                    'spin_duration',
                    # 'baking_required',
                    # 'baking_duration',
                    # 'baking_temperature',
                    # 'thickness_measured',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        description='Type of resist to be deposited',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'resist name',
        },
    )
    chemical_formula = Quantity(
        type=str,
        description='Resist formula. Insert only if known',
        a_eln={'component': 'StringEditQuantity'},
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of resist to be deposited',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )
    hdms_required = Quantity(
        type=bool,
        description='The recipe use the hdms?',
        a_eln={'component': 'BoolEditQuantity'},
    )
    hdms_temperature = Quantity(
        type=np.float64,
        description='Temperature of the primer',
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit':'celsius'},
        unit='celsius'
    )
    priming_duration=Quantity(
        type=np.float64,
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit':'sec'},
        unit='sec'
    )
    dispensing_mode=Quantity(
        type=MEnum(
            'auto',
            'manual',
        ),
        a_eln={'component':'EnumEditQuantity'},
    )
    dispensing_locus=Quantity(
        type=str,
        a_eln={'component':'StringEditQuantity'},
    )
    # exposure_required = Quantity(
    #     type=bool,
    #     description='The recipe use exposure?',
    #     a_eln={'component': 'BoolEditQuantity'},
    # )
    # exposure_intensity = Quantity(
    #     type=np.float64,
    #     description='Power per area in the exposure',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'mwatt/cm^2',
    #     },
    #     unit='mwatt/cm^2',
    # )
    # exposure_duration = Quantity(
    #     type=np.float64,
    #     description='The duration of the exposure',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'sec',
    #     },
    #     unit='sec',
    # )
    # peb_required = Quantity(
    #     type=bool,
    #     description='The recipe needs PEB?',
    #     a_eln={'component': 'BoolEditQuantity'},
    # )
    # peb_duration = Quantity(
    #     type=np.float64,
    #     description='The duration of the peb',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'sec',
    #     },
    #     unit='sec',
    # )
    # peb_temperature = Quantity(
    #     type=np.float64,
    #     description='The temperature of the peb',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'celsius',
    #     },
    #     unit='celsius',
    # )
    # dewetting_duration = Quantity(
    #     type=np.float64,
    #     description='The duration of the dewetting',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'minute',
    #     },
    #     unit='minute',
    # )
    # dewetting_temperature = Quantity(
    #     type=np.float64,
    #     description='The temperaure of the dewetting',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'celsius',
    #     },
    #     unit='celsius',
    # )
    spin_dispensed_volume = Quantity(
        type=np.float64,
        description='Solution dispensed',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'milliliter',
        },
        unit='milliliter',
    )
    spin_frequency = Quantity(
        type=np.float64,
        description='Velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )
    spin_angular_acceleration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute/sec',
        },
        unit='revolutions_per_minute/sec',
    )
    spin_duration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    # baking_required = Quantity(
    #     type=bool,
    #     description='The recipe use baking?',
    #     a_eln={
    #         'component': 'BoolEditQuantity',
    #     },
    # )
    # baking_duration = Quantity(
    #     type=np.float64,
    #     description='The duration of the baking',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'minute',
    #     },
    #     unit='minute',
    # )
    # baking_temperature = Quantity(
    #     type=np.float64,
    #     description='The temperaure of the baking',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'celsius',
    #     },
    #     unit='celsius',
    # )
    # thickness_measured = Quantity(
    #     type=np.float64,
    #     description='Actual amount of resist deposited',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'nm',
    #     },
    #     unit='nm',
    # )

    resist_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

    rotation_ramp=SubSection(
        section_def=TimeRampRotation,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_formula is not None:
            generate_elementality(
                self.chemical_formula,
                self.resist_elemental_composition
            )
            # elements, counts = parse_chemical_formula(self.chemical_formula)
            # total = 0
            # for token in counts:
            #     total += int(token)
            # mass = sum(am[an[el]] * cou for el, cou in zip(elements, counts))
            # if total != 0:
            #     elemental_fraction = np.array(counts) / total
            #     elementality = []
            #     i = 0
            #     for entry in elements:
            #         elemental_try = ElementalComposition()
            #         elemental_try.element = entry
            #         elemental_try.atomic_fraction = elemental_fraction[i]
            #         mass_frac = (am[an[entry]] * counts[i]) / mass
            #         elemental_try.mass_fraction = mass_frac
            #         i += 1
            #         elementality.append(elemental_try)
            # else:
            #     print('No elements provided')
            # self.resist_elemental_composition = elementality

### Generare funzione che prende la variabile formula chimica e poi appende le classi


class Bonding(FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'wafer_bonding_type',
                    'alignment_required',
                    'alignment_max_error',
                    'wafer_stack_1_name',
                    'wafer_stack_2_name',
                    'wafer_space_required',
                    'alignment_target_mask_name',
                    'alignment_viewfinder_mask_name',
                    'wafer_bonded_name',
                    'notes',
                ]
            },
        },
    )
    wafer_bonding_type = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    alignment_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    alignment_max_error = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    wafer_stack_1_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_stack_2_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_space_required = Quantity(
        type=bool,
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    alignment_target_mask_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    alignment_viewfinder_mask_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_bonded_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )


class ElectronGun(FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'short_name',
                    'wafer_stack_name',
                    'thickness_target',
                    'duration_target',
                    'chamber_pressure',
                    'spin_frequency',
                    'thickness_measured',
                    'gun_voltage_measured',
                    'gun_current_measured',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        description='Deposited Material',
        a_eln={'component': 'StringEditQuantity', 'label': 'Target material'},
    )
    wafer_stack_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    spin_frequency = Quantity(
        type=np.float64,
        description='Velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )
    thickness_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    chamber_pressure = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    thickness_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    gun_voltage_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )
    gun_current_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mampere'},
        unit='mampere',
    )


class Sputtering(Chemical, FabricationProcessStep, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'short_name',
                    'chemical_formula',
                    'index',
                    'sample_movement',
                    'spin_frequency',
                    'thickness_target',
                    'duration_target',
                    'chuck_temperature',
                    'power',
                    'delay_between_stack_layers',
                    'thickness_measured',
                    'duration_measured',
                    'deposition_rate_obtained',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        description='Material to be deposited',
        a_eln={'component': 'StringEditQuantity', 'label': 'target material'},
    )
    sample_movement = Quantity(
        type=str,
        description='Movimentation the sample is exposed to',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    spin_frequency = Quantity(
        type=np.float64,
        description='Velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
            'label': 'Movimentation frequency',
        },
        unit='revolutions_per_minute',
    )
    index = Quantity(
        type=int,
        description='Deposition step index',
        a_eln={
            'component': 'NumberEditQuantity',
        },
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    power = Quantity(
        type=np.float64,
        description='Power erogated',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'watt'},
        unit='watt',
    )
    delay_between_stack_layers = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    thickness_measured = Quantity(
        type=np.float64,
        description='Amount of material deposited effectively in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_measured = Quantity(
        type=np.float64,
        description='Real time employed',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    deposition_rate_obtained = Quantity(
        type=np.float64,
        description='Deposition rate as output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )

    material_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_formula:
            elements, counts = parse_chemical_formula(self.chemical_formula)
            total = 0
            for token in counts:
                total += int(token)
            if total != 0:
                elemental_fraction = np.array(counts) / total
                elementality = []
                i = 0
                for entry in elements:
                    elemental_try = ElementalComposition()
                    elemental_try.element = entry
                    elemental_try.atomic_fraction = elemental_fraction[i]
                    i += 1
                    elementality.append(elemental_try)
            else:
                print('No elements provided')
            self.material_elemental_composition = elementality


class SOG(Chemical, FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'short_name',
                    'chemical_formula',
                    'pre_cleaning',
                    'thickness_target',
                    'dewetting_duration',
                    'dewetting_temperature',
                    'thickness_measured',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label': 'Substrate Material'},
    )
    pre_cleaning = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    dewetting_duration = Quantity(
        type=np.float64,
        description='The duration of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    dewetting_temperature = Quantity(
        type=np.float64,
        description='The temperaure of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    thickness_measured = Quantity(
        type=np.float64,
        description='Amount of material deposited as described in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )

    substrate_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_formula:
            elements, counts = parse_chemical_formula(self.chemical_formula)
            total = 0
            for token in counts:
                total += int(token)
            if total != 0:
                elemental_fraction = np.array(counts) / total
                elementality = []
                i = 0
                for entry in elements:
                    elemental_try = ElementalComposition()
                    elemental_try.element = entry
                    elemental_try.atomic_fraction = elemental_fraction[i]
                    i += 1
                    elementality.append(elemental_try)
            else:
                print('No elements provided')
            self.substrate_elemental_composition = elementality


m_package.__init_metainfo__()
