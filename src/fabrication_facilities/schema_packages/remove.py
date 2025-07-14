#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
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
)
from fabrication_facilities.schema_packages.utils import (
    Massflow_controller,
    parse_chemical_formula,
    FabricationChemical,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Etching workflow schema')

class RIE(FabricationProcessStep, ArchiveSection):
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
                    'short_names',
                    'chemical_species_formulas',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'wall_temperature',
                    'chuck_temperature',
                    'chuck_power',
                    'chuck_frequency',
                    'chamber_pressure',
                    'bias',
                    'clamping',
                    'clamping_type',
                    'depth_measured',
                    'duration_measured',
                    'etching_rate_obtained',
                    'notes',
                ]
            },
        },
    )
    short_names = Quantity(
        type=str,
        description='Materials to be etched',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity', 'label': 'target material'},
    )
    duration_target = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    chemical_species_formulas = Quantity(
        type=str,
        description='Inserted only if known',
        shape= ['*'],
        a_eln={'component': 'StringEditQuantity'},
    )
    depth_target = Quantity(
        type=np.float64,
        description='Amount of material to be etched',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    wall_temperature=Quantity(
        type=np.float64,
        description='Temperature of the wall of the chamber',
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    chuck_temperature=Quantity(
        type=np.float64,
        description='Temperature imposed on the chuck',
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    chuck_power=Quantity(
        type=np.float64,
        description='Power imposed on the chuck',
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='W',
    )
    chuck_frequency=Quantity(
        type=np.float64,
        description='Frequency impulse imposed on the chuck',
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )
    bias=Quantity(
        type=np.float64,
        description='Voltage imposed on the sample by electodes',
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )
    clamping= Quantity(
        type=bool,
        description='Is clamping used in the process?',
        a_eln={'component':'BoolEditQuantity'},
    )
    clamping_type = Quantity(
        type=MEnum(
            [
                'None',
                'Mechanical',
                'Electrostatic',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    depth_measured = Quantity(
        type=np.float64,
        description='Amount of material ethced effectively in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_measured = Quantity(
        type=np.float64,
        description='Real time of the process ad output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    etching_rate_obtained = Quantity(
        type=np.float64,
        description='Etching rate as output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )
    etching_rate_target = Quantity(
        type=np.float64,
        description='etching rate desired',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm/minute',
        },
        unit='nm/minute',
    )
    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
    )

    materials_etched=SubSection(
        section_def= FabricationChemical,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        chems = []
        for formula in self.chemical_species_formulas:
            chemical = FabricationChemical()
            chemical.chemical_formula=formula
            chemical.normalize(archive, logger)
            chems.append(chemical)
        self.materials_etched = chems


class ICP_RIE(RIE, ArchiveSection):
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
                    'short_names',
                    'chemical_species_formulas',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'wall_temperature'
                    'chamber_pressure',
                    'chuck_temperature',
                    'chuck_power',
                    'chuck_frequency',
                    'icp_power',
                    'icp_frequency',
                    'bias',
                    'cooling_helium_massflow',
                    'cooling_helium_temperature',
                    'clamping',
                    'clamping_type',
                    'depth_measured',
                    'duration_measured',
                    'etching_rate_obtained',
                    'notes',
                ]
            },
        },
    )
    # chamber_pressure = Quantity(
    #     type=np.float64,
    #     description='Pressure in the chamber',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'mbar',
    #     },
    #     unit='mbar',
    # )
    # chuck_temperature = Quantity(
    #     type=np.float64,
    #     description='Temperature of the chuck',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'celsius',
    #     },
    #     unit='celsius',
    # )
    # chuck_power = Quantity(
    #     type=np.float64,
    #     description='Power erogated on the chuck',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'watt',
    #     },
    #     unit='watt',
    # )
    # chuck_frequency = Quantity(
    #     type=np.float64,
    #     description='Frequency of current on the chuck',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'MHz',
    #     },
    #     unit='MHz',
    # )
    icp_power = Quantity(
        type=np.float64,
        description='Power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )
    icp_frequency = Quantity(
        type=np.float64,
        description='Frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    cooling_helium_massflow = Quantity(
        type=np.float64,
        description='Rate at which the helium for cooling the chuck flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    cooling_helium_temperature = Quantity(
        type=np.float64,
        description='Temperature of the cooling helium on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    # bias = Quantity(
    #     type=np.float64,
    #     description='Bias voltage in the chamber',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'volt',
    #     },
    #     unit='volt',
    # )
    # depth_measured = Quantity(
    #     type=np.float64,
    #     description='Amount of material ethced effectively in the process',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'nm',
    #     },
    #     unit='nm',
    # )
    # duration_measured = Quantity(
    #     type=np.float64,
    #     description='Real time of the process ad output',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'minute',
    #     },
    #     unit='minute',
    # )
    # etching_rate_obtained = Quantity(
    #     type=np.float64,
    #     description='Etching rate as output',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'nm/minute',
    #     },
    #     unit='nm/minute',
    # )
    # fluximeters = SubSection(
    #     section_def=Massflow_controller,
    #     repeats=True,
    # )
    # material_elemental_composition = SubSection(
    #     section_def=ElementalComposition, repeats=True
    # )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        # if self.chemical_formula:
        #     elements, counts = parse_chemical_formula(self.chemical_formula)
        #     total = 0
        #     for token in counts:
        #         total += int(token)
        #     mass = sum(am[an[el]] * cou for el, cou in zip(elements, counts))
        #     if total != 0:
        #         elemental_fraction = np.array(counts) / total
        #         elementality = []
        #         i = 0
        #         for entry in elements:
        #             elemental_try = ElementalComposition()
        #             elemental_try.element = entry
        #             elemental_try.atomic_fraction = elemental_fraction[i]
        #             mass_frac = (am[an[entry]] * counts[i]) / mass
        #             elemental_try.mass_fraction = mass_frac
        #             i += 1
        #             elementality.append(elemental_try)
        #     else:
        #         print('No elements provided')
        #     self.material_elemental_composition = elementality


class WetEtching(Chemical, FabricationProcessStep, ArchiveSection):
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
                    'etching_solution',
                    'etching_solution_proportions',
                    'depth_target',
                    'duration_target',
                    'depth_measured',
                    'duration_measured',
                    'etching_rate_obtained',
                    'etching_type',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        description='Material to be etched',
        a_eln={'component': 'StringEditQuantity', 'label': 'target material'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={'component': 'StringEditQuantity'},
    )
    depth_target = Quantity(
        type=np.float64,
        description='Amount of material to be etched',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    etching_solution = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    etching_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    duration_target = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    depth_measured = Quantity(
        type=np.float64,
        description='Amount of material ethced effectively in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_measured = Quantity(
        type=np.float64,
        description='Real time of the process ad output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    etching_rate_obtained = Quantity(
        type=np.float64,
        description='Etching rate as output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )
    etching_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
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


class WetCleaning(FabricationProcessStep, ArchiveSection):
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
                    'removing_solution',
                    'removing_solution_proportions',
                    'removing_duration',
                    'removing_temperature',
                    'rising_solution',
                    'rising_solution_proportions',
                    'rising_duration',
                    'notes',
                ]
            },
        },
    )
    removing_solution = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    removing_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    removing_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    removing_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    rising_solution = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    rising_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    rising_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )


class Stripping(Chemical, FabricationProcessStep, ArchiveSection):
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
                    'stripping_type',
                    'short_name',
                    'chemical_formula',
                    'duration_target',
                    'removing_temperature',
                    'ultrasound_required',
                    'notes',
                ]
            },
        },
    )
    stripping_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    short_name = Quantity(
        type=str,
        description='Material to remove',
        a_eln={'component': 'StringEditQuantity', 'label': 'Target material'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={'component': 'StringEditQuantity'},
    )
    removing_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    duration_target = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    ultrasound_required = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
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


m_package.__init_metainfo__()
