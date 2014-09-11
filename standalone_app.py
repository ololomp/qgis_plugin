from qgis.core import *

# supply path to where is your qgis installed
QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

# load providers
QgsApplication.initQgis()
print(QgsProviderRegistry.instance().providerList())


vlayer = QgsVectorLayer("/home/nviel/tmp/TEST_QGIS/moncode/D90.shp", "nico_layer", "ogr")

if not vlayer.isValid():
  print "Layer failed to load!"
  
print("fini")