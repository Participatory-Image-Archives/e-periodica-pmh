# e-periodica OAI-PMH - Ethnology and Folklore
This script was done to download the metadata of [e-periodica](https://www.e-periodica.ch/) through their OAI-PMH endpoint (`https://www.e-periodica.ch/oai`) that could be interesting to the PIA research project as we want to link our image-based collections to the e-periodica articles. 

There are more than 16k metadata articles which have the 390 `setSpec` (Ethnology, folklore) on e-periodica. Probably, the more relevant articles come from the `Korrespondenzblättern der SGV` (more than 2k articles), divided into these three sources: 

- https://www.e-periodica.ch/digbib/volumes?UID=sgv-001 
- https://www.e-periodica.ch/digbib/volumes?UID=sgv-002
- https://www.e-periodica.ch/digbib/volumes?UID=sgv-003 

## Records in CSV
- [All records](data/records.csv)
- [Extract (SGV)](data/sgv.csv)

## Acknowledgements
It was done thanks to the help of the ETH Library and following the instructions of the [Bern University Library's Python Digital Toolbox](https://github.com/ub-unibe-ch/ds-pytools). 

# How to cite
Raemy, J. A. (2023). e-periodica OAI-PMH - Ethnology and Folklore (Version 1.0.0) [Computer software]. https://doi.org/10.5281/zenodo.7777797
[![DOI](https://zenodo.org/badge/620255649.svg)](https://zenodo.org/badge/latestdoi/620255649)
