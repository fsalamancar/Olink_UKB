# Covariate Selection for IBD Disease

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This project implements covariate selection methods for Inflammatory Bowel Disease (IBD) analysis using the UK Biobank dataset. It provides a comprehensive toolkit for identifying relevant covariates through machine learning techniques and statistical methods.

## Table of Contents

- [Covariate Selection for IBD Disease](#covariate-selection-for-ibd-disease)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [Dependencies](#dependencies)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)
  - [Contact](#contact)

## Overview

The **covariableSelection** tool is designed to facilitate the identification and selection of relevant covariates in IBD disease studies. By leveraging machine learning algorithms and statistical approaches, this toolkit helps researchers:

- Preprocess and transform UK Biobank datasets
- Select relevant features for IBD prediction
- Evaluate model performance with comprehensive metrics
- Visualize results and feature importance

## Project Structure

```
Olink_UKB/
├── README.md                           # Project documentation
├── covariableSelection.toml            # Project configuration and dependencies
├── .gitignore                          # Git ignore rules
│
├── covariableSelection/                # Main package directory
│   ├── data/                          # Data handling modules
│   │   ├── load.py                    # Data loading utilities
│   │   ├── preprocesing.py            # Data preprocessing functions
│   │   └── transform.py               # Data transformation utilities
│   │
│   ├── training/                      # Model training modules
│   │   └── splitData.py               # Train/test split utilities
│   │
│   ├── models/                        # Machine learning models (empty - to be implemented)
│   │
│   ├── evaluation/                    # Model evaluation modules
│   │   ├── metrics.py                 # Performance metrics
│   │   └── visualisate.py             # Visualization functions
│   │
│   └── utils/                         # Utility functions
│       └── renameColums.py            # Column renaming utilities
│
├── data/                              # Data storage directory
│   ├── raw/                           # Raw data files
│   ├── preprocessing/                 # Preprocessed data
│   └── outputs/                       # Generated outputs and results
│
├── notebooks/                         # Jupyter notebooks for analysis
│   └── ibd/                           # IBD-specific analyses
│       └── phenotype.ipynb            # Phenotype analysis notebook
│
└── test/                              # Unit tests (to be implemented)
```

## Installation

### Prerequisites

- Python 3.13 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/fsalamancar/Olink_UKB.git
cd Olink_UKB
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

Or manually install required packages:
```bash
pip install pandas>=2.0.3 numpy>=1.24.3 scikit-learn>=1.2.2 statsmodels>=0.14.0 matplotlib>=3.7.1 seaborn>=0.12.2
```

## Dependencies

The project relies on the following key libraries:

- **pandas** (>=2.0.3) - Data manipulation and analysis
- **numpy** (>=1.24.3) - Numerical computing
- **scikit-learn** (>=1.2.2) - Machine learning algorithms
- **statsmodels** (>=0.14.0) - Statistical models
- **matplotlib** (>=3.7.1) - Data visualization
- **seaborn** (>=0.12.2) - Statistical data visualization

See `covariableSelection.toml` for the complete list of dependencies.


## Authors

- **Angie G. Pineda** - [agpinedam@unal.edu.co](mailto:agpinedam@unal.edu.co)
- **Francisco J. Salamanca** - [fsalamancar@unal.edu.co](mailto:fsalamancar@unal.edu.co)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- UK Biobank for providing the dataset
- Universidad Nacional de Colombia
- All contributors and researchers involved in this project

## Contact

For questions, suggestions, or collaborations, please contact the authors via email or open an issue in the repository.

---

**Version:** 0.1.0  
**Last Updated:** October 2025
