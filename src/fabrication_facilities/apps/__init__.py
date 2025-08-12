from nomad.config.models.plugins import AppEntryPoint

from fabrication_facilities.apps.addapp import addapp
from fabrication_facilities.apps.charact_equipmentapp import charact_equipmentapp
from fabrication_facilities.apps.characterapp import characterapp
from fabrication_facilities.apps.equipmentapp import equipmentapp
from fabrication_facilities.apps.processapp import processapp
from fabrication_facilities.apps.removeapp import removeapp
from fabrication_facilities.apps.stepapp import stepapp
from fabrication_facilities.apps.transapp import transapp

equipment_app_entry_point = AppEntryPoint(
    name='Fabrication_equipment_search',
    description='New app for equipment of fabrication facilities.',
    app=equipmentapp,
)

charact_equipment_app_entry_point = AppEntryPoint(
    name='Characterization_equipment_search',
    description='New app for equipment of characterization facilities.',
    app=charact_equipmentapp,
)

process_app_entry_point = AppEntryPoint(
    name='Fabrication_process_search',
    description='New app for equipment of fabrication facilities.',
    app=processapp,
)

step_app_entry_point = AppEntryPoint(
    name='Fabrication_process_search',
    description='New app for equipment of fabrication facilities.',
    app=stepapp,
)

app_remove_entry_point = AppEntryPoint(
    name='Remove steps research app',
    description='App for searching remove steps like etching, drying, etc.',
    app=removeapp,
)

app_add_entry_point = AppEntryPoint(
    name='Add steps research app',
    description='App for researching add steps like synthesis, bonding, etc.',
    app=addapp,
)

app_trans_entry_point = AppEntryPoint(
    name='Transform steps research app',
    description='App for searching transform steps like lithography, oxydation, etc.',
    app=transapp,
)

app_character_entry_point = AppEntryPoint(
    name='Character steps research app',
    description='App for researching characterization steps.',
    app=characterapp,
)

app_entry_point = app_trans_entry_point
