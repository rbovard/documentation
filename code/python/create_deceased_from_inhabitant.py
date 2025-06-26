from qgis.utils import iface
from qgis.core import QgsFeature, QgsExpression, QgsExpressionContext, QgsExpressionContextUtils

source_layer_id = "[% @layer_id %]"
destination_layer_id = "od_defunts_6f4e6b50_49c4_46d6_b1f6_a1d340cf2619"

source_layer = QgsProject.instance().mapLayer(source_layer_id)
destination_layer = QgsProject.instance().mapLayer(destination_layer_id)

feature = source_layer.getFeature([% $id %])

if not destination_layer.isEditable():
    destination_layer.startEditing()

new_feature = QgsFeature(destination_layer.fields())

# Manually set gid because QGIS client-side default value evaluation doesn't trigger PostGIS sequence
expr = QgsExpression('maximum("gid")')
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(destination_layer))
max_gid = expr.evaluate(context)
max_gid = int(max_gid) if max_gid is not None else 0

new_feature.setAttribute("gid", max_gid + 1)

fields_to_copy = ["nom", "suffixe_nom", "prenom", "sexe", "lieu_origine", "etat_civil", "date_naissance", "lieu_naissance"]

for field in fields_to_copy:
    if field in feature.fields().names():
        new_feature.setAttribute(field, feature[field])

destination_layer.addFeature(new_feature)
destination_layer.commitChanges()

iface.messageBar().pushSuccess("Défunt créé", "Un défunt a été créé à partir de cet habitant.")
