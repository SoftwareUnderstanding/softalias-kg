# Description
Author: Hector Lopez Valero

This project contains a set of Python scripts designed to manipulate and transform data for format unification and error correction. The initial data is provided in pkl format and is intended to be converted to a more manageable json format.

A detailed description of the purpose of each script along with the recommended order of execution is provided below.

# Order of execution

- scriptPkl.py: This script converts pkl format files to json. Its function is to open the pkl file, load the data and dump it into a json file.
- scriptJsonFormat.py: This script is responsible for transforming and organizing the data contained in several source json files (extracted from different locations). It applies the trust calculation between group and alias names and adds the number of repetitions and other relevant information.
- scriptJsonFormatWithoutNull.py: Similar to scriptJsonFormat.py, but with an additional check to make sure the keys and values are not None before adding them to the final json.
- scriptJsonFormatWithoutNullWithoutVoid.py: Similar to scriptJsonFormatWithoutNull.py, but with an additional check to make sure the alias is not empty before adding it to the final json.
- scriptDeleteDuplicatedAlias.py: This script is used to remove duplicate aliases within the same group in json files. It checks the alias ids and ensures that there are no duplicates.
- scriptJsonUpdateFormat.py: This script performs a number of formatting and cleanup operations on json files, such as replacing the value of certain fields, removing unnecessary fields, and removing trusted values.
- scriptCheck.py: This script is used to check the consistency between data in CSV and JSON files. It identifies discrepancies and records them in a text file for later review.

Please follow the order provided to ensure correct data manipulation and transformation.

# Requirements
These scripts require Python 3.7 or higher and the following Python libraries:

- pandas
- json
- pickle
- shutil
- numpy
- jaro (for Jaro-Winkler metric calculation)

Please make sure you have them installed before running the scripts.

# Usage
To run each script, use the following command in your terminal:

"python <scriptname.py>"

Be sure to replace <scriptname.py> with the actual name of the script.


