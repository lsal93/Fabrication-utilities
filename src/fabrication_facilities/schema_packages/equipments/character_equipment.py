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
# py module dedicated to characterization tools based on
# equipments.py
from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import Equipment
from fabrication_facilities.schema_packages.steps.character import (
    CharacterizationTechnique,
)

if TYPE_CHECKING:
    pass

m_package = Package(name='Characterization equipment specific definitions ')


#######################################################################################
################################ AFM ##################################################
#######################################################################################
class CharctEquipmentBase(Equipment):
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
                    'notes',
                ],
            },
        }
    )
    lab_id = Quantity(
        type=str,
        description='ID assigned by lab for findability',
        a_eln={'component': 'StringEditQuantity', 'label': 'id'},
    )
    inventary_code = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    affiliation = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    institution = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    manufacturer_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    product_model = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    automatic_loading = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    is_bookable = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    contamination_class = Quantity(
        type=int,
        description='Level of quality of the environment in the equipment',
        a_eln={'component': 'NumberEditQuantity'},
    )

    notes = Quantity(
        type=str,
        a_eln={
            'component': 'RichTextEditQuantity',
        },
    )
    equipmentTechniques = SubSection(
        section_def=CharacterizationTechnique,
        repeats=True,
    )


class AFM_System(CharctEquipmentBase, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'afm_tip',
                    'afm_mode',
                    'afm_setpoint',
                    'afm_fb_gain',
                    'afm_tip_resonance',
                    'afm_tip_phase',
                    'afm_laser_intensity',
                    'afm_fb_gain_o',
                ],
            },
        }
    )

    afm_tip = Quantity(
        type=str,
        description='the model of the probing tip',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    afm_mode = Quantity(
        type=str,
        description='if proxy or in contact, if linear or scanning',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    afm_setpoint = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
    afm_fb_gain = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
    afm_tip_resonance = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='MHz',
    )
    afm_tip_phase = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
    afm_laser_intensity = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='mA',
    )
    afm_fb_gain_o = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
