######################################### CVD #########################################
#######################################################################################
#    Fabrication process step sub category consisting in the deposition of a solid    #
# material onto a substrate by chemical reaction of a gaseous precursor or mixture of #
#                       precursors, commonly initiated by heat                        #
#######################################################################################

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import (
    Carrier,
    Chuck,
    ICP_Column,
    Massflow_controller,
    SynthesisOutputs,
)
from schema_packages.utils import (
    FabricationChemical,
    TimeRampPressure,
    TimeRampTemperature,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Schemas for cvds steps in fabrication')


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
                    'chamber_temperature',
                    'chamber_pressure',
                    'number_of_loops',
                    'notes',
                ],
            },
        },
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

    material_deposited = SubSection(section_def=FabricationChemical, repeats=True)

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
    )

    item_carrier = SubSection(section_def=Carrier, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class PECVDbase(FabricationProcessStepBase):
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
                    'duration',
                    'chamber_temperature',
                    'chamber_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
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

    material_deposited = SubSection(section_def=FabricationChemical, repeats=True)

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
    )

    chuck = SubSection(section_def=Chuck, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_CVDbase(PECVDbase):
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
                    'duration',
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

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_CVDbase_nested(ICP_CVDbase):
    # self-containing customization of ICP_CVDbase
    m_def = Section(
        description='Atomistic component of an ICP CVD step, nesting version',
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

    substeps = SubSection(
        section_def='ICP_CVDbase_nested',
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class LPCVD(FabricationProcessStep):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of
        a gaseous precursor or mixture of precursors, commonly initiated by heat.
        """,
        a_eln={
            'hide': ['tag', 'duration', 'operator'],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'step_id',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
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

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class PECVD(LPCVD):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of a
        gaseous precursor or mixture of precursors, commonly initiated by heat to create
        a plasma. PECVD uses temperature tipically lower of LPCVD but relyies on an
        electrode system on the sample.
        """,
        a_eln={
            'hide': ['tag', 'duration', 'operator'],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'step_id',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
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

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_CVD(PECVD):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of a
        gaseous precursor or mixture of precursors, commonly initiated by heat to create
        a plasma. To generate the plasma the ICP CVD procedure uses a current in
        addition to the lower electrodes to enanche by magnetic field the generation.
        """,
        a_eln={
            'hide': ['tag', 'duration', 'operator'],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'step_id',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
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

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_CVD_Catania(ICP_CVD):
    m_def = Section(
        # Adaptation of the ICP_CVD class for processes performed at IMM Catania
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of a
        gaseous precursor or mixture of precursors, commonly initiated by heat to create
        a plasma. To generate the plasma the ICP CVD procedure uses a current in
        addition to the lower electrodes to enanche by magnetic field the generation.

        This schema also supports description of single-process multilayer depositions.
        """,
        a_eln={
            'hide': ['tag', 'duration', 'operator'],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'step_id',
                    'process_id',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
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
                    'is_multilayer',
                    'notes',
                ]
            },
        },
    )

    process_id = Quantity(
        type=str,
        description="""
        Unique identifier for CVD processes perfomed in the same location,
        usually of the form YYMMDD_n.
        """,
        a_eln={'component': 'StringEditQuantity'},
    )

    is_multilayer = Quantity(
        type=bool,
        description="""
        Describes wether the deposition is for a multilayer or for a single
        material.
        For a multilayer, it is likely that the synthesis steps are nested and loop.
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )

    synthesis_steps = SubSection(
        section_def=ICP_CVDbase_nested,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_CVD_Catania_testhidden(ICP_CVD):
    m_def = Section(
        # this is to test what happens when properties from parent class are not explicitly declared
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of a
        gaseous precursor or mixture of precursors, commonly initiated by heat to create
        a plasma. To generate the plasma the ICP CVD procedure uses a current in
        addition to the lower electrodes to enanche by magnetic field the generation.

        This schema also supports description of single-process multilayer depositions.
        """,
        a_eln={
            'hide': [  # hide nearly everything
                'tag',
                'duration',
                'operator',
                'job_number',
                'affiliation',
                'location',
                'institution',
                'facility',
                'laboratory',
                'id_item_processed',
                'duration_target',
                'deposition_rate_target',
                'wafer_side',
                'process_id',
                'description',
                'starting_date',
                'ending_date',
                'step_type',
                'definition_of_process_step',
                'keywords',
                'recipe_name',
                'recipe_file',
                'recipe_preview',
                'thickness_target',
                'is_multilayer',
                'notes',
            ],
            'properties': {
                'order': [
                    'step_id',  # step_id and name were in the opposite order originally, so this tests the ordering
                    'name',
                ]
            },
        },
    )

    process_id = Quantity(
        type=str,
        description="""
        Unique identifier for CVD processes perfomed in the same location,
        usually of the form YYMMDD_n.
        """,
        a_eln={'component': 'StringEditQuantity'},
    )

    is_multilayer = Quantity(
        type=bool,
        description="""
        Describes wether the deposition is for a multilayer or for a single
        material.
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )

    synthesis_steps = SubSection(
        section_def=ICP_CVDbase_nested,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


# Current tentative sputtering_catania process class is in CVD.py
# Because:
# -the sputtering class in the main repository of fabrication-utilities does NOT fit
# our needs
# -the CVD classes fit our needs and are used as a template
# -I don't want to deal with how to make NOMAD access this new file right now


class sputtering_catania_base(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a general sputtering step',
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
                    'chamber_temperature',
                    'starting_pressure',
                    'deposition_pressure',
                    'movimentation_frequency',
                    'power',
                    'voltage',
                    'current',
                    'sample_height',
                    'cathode_position',
                    'notes',
                ],
            },
        },
    )

    starting_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber for starting process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )

    deposition_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber during the deposition',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )

    chamber_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    movimentation_frequency = Quantity(
        type=np.float64,
        # description='',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'rpm'},
        unit='rpm',
    )

    power = Quantity(
        type=np.float64,
        # description='',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='W',
    )

    voltage = Quantity(
        type=np.float64,
        # description='',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )

    current = Quantity(
        type=np.float64,
        # description='',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'A'},
        unit='A',
    )

    sample_height = Quantity(
        type=np.float64,
        # description='',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='cm',
    )

    cathode_position = Quantity(
        type=MEnum(
            'confocal',
            'grazing',
        ),
        # description='',
        a_eln={'component': 'EnumEditQuantity'},
    )

    material_deposited = SubSection(section_def=FabricationChemical, repeats=True)

    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class sputtering_catania(FabricationProcessStep):
    m_def = Section(
        description="""
        A synthesis technique where a solid target is bombarded with electrons or
        energetic ions (e.g. Ar+) causing atoms to be ejected ('sputtering').
        The ejected atoms then deposit, as a thin-film, on a substrate.
        http://purl.obolibrary.org/obo/CHMO_0001364

        This schema describes sputtering processes performed at CNR-IMM Catania
        as a unit of NFFA-DI; https://nffa-di.it/en/
        """,
        a_eln={
            'hide': [
                'tag',
                'duration',
                'operator',
                'step_id',
                'affiliation',
                'id_item_processed',
            ],
            'properties': {
                'order': [
                    'name',
                    'process_id',
                    'description',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_preview',
                    'thickness_target',
                    'duration_target',
                    'deposition_rate_target',
                    'notes',
                ]
            },
        },
    )

    process_id = Quantity(
        type=str,
        description="""
        Unique identifier for CVD processes perfomed in the same location,
        usually of the form YYMMDD_n.
        """,
        a_eln={'component': 'StringEditQuantity'},
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
        section_def=sputtering_catania_base,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
