from nomad.config.models.ui import (
    Axis,
    Menu,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
)

from fabrication_facilities.apps.directories import dir_path

mec = 'data.synthesis_steps.material_elemental_composition.element'
flux = 'data.synthesis_steps.fluximeters.elemental_composition.element'
fluxetch = 'data.etching_steps.fluximeters.elemental_composition.element'
rec = 'data.resist_elemental_composition.element'
gec = 'data.gas_elemental_composition.element'
dmec = 'data.doping_material_elemental_composition.element'
sec = 'data.substrate_elemental_composition.element'
wc = 'wafer_cleaning'
dev = 'developing'
meec = 'data.etching_steps.materials_etched.elemental_composition.element'
rute = 'data.reactives_used_to_etch.elemental_composition.element'
ru = 'reactive_used_to_etch'
alias = 'data.synthesis_steps.target_material_formula'

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
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir1"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_target#{dir_path["dir1"]}',
                title='deposition rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.synthesis_steps.tag#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.synthesis_steps.short_name#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Formula of the material to be deposited',
            type='terms',
            search_quantity=f'{alias}#{dir_path["dir1"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'{mec}#{dir_path["dir1"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{flux}#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.chemical_formula#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.name#{dir_path["dir1"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.fluximeters.massflow#{dir_path["dir1"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Wall temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.wall_temperature#{dir_path["dir1"]}',
                title='wall_temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck_temperature#{dir_path["dir1"]}',
                title='chuck_temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Bias',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.bias#{dir_path["dir1"]}',
                title='bias',
                unit='volt',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_pressure#{dir_path["dir1"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck_power#{dir_path["dir1"]}',
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck_frequency#{dir_path["dir1"]}',
                title='chuck frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='ICP Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.icp_power#{dir_path["dir1"]}',
                title='icp power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='ICP Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.icp_frequency#{dir_path["dir1"]}',
                title='icp frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=f'data.synthesis_steps.clamping#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Clamping type',
            type='terms',
            search_quantity=f'data.synthesis_steps.clamping_type#{dir_path["dir1"]}',
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.clamping_pressure#{dir_path["dir1"]}',
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir1"]}',
                title='effective duration',
                unit='minute',
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

menuadd_pecvd = Menu(
    title='PECVD',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir27"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir27"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir27"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_target#{dir_path["dir27"]}',
                title='deposition rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.synthesis_steps.short_name#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Formula of the material to be deposited',
            type='terms',
            search_quantity=f'{alias}#{dir_path["dir27"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'{mec}#{dir_path["dir27"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{flux}#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.chemical_formula#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.name#{dir_path["dir27"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.fluximeters.massflow#{dir_path["dir27"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Wall temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.wall_temperature#{dir_path["dir27"]}',
                title='wall_temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck_temperature#{dir_path["dir27"]}',
                title='chuck_temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Bias',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.bias#{dir_path["dir27"]}',
                title='bias',
                unit='volt',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_pressure#{dir_path["dir27"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck_power#{dir_path["dir27"]}',
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck_frequency#{dir_path["dir27"]}',
                title='chuck frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=f'data.synthesis_steps.clamping#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Clamping type',
            type='terms',
            search_quantity=f'data.synthesis_steps.clamping_type#{dir_path["dir27"]}',
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.clamping_pressure#{dir_path["dir27"]}',
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir27"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir27"]}',
        ),
    ],
)

