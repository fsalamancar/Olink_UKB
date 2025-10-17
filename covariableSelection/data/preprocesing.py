import pandas as pd
import numpy as np
import re

def select_first_cohort(df):
    """
    Select only columns from the first cohort (cohort 0).
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame with UK Biobank format columns
    
    Returns
    -------
    pd.DataFrame
        DataFrame with only eid column (if present) and first cohort data
    """
    pattern = re.compile(r'f_(\d+)_(\d+)_(\d+)')
    cols_to_keep = []
    
    # Only include 'eid' if it exists in the DataFrame
    if 'eid' in df.columns:
        cols_to_keep.append('eid')
    
    for col in df.columns:
        match = pattern.match(col)
        if match:
            field_id, cohort, instance = match.groups()
            if cohort == '0':
                cols_to_keep.append(col)
    
    return df[cols_to_keep]

def na_elimination(dataframe , percentage=0.5):

    threshold = percentage * len(dataframe)
    dataframe = dataframe.dropna(thresh=threshold, axis=1)
    return dataframe

def impute_by_mode_disease(df):
    df = df.copy()
    for col in df.columns:
        if col not in ['eid', 'Disease']:
            modas = df.groupby('Disease')[col].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
            df[col] = df.apply(
                lambda row: modas[row['Disease']] if pd.isna(row[col]) else row[col], axis=1
            )
    return df

def eliminate_fields_by_fieldID (irrelevant_ids, df) :
    pattern = re.compile(rf"^f_({'|'.join(irrelevant_ids)})_\d+_\d+$")
    columns_to_drop = [col for col in df.columns if pattern.match(col)]
    return df.drop(columns=columns_to_drop)