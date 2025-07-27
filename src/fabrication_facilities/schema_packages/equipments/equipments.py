#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import Equipment
from fabrication_facilities.schema_packages.utils import (
    FabricationChemical,
    ReactiveComponents,
)

from fabrication_facilities.schema_packages.equipments.utils import(
    ChuckCapabilities,
    ICP_ColumnCapabilities,
    Massflow_parameter
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Equipments specific definitions ')


class BakingFurnace(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_baking_temperature',
                    'max_baking_temperature',
                    'min_baking_pressure',
                    'max_baking_pressure',
                    'notes',
                ],
            },
        }
    )

    min_baking_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_baking_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_baking_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_baking_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )


class RIE_Etcher(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
        description='Base classes for etching instruments',
    )

    vacuum_system_name = Quantity(
        type=str,
        description='Type of vacuum pump adopted',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_chamber_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chamber_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )

    chuck=SubSection(
        section_def=ChuckCapabilities,
        repeats=False,
    )


class ICP_RIE_Etcher(RIE_Etcher, ArchiveSection):
    m_def = Section(
        description='Dry etching class for instruments where a plasma is involved',
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )

    icp_parameters=SubSection(
        section_def=ICP_ColumnCapabilities,
        repeats=False,
    )

class DRIE_BOSCH_Etcher(ICP_RIE_Etcher, ArchiveSection):
    m_def = Section(
        description='Dry etching instrument for deep geometries',
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )


