import pandas as pd
import json

# Leer el archivo CSV
df = pd.read_csv('bioconductor-FINAL.csv', delimiter=',')

# Leer el archivo JSON
with open('filtered_data.json') as f:
    data_json = json.load(f)

# Comprobar coincidencias del CSV en el JSON
csv_groups = set(df['ID'])
missing_csv_groups = []
for group_id in csv_groups:
    if not any(group['id'] == group_id for group in data_json):
        missing_csv_groups.append(group_id)

# Comprobar coincidencias del JSON en el CSV (solo para grupos con source "scicrunch")
json_groups = [group for group in data_json if group.get('source') == "bioconductor"]
json_group_ids = set(group['id'] for group in json_groups)
missing_json_groups = []
for group_id in json_group_ids:
    if group_id not in csv_groups:
        missing_json_groups.append(group_id)

# Escribir resultados en el archivo de texto
with open('comprobacion.txt', 'w') as f:
    if len(missing_csv_groups) == 0 and len(missing_json_groups) == 0:
        f.write('Todo OK. Todos los grupos coinciden entre el CSV y el JSON.\n')
    else:
        if len(missing_csv_groups) > 0:
            f.write('Los siguientes grupos del CSV no coinciden en el JSON:\n')
            for group_id in missing_csv_groups:
                f.write(f'Grupo {group_id}\n')

        if len(missing_json_groups) > 0:
            f.write('Los siguientes grupos del JSON no coinciden en el CSV:\n')
            for group_id in missing_json_groups:
                f.write(f'Grupo {group_id}\n')