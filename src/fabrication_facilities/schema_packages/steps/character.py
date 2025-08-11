#this .py component contains test classes and other entities needed to manage characterization, like
#characterization stesp, equipment, and the technology hirarchy/taxonomy
#characterization taxonomy referenced in this package is taken from CHADA

from fabrication_facilities.schema_packages.fabrication_utilities import EquipmentTechnique

from typing import (
    TYPE_CHECKING,
)

import numpy as np
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
    BeamColumn,
)
from fabrication_facilities.schema_packages.utils import (
    parse_chemical_formula,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Characterization processes schema')

class CharacterizationTechnique (EquipmentTechnique):
    m_def = Section(
        a_eln={
            'hide':['techniqueGeneralCategory'],
            'properties': {
                'order': [
                    'name',
                    'id',
                    'description',
                    'techniqueMainCategory',
                    'techniqueSubCategory',
                    'genericEquipmentName',
                    'techniqueSubCategory',
                    'referencingcategorization',
                ]
            }
        },
    techniqueMainCategory = Quantity(
        type=MEnum(
            [
                'Mechanical testing methods',
                'Microscopy based methods',
                'Spectroscopy based methods',
                'Diffraction based methods',
                'Light scattering techniques for nanoparticle analysis',
                'Tribological characterisation',
                'Thermal analysis methods',
                'Electrical characterisation methods',
                'Magnetic characterisation methods',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    techniqueSubCategory = Quantity(
        type=MEnum(
            [
                'Macroscopic scale mechanical testing',
                'Micro and nano-indentation',
                'In-situ micro/nano-mechanical testing',
                'Optical microscopy',
                'Electron microscopy',
                'Scanning probe microscopy',
                'Focused Ion Beam microscopy',
                'Scanning probe microscopy',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    

class AFMbase(FabricationProcessStepBase):
    m_def = Section(
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
                    'afm_tip',
                    'afm_mode',
                    'afm_setpoint',
                    'afm_fb_gain',
                    'afm_tip_resonance',
                    'afm_tip_phase',
                    'afm_laser_intensity',
                    'afm_fb_gain_o',
                    'notes',
                ]
            },
        },
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
        description='force applied to the tip',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='A',
    )
    afm_fb_gain = Quantity(
        type=np.float64,
        description='piezoelectric parameter',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
    afm_tip_resonance = Quantity(
        type=np.float64,
        description='tip calibration parameter',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='MHz',
    )
    afm_tip_phase = Quantity(
        type=np.float64,
        description='tip calibration parameter',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
    afm_laser_intensity = Quantity(
        type=np.float64,
        description='the laser source hitting the photodiode',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='mA',
    )
    afm_fb_gain_o = Quantity(
        type=np.float64,
        description='tip parameter',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )

#prova di modifica
