import os
from covariableSelection.data.load import load_tsv
from covariableSelection.data.preprocesing import select_first_cohort

# Ruta del archivo actual (scripts/ibd/phenotype.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Subir tres niveles: scripts/ibd → covariableSelection → Olink_UKB
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../../../"))

input_path = os.path.join(PROJECT_ROOT, "data/raw/phenotype/")
output_path = os.path.join(PROJECT_ROOT, "data/processed/phenotype/")


def preprocess_phenotype_data():

    phenotype_df = load_tsv(input_path, "phenotype_data.tsv")
    print("Raw data", phenotype_df.shape)

    phenotype_df = select_first_cohort(phenotype_df)
    print("First cohort selected", phenotype_df.shape)

    return phenotype_df


def main():
    os.makedirs(output_path, exist_ok=True)
    phenotype_df = preprocess_phenotype_data()
    print("Processed phenotype data", phenotype_df.shape)

if __name__ == "__main__":
    main()
    
