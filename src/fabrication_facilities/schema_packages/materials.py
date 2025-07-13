from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.eln import Chemical

from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import(
    EquipmentReference,
    FabricationProcessStep,
)

if TYPE_CHECKING:
    pass

m_package = Package(
    name='Materials plugin',
    description='Plugin to describe raw materials properties'
)

class EtchingProperties(ArchiveSection):

    m_def = Section(
        description='Class describing etching properties characterized for materials',
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
        description= 'Instrument through which the etching trial was performed',
        repeats=False,
    )

class FabricationChemical(Chemical, ArchiveSection):

    m_def = Section(
        definition = 'Chemicals for fabrication products',
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
        }
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

class Material(EntryData, ArchiveSection):

    m_def=Section(
        description='Class containeg all information measured for a raw material',
        a_eln={
            'properties':{
                'order':[
                    'name',
                    'ID',
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

    ID = Quantity(
        type=str,
        a_eln={
            'component':'StringEditQuantity',
        },
    )

    description = Quantity(
        type=str,
        a_eln={
            'component':'RichTextEditQuantity',
        },
    )

    location= Quantity(
        type=str,
        description= 'Laboratiory which produced the material',
        a_eln={
            'component':'StringEditQuantity',
        },
    )

    operator= Quantity(
        type=str,
        description= 'Physical person which produced the material',
        a_eln={
            'component':'StringEditQuantity',
        },
    )

    chemical_components=SubSection(
        section_def = FabricationChemical,
        repeats=True,
    )

    etching_rates_list= SubSection(
        section_def = EtchingProperties,
        repeats= True,
    )