menuadd_lpcvd = Menu(
    title='LPCVD',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir28"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir28"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir28"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_target#{dir_path["dir28"]}',
                title='deposition rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.synthesis_steps.short_name#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Formula of the material to be deposited',
            type='terms',
            search_quantity=f'{alias}#{dir_path["dir28"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'{mec}#{dir_path["dir28"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{flux}#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.chemical_formula#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.name#{dir_path["dir28"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.fluximeters.massflow#{dir_path["dir28"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Wall temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.wall_temperature#{dir_path["dir28"]}',
                title='wall_temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck_temperature#{dir_path["dir28"]}',
                title='chuck_temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_pressure#{dir_path["dir28"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=f'data.synthesis_steps.clamping#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Clamping type',
            type='terms',
            search_quantity=f'data.synthesis_steps.clamping_type#{dir_path["dir28"]}',
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.clamping_pressure#{dir_path["dir28"]}',
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir28"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir28"]}',
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
        MenuItemTerms(
            title='Formulas of the resist',
            type='terms',
            search_quantity=f'data.chemical_formula#{dir_path["dir2"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the resist deposited',
            type='periodic_table',
            search_quantity=f'{rec}#{dir_path["dir2"]}',
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
            title='Exposure power density',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.exposure_intensity#{dir_path["dir2"]}',
                title='exposure power density',
                unit='mwatt/cm^2',
            ),
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
        MenuItemTerms(
            title='Bake',
            type='terms',
            search_quantity=f'data.baking_required#{dir_path["dir2"]}',
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
            x=Axis(
                title='dose',
                unit='uC/cm^2',
                search_quantity=f'data.dose#{dir_path["dir3"]}',
            ),
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
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='chuck temperature',
                unit='celsius',
                search_quantity=f'data.chuck_temperature#{dir_path["dir3"]}',
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
            x=Axis(
                title='dose',
                unit='uC/cm^2',
                search_quantity=f'data.dose#{dir_path["dir4"]}',
            ),
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
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='chuck temperature',
                unit='celsius',
                search_quantity=f'data.chuck_temperature#{dir_path["dir4"]}',
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
            title='Developing solution proportions',
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
            title='Stopping solution',
            type='terms',
            search_quantity=f'data.stopping_solution#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Stopping solution proportions',
            type='terms',
            search_quantity=f'data.stopping_solution_proportions#{dir_path["dir7"]}',
        ),
        MenuItemHistogram(
            title='Stopping duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.stopping_duration#{dir_path["dir7"]}',
                title='stopping duration',
                unit='sec',
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

menuremove_icprie = Menu(
    title='ICP RIE',
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
            title='Etching rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_target#{dir_path["dir5"]}',
                title='etching rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.etching_steps.tag#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Material to be etched',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.name#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Formulas of the etched material',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.chemical_formula#{dir_path["dir5"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements etched',
            type='periodic_table',
            search_quantity=f'{meec}#{dir_path["dir5"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{fluxetch}#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.chemical_formula#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.name#{dir_path["dir5"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.fluximeters.massflow#{dir_path["dir5"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_temperature#{dir_path["dir5"]}',
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Wall temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.wall_temperature#{dir_path["dir5"]}',
                title='wall temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Bias',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.bias#{dir_path["dir5"]}',
                title='bias',
                unit='V',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_pressure#{dir_path["dir5"]}',
                title='chamber_pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_power#{dir_path["dir5"]}',
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_frequency#{dir_path["dir5"]}',
                title='chuck frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='ICP Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.icp_power#{dir_path["dir5"]}',
                title='icp power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='ICP Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.icp_frequency#{dir_path["dir5"]}',
                title='icp frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=f'data.etching_steps.clamping#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Clamping type',
            type='terms',
            search_quantity=f'data.etching_steps.clamping_type#{dir_path["dir5"]}',
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.clamping_pressure#{dir_path["dir5"]}',
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir5"]}',
                title='effective duration',
                unit='minute',
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
menuremove_wetclean = Menu(
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
            search_quantity=f'{mec}#{dir_path["dir9"]}',
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
            title='Gas formula',
            type='terms',
            search_quantity=f'data.gas_formula#{dir_path["dir9"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the gas',
            type='periodic_table',
            search_quantity=f'{gec}#{dir_path["dir9"]}',
        ),
        MenuItemHistogram(
            title='Gas percentage',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.gas_percentage#{dir_path["dir9"]}',
                title='gas percentage (%)',
            ),
        ),
        MenuItemHistogram(
            title='Gas flow',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.gas_flow#{dir_path["dir9"]}',
                title='gas flow',
                unit='centimeter^3/minute',
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
            search_quantity=f'{gec}#{dir_path["dir10"]}',
        ),
        MenuItemHistogram(
            title='Densification temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.temperature_target#{dir_path["dir10"]}',
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
                unit='centimeter^3/minute',
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
            search_quantity=f'{gec}#{dir_path["dir11"]}',
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
                unit='centimeter^3/minute',
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
                search_quantity=f'data.edge_chipping_measured#{dir_path["dir12"]}',
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
menutrans_doping = Menu(
    title='Doping',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir13"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir13"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir13"]}',
        ),
        MenuItemTerms(
            title='Doping type',
            type='terms',
            search_quantity=f'data.doping_type#{dir_path["dir13"]}',
        ),
        MenuItemHistogram(
            title='Doping temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.temperature_target#{dir_path["dir13"]}',
                title='doping temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Doping duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir13"]}',
                title='doping duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Surface resistance measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.surface_resistance_measured#{dir_path["dir13"]}',
                title='surface resistance measured',
                unit='ohm',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir13"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir13"]}',
        ),
    ],
)
menutrans_labelingcleaning = Menu(
    title='Labeling & Cleaning',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='Wafer label position',
            type='terms',
            search_quantity=f'data.wafer_label_position#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='Wafer label name',
            type='terms',
            search_quantity=f'data.wafer_label_name#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='Cleaning with DI ultrasound?',
            type='terms',
            search_quantity=f'data.{wc}_DI_ultrasound_required#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='RCA cleaning?',
            type='terms',
            search_quantity=f'data.{wc}_rca_required#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='Piranha cleaning?',
            type='terms',
            search_quantity=f'data.{wc}_piranha_required#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='Dip HF cleaning?',
            type='terms',
            search_quantity=f'data.{wc}_dipHF_required#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='Rinse spin dryer required?',
            type='terms',
            search_quantity=f'data.{wc}_rinse_spin_dryer_required#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir14"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir14"]}',
        ),
    ],
)
menutrans_sod = Menu(
    title='SOD',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir15"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir15"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir15"]}',
        ),
        MenuItemTerms(
            title='Dopant solution (short name)',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir15"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the solution',
            type='periodic_table',
            search_quantity=f'{dmec}#{dir_path["dir15"]}',
        ),
        MenuItemHistogram(
            title='Volume dispensed',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_dispensed_volume#{dir_path["dir15"]}',
                title='spin dispensed volume',
                unit='milliliter',
            ),
        ),
        MenuItemTerms(
            title='Dipping HF proportions',
            type='terms',
            search_quantity=f'data.dipping_HFsolution_proportions#{dir_path["dir15"]}',
        ),
        MenuItemHistogram(
            title='Dip HF duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_dipHF_duration#{dir_path["dir15"]}',
                title='dip HF duration',
                unit='sec',
            ),
        ),
        MenuItemTerms(
            title='Water rinse required?',
            type='terms',
            search_quantity=f'data.water_rinse_required#{dir_path["dir15"]}',
        ),
        MenuItemTerms(
            title='Spin dryer required?',
            type='terms',
            search_quantity=f'data.spin_dryer_required#{dir_path["dir15"]}',
        ),
        MenuItemHistogram(
            title='PEB duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.peb_duration#{dir_path["dir15"]}',
                title='peb duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='PEB temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.peb_temperature#{dir_path["dir15"]}',
                title='peb temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Spin duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_duration#{dir_path["dir15"]}',
                title='spin duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_frequency#{dir_path["dir15"]}',
                title='spin frequency',
                unit='revolutions_per_minute',
            ),
        ),
        MenuItemHistogram(
            title='Spin angular acceleration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_angular_acceleration#{dir_path["dir15"]}',
                title='angular acceleration',
                unit='rpm/sec',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir15"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir15"]}',
        ),
    ],
)
menutrans_track = Menu(
    title='Track',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='Resist name',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir16"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the resist',
            type='periodic_table',
            search_quantity=f'{rec}#{dir_path["dir16"]}',
        ),
        MenuItemHistogram(
            title='Resist thickness (target)',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir16"]}',
                title='resist thickness',
                unit='um',
            ),
        ),
        MenuItemHistogram(
            title='De-wetting duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dewetting_duration#{dir_path["dir16"]}',
                title='de-wetting duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='De-wetting temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dewetting_temperature#{dir_path["dir16"]}',
                title='de-wetting temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='HDMS',
            type='terms',
            search_quantity=f'data.hdms_required#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='Mask set name',
            type='terms',
            search_quantity=f'data.mask_set_name#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='Mask name',
            type='terms',
            search_quantity=f'data.mask_name#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='Mask aligner name',
            type='terms',
            search_quantity=f'data.mask_aligner_name#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='Alignment type',
            type='terms',
            search_quantity=f'data.alignment_type#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='Mask target',
            type='terms',
            search_quantity=f'data.mask_target#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='Exposure mask contact type',
            type='terms',
            search_quantity=f'data.exposure_mask_contact_type#{dir_path["dir16"]}',
        ),
        MenuItemHistogram(
            title='Exposure intensity',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.exposure_intensity#{dir_path["dir16"]}',
                title='exposure power density',
                unit='mwatt/cm^2',
            ),
        ),
        MenuItemHistogram(
            title='Exposure duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.exposure_duration#{dir_path["dir16"]}',
                title='exposure duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Developing duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.developing_duration#{dir_path["dir16"]}',
                title='developing duration',
                unit='sec',
            ),
        ),
        MenuItemTerms(
            title='Developing rinse spin dryer required?',
            type='terms',
            search_quantity=f'data.{dev}_rinse_spin_dryer_required#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='PEB required?',
            type='terms',
            search_quantity=f'data.peb_required#{dir_path["dir16"]}',
        ),
        MenuItemHistogram(
            title='PEB duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.peb_duration#{dir_path["dir16"]}',
                title='peb duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='PEB temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.peb_temperature#{dir_path["dir16"]}',
                title='peb temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Softbake required?',
            type='terms',
            search_quantity=f'data.softbake_required#{dir_path["dir16"]}',
        ),
        MenuItemHistogram(
            title='Softbake duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.softbake_duration#{dir_path["dir16"]}',
                title='softbake duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Softbake temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.softbake_temperature#{dir_path["dir16"]}',
                title='softbake temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Hardbake required?',
            type='terms',
            search_quantity=f'data.hardbake_required#{dir_path["dir16"]}',
        ),
        MenuItemHistogram(
            title='Hardbake duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.hardbake_duration#{dir_path["dir16"]}',
                title='hardbake duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Hardbake temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.hardbake_temperature#{dir_path["dir16"]}',
                title='hardbake temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir16"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir16"]}',
        ),
    ],
)
menuadd_electrongun = Menu(
    title='Electron Gun',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='Target material (short name)',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='Wafer stack name',
            type='terms',
            search_quantity=f'data.wafer_stack_name#{dir_path["dir17"]}',
        ),
        MenuItemHistogram(
            title='Deposition thickness (target)',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir17"]}',
                title='thickness target',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Deposition duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir17"]}',
                title='duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Deposition chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.chamber_pressure#{dir_path["dir17"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_frequency#{dir_path["dir17"]}',
                title='frequency',
                unit='rpm',
            ),
        ),
        MenuItemHistogram(
            title='Deposition thickness (measured)',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_measured#{dir_path["dir17"]}',
                title='thickness measured',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Gun voltage measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.gun_voltage_measured#{dir_path["dir17"]}',
                title='gun voltage',
                unit='V',
            ),
        ),
        MenuItemHistogram(
            title='Gun current measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.gun_current_measured#{dir_path["dir17"]}',
                title='gun current',
                unit='mampere',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir17"]}',
        ),
    ],
)
menuadd_sputtering = Menu(
    title='Sputtering',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir18"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'{mec}#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='Sample Movement',
            type='terms',
            search_quantity=f'data.sample_movement#{dir_path["dir18"]}',
        ),
        MenuItemHistogram(
            title='Movement frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.spin_frequency#{dir_path["dir18"]}',
                title='frequency',
                unit='rpm',
            ),
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir18"]}',
                title='thickness target',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Duration target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir18"]}',
                title='duration target',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.chuck_temperature#{dir_path["dir18"]}',
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.power#{dir_path["dir18"]}',
                title='power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Delay between stack layers',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.delay_between_stack_layers#{dir_path["dir18"]}',
                title='delay between stack layers',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Thickness obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_measured#{dir_path["dir18"]}',
                title='thickness obtained',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_measured#{dir_path["dir18"]}',
                title='duration measured',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_obtained#{dir_path["dir18"]}',
                title='deposition rate obtained',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir18"]}',
        ),
    ],
)
menuadd_sog = Menu(
    title='SOG',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='Substrate material',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir19"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the substrate',
            type='periodic_table',
            search_quantity=f'{sec}#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='Pre-cleaning method',
            type='terms',
            search_quantity=f'data.pre_cleaning#{dir_path["dir19"]}',
        ),
        MenuItemHistogram(
            title='Target thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir19"]}',
                title='thickness target',
                unit='um',
            ),
        ),
        MenuItemHistogram(
            title='De-wetting duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dewetting_duration#{dir_path["dir19"]}',
                title='de-wetting duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='De-wetting temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dewetting_temperature#{dir_path["dir19"]}',
                title='de-wetting temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Measured thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_measured#{dir_path["dir19"]}',
                title='thickness measured',
                unit='um',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir19"]}',
        ),
    ],
)
menuremove_rie = Menu(
    title='RIE',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir20"]}',
        ),
        MenuItemHistogram(
            title='Desired depth',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir20"]}',
                title='depth target',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Desired duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir20"]}',
                title='duration target',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Desired etching rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_target#{dir_path["dir20"]}',
                title='etching rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.etching_steps.recipe_name#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Material to be etched',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.name#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Formulas of the etched material',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.chemical_formula#{dir_path["dir20"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements etched',
            type='periodic_table',
            search_quantity=f'{meec}#{dir_path["dir20"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{fluxetch}#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.chemical_formula#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.name#{dir_path["dir20"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.fluximeters.massflow#{dir_path["dir20"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_temperature#{dir_path["dir20"]}',
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Wall temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.wall_temperature#{dir_path["dir20"]}',
                title='wall temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_pressure#{dir_path["dir20"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_power#{dir_path["dir20"]}',
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_frequency#{dir_path["dir20"]}',
                title='chuck frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=f'data.etching_steps.clamping#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Clamping type',
            type='terms',
            search_quantity=f'data.etching_steps.clamping_type#{dir_path["dir20"]}',
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.clamping_pressure#{dir_path["dir20"]}',
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir20"]}',
                title='duration measured',
                unit='sec',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir20"]}',
        ),
    ],
)
menuremove_wetetching = Menu(
    title='Wet Etching',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Material to be etched',
            type='terms',
            search_quantity=f'data.materials_etched.name#{dir_path["dir21"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the material',
            type='periodic_table',
            search_quantity=f'{meec}#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Etching solution',
            type='terms',
            search_quantity=f'data.etching_solution#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Etching solution proportions',
            type='terms',
            search_quantity=f'data.etching_solution_proportions#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Name of compounds used to etch',
            type='terms',
            search_quantity=f'data.reactives_used_to_etch.name#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Formula of the compounds used to etch',
            type='terms',
            search_quantity=f'data.{ru}.chemical_formula#{dir_path["dir21"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the etching compounds',
            type='periodic_table',
            search_quantity=f'{rute}#{dir_path["dir21"]}',
        ),
        MenuItemHistogram(
            title='Desired depth',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir21"]}',
                title='depth target',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Desired duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir21"]}',
                title='duration target',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Depth obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_measured#{dir_path["dir21"]}',
                title='depth measured',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_measured#{dir_path["dir21"]}',
                title='duration measured',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Etching rate obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_obtained#{dir_path["dir21"]}',
                title='etching rate obtained',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Etching type',
            type='terms',
            search_quantity=f'data.etching_type#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir21"]}',
        ),
    ],
)
menuremove_stripping = Menu(
    title='Stripping',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Stripping type',
            type='terms',
            search_quantity=f'data.stripping_type#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Material to remove',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir22"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the material',
            type='periodic_table',
            search_quantity=f'{mec}#{dir_path["dir22"]}',
        ),
        MenuItemHistogram(
            title='Target duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir22"]}',
                title='duration target',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Removing temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.removing_temperature#{dir_path["dir22"]}',
                title='removing temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Ultrasound required?',
            type='terms',
            search_quantity=f'data.ultrasound_required#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir22"]}',
        ),
    ],
)
menuutils_obsmeasurements = Menu(
    title='Observation Measurements',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Equipment used',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Activity type',
            type='terms',
            search_quantity=f'data.activity_type#{dir_path["dir23"]}',
        ),
        MenuItemHistogram(
            title='Target duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir23"]}',
                title='duration target',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Image name',
            type='terms',
            search_quantity=f'data.image_name#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Thickness measurements',
            type='terms',
            search_quantity=f'data.thickness_measurements#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Electrical measurements',
            type='terms',
            search_quantity=f'data.electrical_measurements#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir23"]}',
        ),
    ],
)
menuutils_startingmaterial = Menu(
    title='Starting Material',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='Wafer material (short name)',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir24"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements in the wafer',
            type='periodic_table',
            search_quantity=f'data.elemental_composition.element#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='Manufacturer name',
            type='terms',
            search_quantity=f'data.manufacturer_name#{dir_path["dir24"]}',
        ),
        MenuItemHistogram(
            title='Wafer quantity',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.wafer_quantity#{dir_path["dir24"]}',
                title='quantity',
            ),
        ),
        MenuItemHistogram(
            title='Wafer resistivity',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.wafer_resistivity#{dir_path["dir24"]}',
                title='wafer resistivity',
                unit='ohm*cm',
            ),
        ),
        MenuItemTerms(
            title='Wafer orientation',
            type='terms',
            search_quantity=f'data.wafer_orientation#{dir_path["dir24"]}',
        ),
        MenuItemHistogram(
            title='Wafer thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.wafer_thickness#{dir_path["dir24"]}',
                title='wafer thickness',
                unit='um',
            ),
        ),
        MenuItemTerms(
            title='Wafer surface finish',
            type='terms',
            search_quantity=f'data.wafer_surface_finish#{dir_path["dir24"]}',
        ),
        MenuItemHistogram(
            title='Wafer diameter',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.wafer_diameter#{dir_path["dir24"]}',
                title='wafer diameter',
                unit='mm',
            ),
        ),
        MenuItemTerms(
            title='Wafer doping',
            type='terms',
            search_quantity=f'data.wafer_doping#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir24"]}',
        ),
    ],
)
menutrans_baking = Menu(
    title='Baking',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir25"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir25"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir25"]}',
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.chuck_temperature#{dir_path["dir25"]}',
                title='chuck temperature',
                unit='K',
            ),
        ),
        MenuItemHistogram(
            title='Duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration#{dir_path["dir25"]}',
                title='duration',
                unit='sec',
            ),
        ),
    ],
)

