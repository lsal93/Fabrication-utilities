#######################################################################################
###################################### SYNTHESIS ######################################
#######################################################################################
#   Fabrication process step main category consisting in the placing of a substance   #
#    on a substrate. This might be individual atoms or the forming of a layer of a    #
#                                      substance                                      #
#######################################################################################


from nomad.config.models.plugins import SchemaPackageEntryPoint


class CVDsEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.add.synthesis.CVD import m_package

        return m_package


CVDs_entry_point = CVDsEntryPoint(
    name='CVDs steps definitions',
    description='Schema package for describing cvd steps in fabrication.',
)


class CoatingEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.add.synthesis.coating import m_package

        return m_package


coating_entry_point = CoatingEntryPoint(
    name='Coating steps definitions',
    description='Schema package for describing coating steps in fabrication.',
)
