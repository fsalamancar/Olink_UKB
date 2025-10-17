import pandas as pd
import numpy as np
import re

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