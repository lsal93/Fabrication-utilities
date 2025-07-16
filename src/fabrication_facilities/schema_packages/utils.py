import re
from collections import defaultdict
from typing import (
    TYPE_CHECKING,
)

import numpy as np

from ase.data import atomic_masses as am
from ase.data import atomic_numbers as an

from nomad.datamodel.data import (ArchiveSection, EntryData)

from nomad.datamodel.metainfo.basesections import ElementalComposition

from nomad.datamodel.metainfo.plot import PlotSection

from nomad.datamodel.metainfo.eln import Chemical

from nomad.metainfo import (
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


def parse_chemical_formula(formula):
    formula = formula.replace('·', '.')
    if '.' in formula:
        main_part, hydrate_part = formula.split('.')
    else:
        main_part, hydrate_part = formula, None

    def extract_elements(compound):
        # Espressione per trovare elementi chimici seguiti da un numero opzionale
        matches = re.findall(r'([A-Z][a-z]*)(\d*)', compound)
        elements = defaultdict(int)

        for element, count in matches:
            elements[element] += int(count) if count else 1

        return elements

    element_main = defaultdict(int)

    # Espandiamo le parentesi prima di estrarre gli elementi
    while '(' in main_part:
        main_part = re.sub(
            r'\(([^()]*)\)(\d+)', lambda m: m.group(1) * int(m.group(2)), main_part
        )

    # Trova elementi e numeri
    matches = re.findall(r'([A-Z][a-z]*)(\d*)', main_part)

    for element, count in matches:
        element_main[element] += (
            int(count) if count else 1
        )  # Se il numero manca, assume 1

    if hydrate_part:
        hydrate_match = re.match(r'(\d*)H2O', hydrate_part)
        if hydrate_match:
            water_molecules = (
                int(hydrate_match.group(1)) if hydrate_match.group(1) else 1
            )
            elements_hydrate = extract_elements('H2O')

            for element, count in elements_hydrate.items():
                element_main[element] += count * water_molecules

    # Convertiamo il dizionario in due liste ordinate
    elements = list(element_main.keys())
    counts = list(element_main.values())

    return elements, counts


class FabricationChemical(Chemical, ArchiveSection):
    m_def = Section(
        definition='Chemicals for fabrication products',
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
        },
    )

    elemental_composition = SubSection(
        section_def=ElementalComposition,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_formula:
            elements, counts = parse_chemical_formula(self.chemical_formula)
            total = 0
            for token in counts:
                total += int(token)
            mass = sum(am[an[el]] * cou for el, cou in zip(elements, counts))
            if total != 0:
                elemental_fraction = np.array(counts) / total
                elementality = []
                i = 0
                for entry in elements:
                    elemental_try = ElementalComposition()
                    elemental_try.element = entry
                    elemental_try.atomic_fraction = elemental_fraction[i]
                    mass_frac = (am[an[entry]] * counts[i]) / mass
                    elemental_try.mass_fraction = mass_frac
                    i += 1
                    elementality.append(elemental_try)
            else:
                print('No elements provided')
            self.elemental_composition = elementality

# class RampOfGases(ArchiveSection):
#     m_def=Section(
#         a_plot=dict(
#             x='time'

#         )
#     )

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

    # ramp_flows= SubSection(
    #     section_def = RampOfGases,
    #     repeats=True
    # )

    # elemental_composition = SubSection(
    #     section_def=ElementalComposition,
    #     repeats=True,
    # )

    # def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
    #     super().normalize(archive, logger)
    #     if self.chemical_formula:
    #         elements, counts = parse_chemical_formula(self.chemical_formula)
    #         total = 0
    #         for token in counts:
    #             total += int(token)
    #         mass = sum(am[an[el]] * cou for el, cou in zip(elements, counts))
    #         if total != 0:
    #             elemental_fraction = np.array(counts) / total
    #             elementality = []
    #             i = 0
    #             for entry in elements:
    #                 elemental_try = ElementalComposition()
    #                 elemental_try.element = entry
    #                 elemental_try.atomic_fraction = elemental_fraction[i]
    #                 mass_frac = (am[an[entry]] * counts[i]) / mass
    #                 elemental_try.mass_fraction = mass_frac
    #                 i += 1
    #                 elementality.append(elemental_try)
    #         else:
    #             print('No elements provided')
    #         self.elemental_composition = elementality


# class ConditioningSteps(ArchiveSection):
#     duration = Quantity(
#         type=np.float64,
#         description='Time of conditioning',
#         a_eln={
#             'component': 'NumberEditQuantity',
#             'defaultDisplayUnit': 'sec',
#         },
#         unit='sec',
#     )

class CustomSection(PlotSection, EntryData):
    m_def = Section(
        # a_plotly_graph_object=[
        #     {
        #         'label': 'graph object 1',
        #         'data': {'x': '#time', 'y': '#chamber_pressure'},
        #         'layout': {
        #             'title': {
        #                 'text': 'Plot in section level'
        #             },
        #             'xaxis': {
        #                 'title': {
        #                     'text': 'x data'
        #                 }
        #             },
        #             'yaxis': {
        #                 'title': {
        #                     'text': 'y data'
        #                 }
        #             }
        #         }
        #     }, {
        #         'label': 'graph object 2',
        #         'data': {'x': '#time', 'y': '#substrate_temperature'}
        #     }
        # ],
#        a_plotly_express={
#            'label': 'fig 2',
#            'index': 2,
#            'method': 'scatter',
#            'x': '#substrate_temperature',
#            'y': '#chamber_pressure',
#            'color': '#chamber_pressure'
#        },
        a_plotly_subplots={
            'label': 'Subplot',
            'index': 1,
            'parameters': {'rows': 2, 'cols': 2},
            'layout': {
                'title': {
                    'text': 'All plots'
                }
            },
            'plotly_express': [
                {
                    'method': 'scatter',
                    'x': '#time',
                    'y': '#chamber_pressure',
                    'color': '#chamber_pressure'
                },
                {
                    'method': 'scatter',
                    'x': '#time',
                    'y': '#substrate_temperature',
                    'color': '#substrate_temperature'
                },
            ]
        }
    )
    time = Quantity(type=float, shape=['*'], unit='s', a_eln=dict(component='NumberEditQuantity'))
    substrate_temperature = Quantity(type=float, shape=['*'], unit='K', a_eln=dict(component='NumberEditQuantity'))
    chamber_pressure = Quantity(type=float, shape=['*'], unit='Pa', a_eln=dict(component='NumberEditQuantity'))