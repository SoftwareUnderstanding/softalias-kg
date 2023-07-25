import json
import shutil
import jaro

pathList = [
    'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/bioconductor_synonyms.json',
    'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/cran_synonyms.json',
    'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/extra-scicrunch_synonyms.json',
    'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/pypi_synonyms.json',
    'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/scicrunch_synonyms.json'
]

rawNumReps = 'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/IntermediateFileJSON/freq_dict.json'
rawSM = 'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/IntermediateFileJSON/mention2ID.json'
# rawSimilarity = 'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/resouces/RawJsonFiles/string_similarity_synonyms.json'

# Abrir archivo JSON del numero de menciones y de SM
with open(rawNumReps) as fileSrc:
      jsonNumReps = json.loads(fileSrc.read())
with open(rawSM) as fileSrc:
      jsonSM = json.loads(fileSrc.read())

# with open(rawSimilarity) as fileSrc:
#      jsonSimilarity = json.loads(fileSrc.read())


final = []
end = []

for pathName in pathList:
    # Obtenemos el SOURCE mediante el nombre del archivo, split del / para obtener el ultimo y luego split del _
    rawName = pathName.split("/").pop()
    source = rawName.split("_")[0]

    # Parametro de Url de la herramienta
    # TODO: saber si queremos guardar mas de una URL
    url = ""

    # Nombre del JSON resultado
    jsonName = 'JSONFinal.json'

    # Abrir archivo JSON usando el path
    with open(pathName) as fileSrc:
      jsonData= json.loads(fileSrc.read())

    # Guardamos en listas las key y values del dict obtenido del pkl
    listValues = list(jsonData.values())
    listKeys = list(jsonData.keys())

    # Recorremos las listas para ir añaidiendo los valores a las variables Alias y Final
    idx = -1
    for k in listKeys:
        idx += 1
        alias = []

        for v in listValues[idx]:
            alias.append({
                "name": v,
                "type": 'alias',
                "id_group": jsonSM.get(k),
                "id_alias": jsonSM.get(v),
                "confidence": jaro.jaro_winkler_metric(v, k),
                "number_of_repetitions": jsonNumReps.get(v) if (jsonNumReps.get(v)!= None) else 0
            })

        final.append({
            "name": k,
            "type": 'group',
            "id": jsonSM.get(k),
            "alias": alias,
            "source": source,
            "url": url
        })

end.append({
    "tools": final
})

# Escribimos los datos de la variable Final (contiene todos los datos procesados) en un .json
with open(jsonName, "w") as outfile:
    json.dump(end, outfile, indent=4)

# Reubicamos el archivo
newPath = 'C:/Users/hecto/OneDrive/Escritorio/TFG/WorkspaceTest/src/ArchivosProcesados/'+ jsonName
shutil.move(jsonName, newPath)