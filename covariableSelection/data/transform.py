from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

def scale_numeric_columns(df, id_col='eid'):
    """
    Standardize numeric columns of the DataFrame (mean=0, std=1), excluding the id_col column.

    Parameters:
        df (pd.DataFrame): DataFrame with the data.
        id_col (str): Identifier column (not scaled).

    Returns:
        pd.DataFrame: DataFrame with scaled numeric columns and id_col unchanged.
    """
    df = df.copy()

    if id_col not in df.columns:
        raise ValueError(f"The column '{id_col}' is not in the DataFrame.")

    id_series = df[[id_col]].astype(str)
    numeric_df = df.drop(columns=[id_col]).select_dtypes(include=[np.number])

    scaler = StandardScaler()
    scaled_array = scaler.fit_transform(numeric_df)
    scaled_df = pd.DataFrame(scaled_array, columns=numeric_df.columns, index=numeric_df.index)

    return pd.concat([id_series, scaled_df], axis=1)

def normalize_numeric_columns(df, id_col='eid'):
    """
    Normalize numeric columns of the DataFrame to the [0, 1] range, excluding the id_col column.

    Parameters:
        df (pd.DataFrame): DataFrame with the data.
        id_col (str): Identifier column (not normalized).

    Returns:
        pd.DataFrame: DataFrame with normalized numeric columns and id_col unchanged.
    """
    df = df.copy()

    if id_col not in df.columns:
        raise ValueError(f"The column '{id_col}' is not in the DataFrame.")

    id_series = df[[id_col]].astype(str)
    numeric_df = df.drop(columns=[id_col]).select_dtypes(include=[np.number])

    scaler = MinMaxScaler()
    normalized_array = scaler.fit_transform(numeric_df)
    normalized_df = pd.DataFrame(normalized_array, columns=numeric_df.columns, index=numeric_df.index)

    return pd.concat([id_series, normalized_df], axis=1)