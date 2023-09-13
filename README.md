# softalias-kg
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8341333.svg)](https://doi.org/10.5281/zenodo.8341333)


**Authors:** Hector López and Daniel Garijo


This repository contains the mappings, cleaning code and construct queries used for creating Softalias-KG. At the moment, the KG contains two main sources of software aliases:

- [The CZI software mention dataset (Dryad)](https://datadryad.org/stash/dataset/doi:10.5061/dryad.6wwpzgn2c): A large dataset of software mentions in the biomedical literature containing thousands of aliases. This dataset consists on two sets of files. On the one hand, a set of pickle files describe the software mention groups matched to each external platform (Pypi, CRAN, etc.), together with a file assigning an id to each software mention in a publication. On the other hand, a set of CSVs contain the metadata for each software entry on each external platform. The input data used for this project are the .pkl files from the 'disambiguated' folder, the .csv files from 'linked' and the .pkl files from 'intermediate_files'. The folder `czi_dataset/transformation_scripts` contains all the Python scripts used to  reading, cleaning, transforming and verifying the data (see the readme file for their execution). The results of the transformation in RDF are available in Zenodo (DOI: [https://doi.org/10.5281/zenodo.7988427](https://doi.org/10.5281/zenodo.7988427)). 
- [Wikidata](https://wikidata.org/): we have enriched Softalias-KG with over 8K software applications (free software, wd:Q341) and more than 3k alternative labels (skos:altLabel) from Wikidata. The folder `wikidata` contains the python script with the queries used to retrieve software aliases from Wikidata. The category `Software` is not used directly because it incorporates many undesired results (e.g., videogames)

The folder `vocab` contains a description of the vocabulary used to describe aliases. Namely, we have class "SoftwareAlias" and the "alias" property (designed to indicate that a SoftwareApplication has a certain alias)

## Requirements
The pipeline has been tested with python 3.9. The following libraries are required:

- pandas
- json
- pickle
- shutil
- numpy
- jaro (for Jaro-Winkler metric calculation)
- Sparqlwrapper (for Wikidata construct queries)
- morph_kgc

For CZI transformation details, please see the associated [README file](https://github.com/SoftwareUnderstanding/softalias-kg/tree/main/czi_dataset/transformation_scripts#readme).
