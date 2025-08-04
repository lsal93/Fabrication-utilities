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

# from fabrication_facilities.schema_packages.fabrication_utilities import (
# EquipmentReference,
#    FabricationProcess,
#    FabricationProcessStep,
# )
from fabrication_facilities.schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    pass

m_package = Package(
    name='Materials plugin', description='Plugin to describe raw materials properties'
)


class EtchingMeasures(ArchiveSection):
    m_def = Section(
        description='Class describing etching properties characterized for materials',
        a_eln={
            'properties': {
                'order': [
                    'recipe_name',
                    # 'link_to_step',
                    'etching_rate_measured',
                ],
            },
        },
    )

    recipe_name = Quantity(
        type=str,
        description='Recipe used to measure etching rate in the process',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    # link_to_step = Quantity(
    #     type=FabricationProcessStep,
    #     description='Link to reach the step with the parameters used',
    #     a_eln={'component': 'ReferenceEditQuantity'},
    # )

    etching_rate_measured = Quantity(
        type=np.float64,
        description='Value obtained for the etching rate',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm/minute',
        },
        unit='nm/minute',
    )

    # instrument = SubSection(
    #     section_def=EquipmentReference,
    #     description='Instrument through which the etching trial was performed',
    #     repeats=False,
    # )


class EtchingProperties(ArchiveSection):
    etching_results = SubSection(
        section_def=EtchingMeasures,
        repeats=True,
    )


class StressMeasures(ArchiveSection):
    m_def = Section(
        description='Class describing stress properties characterized for materials',
        a_eln={
            'properties': {
                'order': [
                    'stress_measured',
                ],
            },
        },
    )

    # recipe_name = Quantity(
    #     type=str,
    #     description='Recipe used to measure etching rate in the process',
    #     a_eln={
    #         'component': 'StringEditQuantity',
    #     },
    # )

    # link_to_step = Quantity(
    #     type=FabricationProcessStep,
    #     description='Link to reach the step with the parameters used',
    #     a_eln={'component': 'ReferenceEditQuantity'},
    # )

    stress_measured = Quantity(
        type=np.float64,
        description='Value obtained for the etching rate',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'GPa',
        },
        unit='GPa',
    )

    # instrument = SubSection(
    #     section_def=EquipmentReference,
    #     description='Instrument through which the etching trial was performed',
    #     repeats=False,
    # )


class StressProperties(ArchiveSection):
    # instrument = SubSection(
    #     section_def=EquipmentReference,
    #     description='Instrument through which the characterization was performed',
    #     repeats=False,
    # )
    stress_results = SubSection(
        section_def=StressMeasures,
        repeats=True,
    )


# class ElectricProperties(ArchiveSection):
#     instrument = SubSection(
#         section_def=EquipmentReference,
#         description='Instrument through which the characterization was performed',
#         repeats=False,
#     )


class FabricationOutput(ArchiveSection):
    m_def = Section(
        description="""
        Ideal class to inherit to define any kind of outputs from a FabricationProcess.
        """
    )


class FabricationMaterial(FabricationOutput):
    m_def = Section(
        description='Class containeg all information measured for a raw material',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'ID',
                    'description',
                    'location',
                    # 'operator',
                    # 'production_process_name',
                    # 'production_process_reference',
                ]
            }
        },
    )

    name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    ID = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    description = Quantity(
        type=str,
        a_eln={
            'component': 'RichTextEditQuantity',
        },
    )

    location = Quantity(
        type=str,
        description='Laboratiory which produced the material',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    # operator = Quantity(
    #     type=str,
    #     description='Physical person which produced the material',
    #     a_eln={
    #         'component': 'StringEditQuantity',
    #     },
    # )

    # production_process_name = Quantity(
    #     type=str,
    #     description='Name of the referenced process used in the production',
    #     a_eln={
    #         'component': 'StringEditQuantity',
    #     },
    # )

    # production_process_reference = Quantity(
    #     type=FabricationProcess,
    #     description='Link to fabrication process employed',
    #     a_eln={'component': 'ReferenceEditQuantity'},
    # )

    chemical_components = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    etching_properties = SubSection(
        section_def=EtchingProperties,
        repeats=False,
    )

    stress_properties = SubSection(
        section_def=StressProperties,
        repeats=False,
    )

    # geometric_properties = SubSection(
    #     section_def=ProfileProperties,
    #     repeats=False,
    # )

    # electric_properties = SubSection(
    #     section_def=ElectricProperties,
    #     repeats=False,
    # )
