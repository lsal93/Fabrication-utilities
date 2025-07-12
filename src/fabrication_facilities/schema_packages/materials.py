from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.basesections import (
    Entity,
)
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import{
    EquipmentReference,
    FabricationProcessStep,
}

if TYPE_CHECKING:
    pass

m_package = Package(
    name='Materials plugin',
    description='Plugin to describe raw materials properties'
)

class Etching_Properties(ArchiveSection):

    m_def = Section(
        description='Class describing etching properties characterized for materials'
        a_eln={
            'properties': {
                'order': [
                    'recipe_name',
                    'link_to_step',
                    'etching_rate_measured',
                ],
            },
        },
    )

    recipe_name=Quantity(
        type= str,
        description= 'Recipe used to measure etching rate in the process',
        a_eln={
            'component':'StringEditQuantity',
        },
    )

    link_to_step=Quantity(
        type=FabricationProcessStep,
        description='Link to reach the step with the parameters used',
        a_eln={'component':'ReferenceEditQuantity'},
    )

    etching_rate_measured=Quantity(
        type=np.float64,
        description='Value obtained for the etching rate',
        a_eln={
            'component':'NumberEditQuantity',
            'defaultDisplayUnit':'nm/minute',
        },
        unit='nm/minute',
    )

    instrument=SubSection(
        section_def= EquipmentReference,
        repeats=False,
    )

class Material(EntryData, ArchiveSection):

    m_def=Section(
        description='Class containeg all information measured for a raw material',
        a_eln={
            'properties':{
                'order':[
                    'name',
                    'id',
                    'description',
                    'location',
                    'operator',
                    'production_method',
                    'link_to_production_process',
                ]
            }
        }
    )

    name=Quantity(
        type=str,
        a_eln={
            'component':'StringEditQuantity',
        },
    )

    