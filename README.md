![Logo](isa-api_logo.png)

# mtblisa: MetaboLights-ISA slicer
Version: 0.7.3

## Short Description

A container image definition for the mtbls module of the ISA API

## Description

The ISA API is a Python 3 library that can create, manipulate, and convert ISA formatted content. The mtbls.py module provides the functionality to access MetaboLights ISA-Tab data, wrapped up as the mtblisa container.

## Key features

- Retrieve metadata from MetaboLights studies in the ISA-Tab and JSON formats
- Query MetaboLights studies for factors used.
- Query MetaboLights studies for factor values used for a given factor.
- Query MetaboLights studies to retrieve data file names filtered on factor and factor value.

## Functionality

- Other Tools

## Approaches
  
## Instrument Data Types

## Tool Authors

- [ISA Team](http://isa-tools.org)

## Container Contributors

- [David Johnson](https://github.com/djcomlab) (University of Oxford)

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

For direct docker usage:

```bash
docker run docker-registry.phenomenal-h2020.eu/phnmnl/mtblisa ...
```

## Publications

- Haug, K., Salek, R. M., Conesa, P., Hastings, J., de Matos, P., Rijnbeek, M., ... & Maguire, E. (2012). MetaboLights—an open-access general-purpose repository for metabolomics studies and associated meta-data. Nucleic acids research, gks1004.

- Sansone, Susanna-Assunta, Rocca-Serra, Philippe, Gonzalez-Beltran, Alejandra, Johnson, David, & ISA Community. (2016, October 28). ISA Model and Serialization Specifications 1.0. Zenodo. http://doi.org/10.5281/zenodo.163640
