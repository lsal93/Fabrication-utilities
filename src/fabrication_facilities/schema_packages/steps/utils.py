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

from fabrication_facilities.schema_packages.utils import (
    TimeRampPressure,
    TimeRampMassflow,
    TimeRampTemperature,
    FabricationChemical
)

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


class Chuck (ArchiveSection):
    m_def=Section(
        description="""
        Section containing all parameters relative to the chuck.
        """
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
        description='Voltage imposed on the sample by electrodes',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )

    temperature_ramps = SubSection(
        section_def = TimeRampTemperature,
        repeats=True,
    )

class DRIE_Chuck(ArchiveSection):
    m_def=Section(
        description="""
        Section containing all parameters relative to the chuck in a DRIE process. The
        main property is the existence of an alternate powering for electrical data,
        so also the duration of each phase is reported.
        """
    )

    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    high_chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the high phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    low_chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the low phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    high_chuck_power_duration = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the high phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    low_chuck_power_duration = Quantity(
        type=np.float64,
        description='Duration of the low phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    chuck_frequency = Quantity(
        type=np.float64,
        description='Frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    bias = Quantity(
        type=np.float64,
        description='Voltage imposed on the sample by electrodes',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )

    temperature_ramps = SubSection(
        section_def = TimeRampTemperature,
        repeats=True,
    )


class Carrier(ArchiveSection):

    m_def=Section(
        description="""
        Section describing a component used to carry vertically
        """
    )


class Chamber(ArchiveSection):

    m_def=Section(
        description="""
        Section describing parameters and components inside the chamber, where sample
        is located. Eventually also the chuck and/or the item carrier could be
        described.
        """
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

    item_carrier = SubSection(
        section_def = Carrier,
        repeats = False
    )

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    temperature_ramps=SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )


class Massflow_controller(FabricationChemical, ArchiveSection):
    m_def = Section(
        a_eln={'overview': True, 'hide': ['lab_id', 'datetime']},
    )
    massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    gaseous_massflow_ramps = SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )


class DRIE_Massflow_controller(Massflow_controller):
    m_def = Section(
        a_eln={'overview': True, 'hide': ['lab_id', 'datetime', 'massflow']},
    )

    priority = Quantity(
        type=str,
        description='Parameter describing the ordering in the chemical reactivity',
        a_eln={'component': 'StringEditQuantity'},
    )

    inactive_state_massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows in the inactive phase of DRIE',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    active_state_massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows in the inactive phase of DRIE',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    pulse_time = Quantity(
        type=np.float64,
        description='Atomistic time of activity for the gas',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )


class ResistivityControl(ArchiveSection):
    m_def = Section(
        description='Section used in case of resistivity feedbacks',
    )

    resistivity_target = Quantity(
        type=np.float64,
        description='Value used as target to stop the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
        unit='ohm*cm',
    )

    increment_duration = Quantity(
        type=np.float64,
        description='Time used in the process to reach the target value',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
