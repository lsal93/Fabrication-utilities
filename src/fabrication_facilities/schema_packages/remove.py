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
    FabricationProcessStepBase,
)
from fabrication_facilities.schema_packages.utils import (
    Massflow_controller,
    parse_chemical_formula,
    FabricationChemical,
    TimeRampTemperature,
    TimeRampMassflow,
    TimeRampPressure,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Etching workflow schema')


class EtchingOutputs(ArchiveSection):

    m_def=Section(
        a_eln={
            'properties':{
                'order':[
                    'depth_obtained',
                    'duration_measured',
                    'etching_rate_obtained',
                ],
            }
        },
        description= 'Set of parameters obtained in an etching process',
    )
    depth_obtained = Quantity(
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
        a_eln={'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.depth_obtained:
            a=self.depth_obtained
            if self.duration_measured:
                b=self.duration_measured
                self.etching_rate_obtained = a/b
            else:
                pass

class RIEbase(FabricationProcessStepBase, ArchiveSection):
    m_def = Section(
        description = 'Atomistic component of a RIE step',
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'step_type',
                'definition_of_process_step',
                'keywords',
                'recipe_name',
                'recipe_file',
                'recipe_preview',
                'name',
                'description',
                'affiliation',
                'room',
                'location',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'operator',
                    'short_names'
                    'target_materials_formulas',
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
                    'clamping_pressure',
                    'number of loops'
                    'notes',
                ]
            },
        },
    )
    duration_target = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    short_names = Quantity(
        type=str,
        description='Name of reactive species',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity', 'label': 'target_materials_names'},
    )
    target_materials_formulas = Quantity(
        type=str,
        description='Inserted only if known',
        shape=['*'],
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
    wall_temperature = Quantity(
        type=np.float64,
        description='Temperature of the wall of the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    chuck_power = Quantity(
        type=np.float64,
        description='Power imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='W',
    )
    chuck_frequency = Quantity(
        type=np.float64,
        description='Frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )
    bias = Quantity(
        type=np.float64,
        description='Voltage imposed on the sample by electodes',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )
    clamping = Quantity(
        type=bool,
        description='Is clamping used in the process?',
        a_eln={'component': 'BoolEditQuantity'},
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

    clamping_pressure = Quantity(
        type=np.float64,
        description='Pressure generated by a cooling helium flow on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    number_of_loops=Quantity(
        type=int,
        description='Times for which this step is repeated with equal parameters',
        a_eln={'component':'NumberEditQuantity'},
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

    temperature_ramps=SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    pressure_ramps=SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    gaseous_massflow_ramps=SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )

    materials_etched = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.target_materials_formulas is None:
            pass
        else:
            chems = []
            for formula in self.target_materials_formulas:
                chemical = FabricationChemical()
                chemical.chemical_formula = formula
                chemical.normalize(archive, logger)
                chems.append(chemical)
            self.materials_etched = chems


class RIE (FabricationProcessStep, ArchiveSection):

    m_def=Section(
        description="""
        Form of plasma etching  in which the wafer is placed on a radio-frequency-driven
        electrode and the counter electrode has a larger area than the driven electrode.
        Uses both physical and chemical mechanisms to achieve high levels of resolutions.
        In the RIE process, cations are produced from reactive gases which are
        accelerated with high energy to the substrate and chemically react with the item
        surface. Factors such as applied coil or electrode power, reactant gas flow
        rates, duty cycles and chamber presures were considered as main process
        parameters. The plasma beam is generated under low pressure by an electromagnetic
         field. High energy ions, predominantly bombarding the surface, normally create
        a local abundance of radicals that react with the surface.
        """,
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
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
                ]
            }
        }
    )

    etching_steps=SubSection(
        section_def=RIEbase,
        repeats=True,
    )

    temperature_ramps=SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    pressure_ramps=SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    gaseous_massflow_ramps=SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )

    outputs=SubSection(
        section_def=EtchingOutputs,
        repeats=True,
    )


