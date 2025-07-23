from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    SearchQuantities,
)

from fabrication_facilities.apps.directories import dir_path
from fabrication_facilities.apps.menu_steps import (
    menuadd_bonding,
    menuadd_electrongun,
    menuadd_icpcvd,
    menuadd_lpcvd,
    menuadd_pecvd,
    menuadd_sog,
    menuadd_spincoat,
    menuadd_sputtering,
    menuremove_driebosch,
    menuremove_icprie,
    menuremove_rie,
    menuremove_stripping,
    menuremove_wetclean,
    menuremove_wetetching,
    menutrans_annealing,
    menutrans_baking,
    menutrans_develop,
    menutrans_dicing,
    menutrans_doping,
    menutrans_ebl,
    menutrans_fib,
    menutrans_labelingcleaning,
    menutrans_ltodensification,
    menutrans_sod,
    menutrans_thermaloxidation,
    menutrans_track,
    menuutils_obsmeasurements,
    menuutils_startingmaterial,
)

schemas = [f'*#{path_value}' for path_value in dir_path.values()]
fps = 'FabricationProcessStep'
dir0 = f'fabrication_facilities.schema_packages.fabrication_utilities.{fps}'
schemas.append(f'*#{dir0}')

stepapp = App(
    label='Fabrication steps',
    path='stepapp',
    category='Fabrication facilities',
    description='App to search fabrication steps.',
    readme="""
    This app is intended to navigate around the ecosystem of clean room fabrication
    possible steps. At the beginning you can see all the fabrication steps available
    in nomad and than through the filters you can specialize the research per single
    technique. Navigation that consists in multiple technique is not allowed.
    """,
    search_quantities=SearchQuantities(include=schemas),
    columns=[
        Column(quantity='entry_name', selected=True),
        Column(quantity='entry_type', selected=True),
        Column(
            quantity=f'data.affiliation#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.location#{dir0}',
            selected=True,
        ),
        Column(quantity='upload_create_time', selected=True),
        Column(quantity=f'data.recipe_name#{dir0}'),
    ],
    filters_locked={'section_defs.definition_qualified_name': dir0},
    menu=Menu(
        items=[
            Menu(
                title='Add steps',
                indentation=0,
                items=[
                    Menu(
                        title='Bonding',
                        items=[
                            menuadd_bonding,
                        ],
                    ),
                    Menu(
                        title='Integration',
                        items=[],
                    ),
                    Menu(
                        title='Sinthesys',
                        items=[
                            menuadd_lpcvd,
                            menuadd_pecvd,
                            menuadd_icpcvd,
                            menuadd_spincoat,
                            menuadd_electrongun,
                            menuadd_sputtering,
                            menuadd_sog,
                        ],
                    ),
                ],
            ),
            Menu(
                title='Transform steps',
                indentation=0,
                items=[
                    Menu(
                        title='Dicing',
                        items=[
                            menutrans_dicing,
                        ],
                    ),
                    Menu(
                        title='Doping',
                        items=[
                            menutrans_doping,
                            menutrans_sod,
                        ],
                    ),
                    Menu(
                        title='Lithography',
                        items=[
                            menutrans_ebl,
                            menutrans_fib,
                            menutrans_track,
                        ],
                    ),
                    Menu(
                        title='Solution modification',
                        items=[
                            menutrans_develop,
                        ],
                    ),
                    Menu(
                        title='Thermal processing',
                        items=[
                            menutrans_annealing,
                            menutrans_ltodensification,
                            menutrans_thermaloxidation,
                            menutrans_baking,
                        ],
                    ),
                    Menu(
                        title='Labeling',
                        items=[
                            menutrans_labelingcleaning,
                        ],
                    ),
                ],
            ),
            Menu(
                title='Remove steps',
                indentation=0,
                items=[
                    Menu(
                        title='Etching',
                        items=[
                            menuremove_rie,
                            menuremove_icprie,
                            menuremove_driebosch,
                            menuremove_wetetching,
                            menuremove_wetclean,
                            menuremove_stripping,
                        ],
                    ),
                ],
            ),
            Menu(
                title='Characterization steps',
                indentation=0,
                items=[
                    Menu(
                        title='Measurements',
                        items=[
                            menuutils_obsmeasurements,
                        ],
                    ),
                ],
            ),
            Menu(
                title='Starting material',
                items=[
                    menuutils_startingmaterial,
                ],
            ),
            Menu(
                title='User defined quantities',
                items=[
                    MenuItemCustomQuantities(
                        title='Costumer user quantities',
                        type='custom_quantities',
                    ),
                ],
            ),
        ],
    ),
)
