from nomad.config.models.ui import (
    Axis,
    Menu,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
)

from fabrication_facilities.apps.directories import dir_path

menuadd_icpcvd = Menu(
    title='ICP-CVD',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir1"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'data.material_elemental_composition.element#{dir_path["dir1"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir1"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'data.fluximeters.elemental_composition.element#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.fluximeters.name#{dir_path["dir1"]}',
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.chuck_temperature#{dir_path["dir1"]}',
                title='chuck_temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Bias',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.bias#{dir_path["dir1"]}',
                title='bias',
                unit='volt',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.chamber_pressure#{dir_path["dir1"]}',
                title='chamber_pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.power#{dir_path["dir1"]}',
                title='chamber_pressure',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_measured#{dir_path["dir1"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Thickness obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_measured#{dir_path["dir1"]}',
                title='thickness obtained',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_obtained#{dir_path["dir1"]}',
                title='deposition rate obtained',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir1"]}',
        ),
    ],
)

menuadd_spincoat = Menu(
    title='Spin Coating',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='Resist to be deposited',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir2"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the resist deposited',
            type='periodic_table',
            search_quantity=f'data.resist_elemental_composition.element#{dir_path["dir2"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir2"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemTerms(
            title='HDMS',
            type='terms',
            search_quantity=f'data.hdms_required#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='PEB',
            type='terms',
            search_quantity=f'data.peb_required#{dir_path["dir2"]}',
        ),
        MenuItemHistogram(
            title='PEB duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.peb_duration#{dir_path["dir2"]}',
                title='peb duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='PEB temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.peb_temperature#{dir_path["dir2"]}',
                title='peb temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Exposure',
            type='terms',
            search_quantity=f'data.exposure_required#{dir_path["dir2"]}',
        ),
        MenuItemHistogram(
            title='Exposure duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.exposure_duration#{dir_path["dir2"]}',
                title='exposure duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='De-wetting duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dewetting_duration#{dir_path["dir2"]}',
                title='de-wetting duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='De-wetting temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dewetting_temperature#{dir_path["dir2"]}',
                title='De-wetting temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Spinned volume',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_dispensed_volume#{dir_path["dir2"]}',
                title='volume dispensed',
                unit='milliliter',
            ),
        ),
        MenuItemHistogram(
            title='Spin duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_duration#{dir_path["dir2"]}',
                title='spin duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_frequency#{dir_path["dir2"]}',
                title='frequency',
                unit='rpm',
            ),
        ),
        MenuItemHistogram(
            title='Spin angular acceleration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_angular_acceleration#{dir_path["dir2"]}',
                title='angular acceleration',
                unit='rpm/sec',
            ),
        ),
        MenuItemHistogram(
            title='Baking duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.baking_duration#{dir_path["dir2"]}',
                title='baking duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Baking temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.baking_temperature#{dir_path["dir2"]}',
                title='baking temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Thickness obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_measured#{dir_path["dir2"]}',
                title='thickness obtained',
                unit='nm',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir2"]}',
        ),
    ],
)
menuadd_bonding = Menu(
    title='Bonding',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer bonding type',
            type='terms',
            search_quantity=f'data.wafer_bonding_type#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Alignment required',
            type='terms',
            search_quantity=f'data.alignment_required#{dir_path["dir8"]}',
        ),
        MenuItemHistogram(
            title='Alignment max error',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.alignment_max_error#{dir_path["dir8"]}',
                title='alignment error',
                unit='nm',
            ),
        ),
        MenuItemTerms(
            title='Wafer stack 1 name',
            type='terms',
            search_quantity=f'data.wafer_stack_1_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer stack 2 name',
            type='terms',
            search_quantity=f'data.wafer_stack_2_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer space required',
            type='terms',
            search_quantity=f'data.wafer_space_required#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Alignment target mask name',
            type='terms',
            search_quantity=f'data.alignment_target_mask_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Alignment viewfinder mask name',
            type='terms',
            search_quantity=f'data.alignment_viewfinder_mask_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer bonded name',
            type='terms',
            search_quantity=f'data.wafer_bonded_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir8"]}',
        ),
    ],
)
menutrans_ebl = Menu(
    title='E-Beam Lithography',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir3"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir3"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir3"]}',
        ),
        MenuItemHistogram(
            title='Dose',
            type='histogram',
            n_bins=10,
            x=Axis(title='dose', unit='uC/cm^2', search_quantity=f'data.dose#{dir_path["dir3"]}'),
        ),
        MenuItemHistogram(
            title='Writing field dimension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='writing field dimension',
                unit='um^2',
                search_quantity=f'data.writing_field_dimension#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Address size',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='address size',
                unit='nm',
                search_quantity=f'data.address_size#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Clock',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='clock',
                unit='MHz',
                search_quantity=f'data.clock#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Current',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='current',
                unit='pA',
                search_quantity=f'data.current#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='chamber pressure',
                unit='mbar',
                search_quantity=f'data.chamber_pressure#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Tension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='tension',
                unit='V',
                search_quantity=f'data.tension#{dir_path["dir3"]}',
            ),
        ),
        MenuItemTerms(
            title='Alignment required',
            type='terms',
            search_quantity=f'data.alignment_required#{dir_path["dir3"]}',
        ),
        MenuItemHistogram(
            title='Max alignment error',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='max alignment error',
                unit='nm',
                search_quantity=f'data.alignment_max_error#{dir_path["dir3"]}',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir3"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir3"]}',
        ),
    ],
)
menutrans_fib = Menu(
    title='Focused I-Beam Lithography',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir4"]}',
        ),
        MenuItemHistogram(
            title='Dose',
            type='histogram',
            n_bins=10,
            x=Axis(title='dose', unit='uC/cm^2', search_quantity=f'data.dose#{dir_path["dir4"]}'),
        ),
        MenuItemHistogram(
            title='Writing field dimension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='writing field dimension',
                unit='um^2',
                search_quantity=f'data.writing_field_dimension#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Address size',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='address size',
                unit='nm',
                search_quantity=f'data.address_size#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Clock',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='clock',
                unit='MHz',
                search_quantity=f'data.clock#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Current',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='current',
                unit='pA',
                search_quantity=f'data.current#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='chamber pressure',
                unit='mbar',
                search_quantity=f'data.chamber_pressure#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Tension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='tension',
                unit='V',
                search_quantity=f'data.tension#{dir_path["dir4"]}',
            ),
        ),
        MenuItemTerms(
            title='Alignment required',
            type='terms',
            search_quantity=f'data.alignment_required#{dir_path["dir4"]}',
        ),
        MenuItemHistogram(
            title='Max alignment error',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='max alignment error',
                unit='nm',
                search_quantity=f'data.alignment_max_error#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='N° of loops',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='n° of loops',
                search_quantity=f'data.number_of_loops#{dir_path["dir4"]}',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir4"]}',
        ),
    ],
)
menutrans_develop = Menu(
    title='Resist development',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Developing solution',
            type='terms',
            search_quantity=f'data.developing_solution#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Removing solution proportions',
            type='terms',
            search_quantity=f'data.developing_solution_proportions#{dir_path["dir7"]}',
        ),
        MenuItemHistogram(
            title='Developing duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.developing_duration#{dir_path["dir7"]}',
                title='developing duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Developing temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.developing_temperature#{dir_path["dir7"]}',
                title='developing temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Cleaning solution',
            type='terms',
            search_quantity=f'data.cleaning_solution#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Cleaning solution proportions',
            type='terms',
            search_quantity=f'data.cleaning_solution_proportions#{dir_path["dir7"]}',
        ),
        MenuItemHistogram(
            title='Cleaning duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.cleaning_duration#{dir_path["dir7"]}',
                title='cleaning duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir7"]}',
        ),
    ],
)

