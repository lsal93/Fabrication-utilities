####################################
# In questo file inserisco tutte le funzionalità e le sezioni che mi saranno utili per
# la descrizione degli steps istanze particolari di ogni superclasse. Ad esempio qui
# definirò la sezione contenente tutti i parametri relativi a una colonna ICP utile sia
# per alcuni processi RIE e alcnui processi CVD.
####################################

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.metainfo import MEnum, Quantity, Section, SubSection

from fabrication_facilities.schema_packages.utils import TimeRampPressure

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

class ICP_Column(ArchiveSection):

    m_def=Section(
        description="""
        Section used to describe component to obtaine inductively coupled plasma
        """
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

class Clamping_System(ArchiveSection):

    m_def=Section(
        description="""
        Class describing all parameters useful for clamping, if used during the step.
        """
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
        description='Adhesion pressure generated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

class Electric_Inputs(ArchiveSection):

    m_def=Section(
        description="""
        Section containing all parameters selected to generate the plasma and
        active on the chuck.
        """
    )

    