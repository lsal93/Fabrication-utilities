#######################################################################################
#######################################################################################
# In this file will be defined entities which will be used to perform some operations #
# on data. In particular, we will define structures within some inputs are passed and #
# through the normalization method will give as output the properties to evaluate.    #
#######################################################################################
#######################################################################################
from typing import (
    TYPE_CHECKING,
)

#import numpy as np
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.basesections import Analysis
#from nomad.datamodel.metainfo.eln import
from nomad.metainfo import (
    # Datetime,
    Package,
    # Quantity,
    Section,
    # SubSection,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Definitions for usual operation of analysis')

class CalculusSheet(ArchiveSection):
    m_def=Section(
        description='Base class to define different specific calculus sheets',
    )


class EtchingRate(Analysis, EntryData, ArchiveSection):
    m_def=Section()
