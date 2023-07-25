import json

# Leer el archivo JSON
with open('new_file.json') as f:
    data_json = json.load(f)

# Crear un nuevo JSON
new_data_json = []

# Recorrer cada grupo en el JSON
for group in data_json:
    # Reemplazar el campo 'source' si es 'extra-scricrunch'
    if 'source' in group and group['source'] == 'extra-scicrunch':
        group['source'] = 'scicrunch'

    # Eliminar el campo 'url'
    if 'url' in group:
        del group['url']

    if 'alias' in group:
        # Crear un conjunto para almacenar id_alias
        alias_ids = set()
        new_alias = []

        # Recorrer cada alias
        for alias in group['alias']:
            # Verificar si el id_alias ya existe
            if alias['id_alias'] not in alias_ids:
                # Agregar el id_alias al conjunto
                alias_ids.add(alias['id_alias'])
                # Modificar el id_group del alias
                alias['id_group'] = group['id']
                # Eliminar el campo 'confidence'
                if 'confidence' in alias:
                    del alias['confidence']
                # Agregar el alias a la nueva lista
                new_alias.append(alias)

        # Reemplazar el campo alias por la nueva lista sin duplicados
        group['alias'] = new_alias

    new_data_json.append(group)

# Guardar el nuevo JSON
with open('dataFinalFormat.json', 'w') as f:
    json.dump(new_data_json, f, indent=4)
