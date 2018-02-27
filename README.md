![Logo](isa-api_logo.png)

# mtblisa: MetaboLights-ISA slicer
Version: 0.9.5

## Short Description

A container the `mtbls` module of the 
[ISA-API](http://github.com/ISA-tools/isa-api) and similar features for 
selecting subsets of data files from ISA-Tab metadata, based on factor values.

## Description

The [ISA-API](http://github.com/ISA-tools/isa-api) is a Python 3 library that 
can create, manipulate, and convert ISA-formatted content. The 
MetaboLights-ISA slicer allows querying over factor information in 
[ISA-Tab](https://isa-specs.readthedocs.io/en/latest/isatab.html) 
metadata directly on studies in 
[MetaboLights](https://www.ebi.ac.uk/metabolights/) as well as other input 
ISA-Tab files.

## Key features

- Retrieve metadata from MetaboLights studies in the ISA-Tab and JSON formats
- Query MetaboLights and ISA-Tab studies for factors used.
- Query MetaboLights and ISA-Tab studies for factor values used for a given 
factor.
- Query MetaboLights and ISA-Tab studies to retrieve data file names filtered 
on factor and factor value.
- Query MetaboLights and ISA-Tab studies to retrieve a folder of data files 
filtered on factor and factor value, if the data files are included with the
input ISA-Tab.
- Query MetaboLights and ISA-Tab studies to retrieve a summary of variable 
values in the ISA tables.


## Functionality

- Data Management / Study Metadata Querying

## Approaches

- Metabolomics
- Isotopic Labelling Analysis
  
## Instrument Data Types
- MS
- NMR

## Tool Authors

- [ISA Team](http://isa-tools.org)

## Container Contributors

- [David Johnson](https://github.com/djcomlab) (University of Oxford)
- [Philippe Rocca-Serra](https://github.com/proccaserra) (University of Oxford)

## Website

- https://github.com/ISA-tools/isa-api


## Git Repository

- https://github.com/phnmnl/container-mtblisa.git

## Installation 

For local individual installation:

```bash
docker pull docker-registry.phenomenal-h2020.eu/phnmnl/mtblisa
```

## Usage Instructions

### For direct docker usage

Basic usage:
```bash
docker run $PWD:/data docker-registry.phenomenal-h2020.eu/phnmnl/mtblisa /data/isatab_files/

docker run docker-registry.phenomenal-h2020.eu/phnmnl/mtblisa <command>
```

## Publications

- Haug, K., Salek, R. M., Conesa, P., Hastings, J., de Matos, P., Rijnbeek, M., 
... & Maguire, E. (2012). MetaboLights - an open-access general-purpose 
repository for metabolomics studies and associated meta-data. Nucleic acids 
research, gks1004.
- Sansone, Susanna-Assunta, Rocca-Serra, Philippe, Gonzalez-Beltran, Alejandra, 
Johnson, David, &amp; ISA Community. (2016, October 28). ISA Model and 
Serialization Specifications 1.0. Zenodo. http://doi.org/10.5281/zenodo.163640
- Sansone, Susanna-Assunta, et al. (2012, January 27). Towards interoperable 
bioscience data. Nature Genetics 44, 121–126. http://doi.org/10.1038/ng.1054
