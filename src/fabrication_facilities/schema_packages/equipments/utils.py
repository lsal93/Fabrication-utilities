from typing import (
    TYPE_CHECKING,
)

#import numpy as np
from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity, Section, SubSection

#from fabrication_facilities.schema_packages.utils import (
#    FabricationChemical,
#)

if TYPE_CHECKING:
    pass

class Clamping_Capabilities(ArchiveSection):
    m_def = Section(
        description="""
        Class describing all parameters useful for clamping capabilites.
        """
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

class ChuckCapabilities(ArchiveSection):
    m_def = Section(
        description="""
        Section containing all parameters relative to the chuck.
        """
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

    clamping = SubSection(section_def=Clamping_Capabilities, repeats=False)


class ICP_ColumnCapabilities(ArchiveSection):
    m_def = Section(
        description="""
        Section used to describe available parameters  in the icp region
        """
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