class ICP_RIEbase(RIEbase, ArchiveSection):
    m_def = Section(
        description = 'Atomistic component of an ICP RIE step',
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'step_type',
                'definition_of_process_step',
                'keywords',
                'recipe_name',
                'recipe_file',
                'recipe_preview',
                'name',
                'description',
                'affiliation',
                'room',
                'location',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'short_names',
                    'target_materials_formulas',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'wall_temperature',
                    'chamber_pressure',
                    'chuck_temperature',
                    'chuck_power',
                    'chuck_frequency',
                    'icp_power',
                    'icp_frequency',
                    'bias',
                    'clamping',
                    'clamping_type',
                    'clamping_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )

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


class ICP_RIE(FabricationProcessStep, ArchiveSection):

    m_def=Section(
        description="""
        Dry etching method by which energy is magnetically coupled into the
        plasma by a current carrying loop around the chamber,
        using etching based on ions reacting with substrate surface and hitting it
        """,
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
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
                ]
            }
        }
    )

    etching_steps=SubSection(
        section_def=ICP_RIEbase,
        repeats=True,
    )

    temperature_ramps=SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    pressure_ramps=SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    gaseous_massflow_ramps=SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )

    outputs=SubSection(
        section_def=EtchingOutputs,
        repeats=True,
    )


class DRIEbase(ICP_RIEbase, ArchiveSection):
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
                'step_type',
                'definition_of_process_step',
                'keywords',
                'recipe_name',
                'recipe_file',
                'recipe_preview',
                'name',
                'description',
                'affiliation',
                'room',
                'location',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'short_names',
                    'target_materials_formulas',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'wall_temperature',
                    'chamber_pressure',
                    'chuck_temperature',
                    'chuck_power',
                    'chuck_frequency',
                    'icp_power',
                    'icp_frequency',
                    'bias',
                    'clamping',
                    'clamping_type',
                    'clamping_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )



class DRIE(FabricationProcessStep, ArchiveSection):
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
                ]
            }
        }
    )

    etching_steps = SubSection(
        section_def=DRIEbase,
        repeats=True,
    )

    temperature_ramps=SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    pressure_ramps=SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    gaseous_massflow_ramps=SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )

    outputs=SubSection(
        section_def=EtchingOutputs,
        repeats=True,
    )


class WetEtching(FabricationProcessStep, ArchiveSection):
    m_def = Section(
        description="""
        Wet etching is a material removal process that uses liquid chemicals or etchants
        to remove materials from a wafer. The specific patters are defined by masks on
        the wafer. Materials that are not protected by the masks are etched away by
        liquid chemicals. A wet etching process involves multiple chemical reactions that
        consume the original reactants and produce new reactants. The wet etch process
        can be described by three basic steps. (1) Diffusion of the liquid etchant to the
        structure that is to be removed. (2) The reaction between the liquid etchant and
        the material being etched away. A reduction-oxidation (redox) reaction usually
        occurs. This reaction entails the oxidation of the material then dissolving the
        oxidized material. (3) Diffusion of the byproducts in the reaction from the
        reacted surface.
        """,
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
                    'target_materials_formulas',
                    'etching_solution',
                    'etching_solution_proportions',
                    'etching_reactives',
                    'etching_reactives_formulas',
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
    short_names = Quantity(
        type=str,
        description='Materials to be etched',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity', 'label': 'target materials'},
    )
    target_materials_formulas = Quantity(
        type=str,
        description='Formulas of materials etched',
        shape=['*'],
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
    etching_reactives = Quantity(
        type=str,
        description='Names of compounds used to etch',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity'},
    )
    etching_reactives_formulas = Quantity(
        type=str,
        description='Formulas of compounds used to etch',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity'},
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

    materials_etched = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    reactives_used_to_etch = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_species_formulas is None:
            pass
        else:
            chems = []
            for num, formula in enumerate(self.chemical_species_formulas):
                chemical = FabricationChemical()
                try:
                    chemical.short_name = self.short_names[num]
                except Exception as e:
                    print(f' Error {e}. No name at position {num} in short_names')
                    raise
                # Si può provare a scrivere una funzione che parsa le entries multiple?
                # Tipo def mult_entries (class_to_append, list to read, element to append):
                # Blocco simile a quanto sopra. Dovrei dargli anche il bersaglio della classe a cui
                # puntare la quantità atomizzata.
                chemical.chemical_formula = formula
                chemical.normalize(archive, logger)
                chems.append(chemical)
            self.materials_etched = chems

        if self.etching_reactives_formulas is None:
            pass
        else:
            reactives = []
            for formula in self.etching_reactives_formulas:
                reactive = FabricationChemical()
                reactive.chemical_formula = formula
                reactive.normalize(archive, logger)
                reactives.append(reactive)
            self.reactives_used_to_etch = reactives


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


# FIB-SEM
# SEM
# EBL
# ICP-RIE
# CVD
# AFM
