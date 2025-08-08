from nomad.config.models.plugins import AppEntryPoint

from fabrication_facilities.apps.equipmentapp import equipmentapp
from fabrication_facilities.apps.processapp import processapp
from fabrication_facilities.apps.stepapp import stepapp
from fabrication_facilities.apps.removeapp import removeapp
from fabrication_facilities.apps.addapp import addapp

equipment_app_entry_point = AppEntryPoint(
    name='Fabrication_equipment_search',
    description='New app for equipment of fabrication facilities.',
    app=equipmentapp,
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
    app=addapp
)

app_entry_point = step_app_entry_point
