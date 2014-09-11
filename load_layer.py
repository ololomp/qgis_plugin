# Documentation de reference: http://qgis.org/api/2.4


def tell_editable(l):
    if l.isEditable():
        print("MODIFIABLE")
    else:
        print("VEROUILLEE")

print(QgsProviderRegistry.instance().providerList()) # liste les librairie permettant l'ouverture de donnees.

if QgsMapLayerRegistry.instance().count() != 0:
   QgsMapLayerRegistry.instance().removeAllMapLayers()
   

vlayer = QgsVectorLayer("/home/nviel/tmp/TEST_QGIS/moncode/D90.shp", "nico_layer", "ogr")
if not vlayer.isValid():
  print("Layer failed to load!")

QgsMapLayerRegistry.instance().addMapLayer(vlayer) # Ajout a la visu.

tell_editable(vlayer)
vlayer.startEditing()
tell_editable(vlayer)

vlayer.selectAll()

print(vlayer.selectedFeatureCount())
flist = vlayer.selectedFeatures()
print(len(flist))

for dalle in flist[:10]:
    # print(dalle.fields()[0].name())  # field ne concerne que la definition du champs
    print(dalle.attributes()[0])       # attribute c'est la valeur