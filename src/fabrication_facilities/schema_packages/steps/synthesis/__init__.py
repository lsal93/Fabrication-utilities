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
        from CVD import m_package

        return m_package


CVDs_entry_point = CVDsEntryPoint(
    name='CVDs steps definitions',
    description='Schema package for describing cvd steps in fabrication.'
)