menuremove_driebosch = Menu(
    title='DRIE BOSCH',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir26"]}',
        ),
        MenuItemHistogram(
            title='Desired depth',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir26"]}',
                title='depth',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir26"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Etching rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_target#{dir_path["dir26"]}',
                title='etching rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.etching_steps.tag#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Material to be etched',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.name#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Formulas of the etched material',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.chemical_formula#{dir_path["dir26"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements etched',
            type='periodic_table',
            search_quantity=f'{meec}#{dir_path["dir26"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{fluxetch}#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.chemical_formula#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.name#{dir_path["dir26"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.fluximeters.massflow#{dir_path["dir26"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_temperature#{dir_path["dir26"]}',
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Wall temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.wall_temperature#{dir_path["dir26"]}',
                title='wall temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Bias',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.bias#{dir_path["dir26"]}',
                title='bias',
                unit='V',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_pressure#{dir_path["dir26"]}',
                title='chamber_pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_power#{dir_path["dir26"]}',
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chuck_frequency#{dir_path["dir26"]}',
                title='chuck frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='ICP Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.icp_power#{dir_path["dir26"]}',
                title='icp power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='ICP Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.icp_frequency#{dir_path["dir26"]}',
                title='icp frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=f'data.etching_steps.clamping#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Clamping type',
            type='terms',
            search_quantity=f'data.etching_steps.clamping_type#{dir_path["dir26"]}',
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.clamping_pressure#{dir_path["dir26"]}',
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir26"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir26"]}',
        ),
    ],
)