class LPCVD_System(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'clamping',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    'min_clamping_pressure',
                    'max_clamping_pressure',
                    'notes',
                ],
            },
        },
        description='Instrument used to perform LPCVD steps',
    )

    vacuum_system_name = Quantity(
        type=str,
        description='Type of vacuum pump adopted',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_wall_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_wall_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    clamping = Quantity(
        type=bool,
        description='Is a system for clamping available?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )

    electrostatic_clamping = Quantity(
        type=bool,
        description='Is electrostatic clamping available',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )

    mechanical_clamping = Quantity(
        type=bool,
        description='Is mechanical clamping available',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )

    min_clamping_pressure = Quantity(
        type=np.float64,
        description='Minimum pressure needed on chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )
    max_clamping_pressure = Quantity(
        type=np.float64,
        description='Maximum pressure needed on chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )


class PECVD_System(LPCVD_System, ArchiveSection):
    m_def = Section(
        description='Class instrument for PECVD procedures',
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_chuck_power',
                    'max_chuck_power',
                    'min_chuck_frequency',
                    'max_chuck_frequency',
                    'min_bias',
                    'max_bias',
                    'clamping',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    'min_clamping_pressure',
                    'max_clamping_pressure',
                    'notes',
                ],
            },
        },
    )

    min_chuck_power = Quantity(
        type=np.float64,
        description='Minimal power erogated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    max_chuck_power = Quantity(
        type=np.float64,
        description='Maximal power erogated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    min_chuck_frequency = Quantity(
        type=np.float64,
        description='Minimal frequency of current on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    max_chuck_frequency = Quantity(
        type=np.float64,
        description='Maximal frequency of current on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    min_bias = Quantity(
        type=np.float64,
        description='Minimal bias voltage in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    max_bias = Quantity(
        type=np.float64,
        description='Maximal bias voltage in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )


class ICP_CVD_System(PECVD_System, ArchiveSection):
    m_def = Section(
        description='Class for instruments devoted to ICP_CVD procedures',
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_chuck_power',
                    'max_chuck_power',
                    'min_chuck_frequency',
                    'max_chuck_frequency',
                    'min_icp_power',
                    'max_icp_power',
                    'min_icp_frequency',
                    'max_icp_frequency',
                    'min_bias',
                    'max_bias',
                    'clamping',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    'min_clamping_pressure',
                    'max_clamping_pressure',
                    'notes',
                ],
            },
        },
    )

    min_icp_power = Quantity(
        type=np.float64,
        description='Minimal power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    max_icp_power = Quantity(
        type=np.float64,
        description='Maximal power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    min_icp_frequency = Quantity(
        type=np.float64,
        description='Minimal frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    max_icp_frequency = Quantity(
        type=np.float64,
        description='Maximal frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )


class Wet_Bench_Unit(Equipment):
    m_def = Section(
        description="""
        Bath containing a chemical solution or pure substance to perform wet processes,
        """,
    )

    hood_system = Quantity(
        type=str,
        description='Name of the hood system used for safety',
        a_eln={'component': 'StringEditQuantity'},
    )

    volume_of_solution = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'liter'},
        unit='liter',
    )

    min_bath_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    max_bath_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    max_overflow = Quantity(
        type=np.float64,
        description='Maximum amount of flow at disposal',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'liter'},
        unit='liter',
    )

    filtering_mechanism = Quantity(
        type=bool,
        description='There is a filtering system for the bath?',
        a_eln={'component': 'BoolEditQuantity'},
    )

    recycle_mechanism = Quantity(
        type=bool,
        description='There is a filtering system for the bath?',
        a_eln={'component': 'BoolEditQuantity'},
    )

    solution_renewal = Quantity(
        type=str,
        description='Frequency of the renewal of the solution in the bath',
        a_eln={'component': 'StringEditQuantity'},
    )

    max_number_of_repetitions = Quantity(
        type=int,
        description='Maximum number of successive steps allowed for that well',
        a_eln={'component': 'NumberEditQuantity'},
    )

    reactives = SubSection(section_def=ReactiveComponents, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.volume_of_solution is not None:
            super().normalize(archive, logger)
            for token in self.reactives:
                self.token.final_solution_concentration = (
                    self.token.initial_concentration
                    * self.token.dispensed_volume
                    / self.volume_of_solution
                )


class ElectronBeamLithographer(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_dose',
                    'max_dose',
                    'min_writing_field_dimension',
                    'max_writing_field_dimension',
                    'min_address_size',
                    'max_address_size',
                    'min_clock',
                    'max_clock',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'min_tension',
                    'max_tension',
                    'min_current',
                    'max_current',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_tension = Quantity(
        type=np.float64,
        description='Minimal voltage in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    max_tension = Quantity(
        type=np.float64,
        description='Maximal voltage in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_dose = Quantity(
        type=np.float64,
        description='Minimal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    max_dose = Quantity(
        type=np.float64,
        description='Maximal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    min_writing_field_dimension = Quantity(
        type=np.float64,
        description='Lower area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )

    max_writing_field_dimension = Quantity(
        type=np.float64,
        description='Maximum area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )
    min_address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )

    max_address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )
    min_clock = Quantity(
        type=np.float64,
        description='Minimum frequency at disposal',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    max_clock = Quantity(
        type=np.float64,
        description='Maximum frequency at disposal',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    min_current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )
    max_current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )


class FocusedIonBeamLithographer(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_dose',
                    'max_dose',
                    'min_writing_field_dimension',
                    'max_writing_field_dimension',
                    'min_address_size',
                    'max_address_size',
                    'min_clock',
                    'max_clock',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'min_tension',
                    'max_tension',
                    'min_current',
                    'max_current',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_tension = Quantity(
        type=np.float64,
        description='Minimal voltage in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    max_tension = Quantity(
        type=np.float64,
        description='Maximal voltage in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_dose = Quantity(
        type=np.float64,
        description='Minimal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    max_dose = Quantity(
        type=np.float64,
        description='Maximal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    min_writing_field_dimension = Quantity(
        type=np.float64,
        description='Lower area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )

    max_writing_field_dimension = Quantity(
        type=np.float64,
        description='Maximum area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )
    min_address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )

    max_address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )
    min_clock = Quantity(
        type=np.float64,
        description='Minimum frequency at disposal',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    max_clock = Quantity(
        type=np.float64,
        description='Maximum frequency at disposal',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    min_current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )
    max_current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )


class ResistDeveloper(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )


class Spinner(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )


class Rinser(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
