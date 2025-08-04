from nomad.config.models.plugins import SchemaPackageEntryPoint


class ItemsEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.Items import m_package

        return m_package


Items_entry_point = ItemsEntryPoint(
    name='FabricationItems',
    description='Schema package for describing items in fabrications.',
)


class UtilitiesEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.fabrication_utilities import (
            m_package,
        )

        return m_package


Utilities_entry_point = UtilitiesEntryPoint(
    name='FabricationBaseExtension',
    description='Schema package for describing base classes and steps in fabrication.',
)


class AddEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.steps.add import m_package

        return m_package


Add_entry_point = AddEntryPoint(
    name='Add processes',
    description='Schema package for describing add steps in fabrications.',
)


class TransformEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.steps.transform import m_package

        return m_package


Transform_entry_point = TransformEntryPoint(
    name='Transoform processes',
    description='Schema package for describing transform steps in fabrications.',
)


class RemoveEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.steps.remove import m_package

        return m_package


Remove_entry_point = RemoveEntryPoint(
    name='Add processes',
    description='Schema package for describing add steps in fabrications.',
)


class EquipmentsEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.equipments.equipments import (
            m_package,
        )

        return m_package


Equipments_entry_point = EquipmentsEntryPoint(
    name='FabricationEquipments',
    description='Schema package for describing various equipments for fabrication.',
)


class MaterialEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.materials import (
            m_package,
        )

        return m_package


materials_entry_point = MaterialEntryPoint(
    name='Fabrication Materials',
    description='Schema package for describing various raw materials properties.',
)


class AnalysisEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.calculus.calculus import (
            m_package,
        )

        return m_package


calculus_entry_point = AnalysisEntryPoint(
    name='Analysis sheets',
    description='Schema package for describing various analysis needed in CR.',
)