menuetchdrie = Menu(
    title='DRIE',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir5"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'data.material_elemental_composition.element#{dir_path["dir5"]}',
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir5"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Desired depth',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir5"]}',
                title='depth',
                unit='nm',
            ),
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'data.fluximeters.elemental_composition.element#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.fluximeters.chemical_formula#{dir_path["dir5"]}',
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.chuck_temperature#{dir_path["dir5"]}',
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Bias',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.bias#{dir_path["dir5"]}',
                title='bias',
                unit='V',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.chamber_pressure#{dir_path["dir5"]}',
                title='chamber_pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.power#{dir_path["dir5"]}',
                title='power',
                unit='W',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_measured#{dir_path["dir5"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Depth obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_measured#{dir_path["dir5"]}',
                title='depth obtained',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Etching rate obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_obtained#{dir_path["dir5"]}',
                title='etching rate obtained',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir5"]}',
        ),
    ],
)
menuetchwetclean = Menu(
    title='Wet cleaning',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Removing solution',
            type='terms',
            search_quantity=f'data.removing_solution#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Removing solution proportions',
            type='terms',
            search_quantity=f'data.removing_solution_proportions#{dir_path["dir6"]}',
        ),
        MenuItemHistogram(
            title='Removing duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.removing_duration#{dir_path["dir6"]}',
                title='removing duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Removing temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.removing_temperature#{dir_path["dir6"]}',
                title='removing temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Rising solution',
            type='terms',
            search_quantity=f'data.rising_solution#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Rising solution proportions',
            type='terms',
            search_quantity=f'data.rising_solution_proportions#{dir_path["dir6"]}',
        ),
        MenuItemHistogram(
            title='Rising duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rising_duration#{dir_path["dir6"]}',
                title='rising duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir6"]}',
        ),
    ],
)
menutrans_annealing = Menu(
    title='Annealing',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='Material to be annealed',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir9"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the material',
            type='periodic_table',
            search_quantity=f'data.material_elemental_composition.element#{dir_path["dir9"]}',
        ),
        MenuItemHistogram(
            title='Starting temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.temperature_start#{dir_path["dir9"]}',
                title='starting temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Target final temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.temperature_final_target#{dir_path["dir9"]}',
                title='target final temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Gas name',
            type='terms',
            search_quantity=f'data.gas_name#{dir_path["dir9"]}',
        ),
        MenuItemHistogram(
            title='Gas percentage',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.gas_percentage#{dir_path["dir9"]}',
                title='gas percentage',
            ),
        ),
        MenuItemHistogram(
            title='Gas flow',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.gas_flow#{dir_path["dir9"]}',
                title='gas flow',
            ),
        ),
        MenuItemHistogram(
            title='Measured final temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.temperature_final_measured#{dir_path["dir9"]}',
                title='measured final temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_measured#{dir_path["dir9"]}',
                title='duration measured',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Ramp up rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.temperature_ramp_up_rate#{dir_path["dir9"]}',
                title='ramp up rate',
                unit='celsius/minute',
            ),
        ),
        MenuItemHistogram(
            title='Ramp down rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.temperature_ramp_down_rate#{dir_path["dir9"]}',
                title='ramp down rate',
                unit='celsius/minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir9"]}',
        ),
    ],
)
menutrans_ltodensification = Menu(
    title='LTO Densification',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir10"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir10"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir10"]}',
        ),
        MenuItemTerms(
            title='Densification type',
            type='terms',
            search_quantity=f'data.densification_type#{dir_path["dir10"]}',
        ),
        MenuItemTerms(
            title='Densification gas',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir10"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the gas',
            type='periodic_table',
            search_quantity=f'data.gas_elemental_composition.element#{dir_path["dir10"]}',
        ),
        MenuItemHistogram(
            title='Densification temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.densification_temperature#{dir_path["dir10"]}',
                title='densification temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Gas flow',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.gas_flow#{dir_path["dir10"]}',
                title='gas flow',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_measured#{dir_path["dir10"]}',
                title='duration measured',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir10"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir10"]}',
        ),
    ],
)
menutrans_thermaloxidation = Menu(
    title='Thermal Oxidation',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='Oxidation type',
            type='terms',
            search_quantity=f'data.oxidation_type#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='Thermal oxidation gas',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir11"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the gas',
            type='periodic_table',
            search_quantity=f'data.gas_elemental_composition.element#{dir_path["dir11"]}',
        ),
        MenuItemHistogram(
            title='Target final temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.temperature_final_target#{dir_path["dir11"]}',
                title='target final temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Desired thickness (target)',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir11"]}',
                title='thickness target',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Process duration (measured)',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_measured#{dir_path["dir11"]}',
                title='duration measured',
                unit='s',
            ),
        ),
        MenuItemHistogram(
            title='Thickness obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_measured#{dir_path["dir11"]}',
                title='thickness measured',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Gas flow',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.gas_flow#{dir_path["dir11"]}',
                title='gas flow',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir11"]}',
        ),
    ],
)
menutrans_dicing = Menu(
    title='Dicing',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='Blade name',
            type='terms',
            search_quantity=f'data.dicing_blade_name#{dir_path["dir12"]}',
        ),
        MenuItemHistogram(
            title='Depth target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir12"]}',
                title='depth target',
                unit='um',
            ),
        ),
        MenuItemTerms(
            title='Protective film required',
            type='terms',
            search_quantity=f'data.protective_film_required#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='File name',
            type='terms',
            search_quantity=f'data.file_name#{dir_path["dir12"]}',
        ),
        MenuItemHistogram(
            title='Spindle frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spindle_frequency#{dir_path["dir12"]}',
                title='spindle frequency',
                unit='rpm',
            ),
        ),
        MenuItemHistogram(
            title='Dicing feed rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dicing_feed_rate#{dir_path["dir12"]}',
                title='feed rate',
                unit='mm/s',
            ),
        ),
        MenuItemHistogram(
            title='Depth step 1',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_step_1#{dir_path["dir12"]}',
                title='depth step 1',
                unit='um',
            ),
        ),
        MenuItemHistogram(
            title='Depth step 2',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_step_2#{dir_path["dir12"]}',
                title='depth step 2',
                unit='um',
            ),
        ),
        MenuItemHistogram(
            title='Depth step 3',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_step_3#{dir_path["dir12"]}',
                title='depth step 3',
                unit='um',
            ),
        ),
        MenuItemHistogram(
            title='Dicing edge chipping measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dicing_edge_chipping_measured#{dir_path["dir12"]}',
                title='edge chipping measured',
                unit='um',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir12"]}',
        ),
    ],
)
