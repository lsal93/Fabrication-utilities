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

import numpy as np
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.basesections import Analysis
from nomad.metainfo import (
    Datetime,
    Package,
    Quantity,
    Section,
    SubSection,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Definitions for usual operation of analysis')

class EtchingRateOutput(ArchiveSection):
    m_def=Section()

    etching_rate_value = Quantity(
        type=np.float64,
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit':'nm/minute'},
        unit='nm/minute'
    )

class EtchingRateInputs(ArchiveSection):
    m_def= Section()

    etching_time = Quantity(
        type=np.float64,
        a_eln = {'component':'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit = 'minute'
    )
    etching_time_reference = Quantity(
        type=Section,
        a_eln = {'component':'ReferenceEditQuantity'},
    )
    depth = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm'
    )
    depth_reference = Quantity(
        type=Section,
        a_eln = {'component':'ReferenceEditQuantity'},
    )

class EtchingRate(EntryData, ArchiveSection):
    m_def=Section()


    name = Quantity(
        type=str,
        a_eln={'component':'StringEditQuantity'}
    )

    ID = Quantity(
        type=str,
        a_eln={'component':'StringEditQuantity'}
    )

    datetime = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )

    location = Quantity(
        type=str,
        a_eln={'component':'StringEditQuantity'}
    )

    inputs= SubSection(
        section_def=EtchingRateInputs,
        repeats=False
    )

    output = SubSection(
        section_def=EtchingRateOutput,
        repeats=False
    )

    def normalize(self, archive:'EntryArchive', logger: 'BoundLogger')->None:
        super().normalize(archive, logger)
        if self.inputs.depth and self.inputs.etching_time:
            self.output.etching_rate_value=self.inputs.depth/self.inputs.etching_time


class DepositionRateOutput(ArchiveSection):
    m_def=Section()

    deposition_rate_value = Quantity(
        type=np.float64,
        a_eln={'component':'NumberEditQuantity', 'defaultDisplayUnit':'nm/minute'},
        unit='nm/minute'
    )

class DepositionRateInputs(ArchiveSection):
    m_def= Section()

    deposition_time = Quantity(
        type=np.float64,
        a_eln = {'component':'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit = 'minute'
    )
    deposition_time_reference = Quantity(
        type=Section,
        a_eln = {'component':'ReferenceEditQuantity'},
    )
    thickness = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm'
    )
    thickness_reference = Quantity(
        type=Section,
        a_eln = {'component':'ReferenceEditQuantity'},
    )

class DepositionRate(EntryData, ArchiveSection):
    m_def=Section()


    name = Quantity(
        type=str,
        a_eln={'component':'StringEditQuantity'}
    )

    ID = Quantity(
        type=str,
        a_eln={'component':'StringEditQuantity'}
    )

    datetime = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )

    location = Quantity(
        type=str,
        a_eln={'component':'StringEditQuantity'}
    )

    inputs= SubSection(
        section_def=DepositionRateInputs,
        repeats=False
    )

    output = SubSection(
        section_def=DepositionRateOutput,
        repeats=False
    )

    def normalize(self, archive:'EntryArchive', logger: 'BoundLogger')->None:
        super().normalize(archive, logger)
        if self.inputs.thickness and self.inputs.deposition_time:
            self.output.deposition_rate_value = (
                self.inputs.thickness/self.inputs.deposition_time
            )