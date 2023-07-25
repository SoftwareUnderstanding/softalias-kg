import pickle
import json
import shutil
import numpy as np

def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()

pathName = 'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/Intermediate_files/intermediate_files/mention2ID.pkl'
rawName = pathName.split("/").pop()

jsonName = rawName.split(".")[0] + '.json'

# abrir archivo .pkl
fileSrc = open(pathName, 'rb')

# dump la informacion en un file
data = pickle.load(fileSrc)

# Creacion del json mediante el dict de los datos obtenidos del pkl
#jsonData = json.dumps(data, default=np_encoder)

with open(jsonName, "w") as outfile:
    json.dump(data, outfile, indent=4, default=np_encoder)

# Reorganizacion del archivo
newPath = 'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/IntermediateFileJSON/'+ jsonName
shutil.move(jsonName, newPath)
