import logging
import os
import re
import numpy as np
import pandas as pd
from covariableSelection.utils.logger import setup_logger

# Set to DEBUG if you want to see .head() and more details
logger = setup_logger("phenotype", level=logging.INFO)

# Compile the regex once for better performance
_RE_FIELD = re.compile(r"^f_(\d+)_(\d+)_(\d+)$")


def select_first_cohort(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns only 'eid' (if present) and columns from cohort 0 (f_<field>_0_<instance>).
    """
    cols_to_keep = ['eid'] if 'eid' in df.columns else []
    for col in df.columns:
        m = _RE_FIELD.match(col)
        if m and m.group(2) == '0':  # cohort == '0'
            cols_to_keep.append(col)

    before_shape = df.shape
    df_sel = df.loc[:, cols_to_keep]

    logger.info("select_first_cohort: selected columns: %d (includes 'eid': %s)",
                len(cols_to_keep), 'eid' in cols_to_keep)
    logger.info("select_first_cohort: shape before %s → after %s",
                before_shape, df_sel.shape)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("First rows after selection:\n%s",
                     df_sel.head().to_string(index=False))

    return df_sel


def eliminate_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicated columns by name.
    """
    n_before = df.shape[1]
    df2 = df.loc[:, ~df.columns.duplicated()]
    n_after = df2.shape[1]
    removed = n_before - n_after

    if removed > 0:
        logger.info("eliminate_duplicates: %d duplicated columns removed (from %d to %d).",
                    removed, n_before, n_after)
    else:
        logger.info("eliminate_duplicates: no duplicated columns found.")

    return df2


def na_elimination(df: pd.DataFrame, percentage: float = 0.5) -> pd.DataFrame:
    """
    Removes columns with less than `percentage` of non-null values.
    """
    threshold = int(percentage * len(df))
    n_before = df.shape[1]
    df2 = df.dropna(thresh=threshold, axis=1)
    n_after = df2.shape[1]

    logger.info("na_elimination: non-null row threshold=%d; columns %d → %d (removed %d).",
                threshold, n_before, n_after, n_before - n_after)
    return df2


def impute_by_mode_disease(df: pd.DataFrame) -> pd.DataFrame:
    """
    Imputes NA values by mode within 'Disease' group for all columns except ['eid','Disease'].
    Note: uses a loop per column; clear and fast enough for medium-sized data.
    """
    if 'Disease' not in df.columns:
        logger.warning("impute_by_mode_disease: 'Disease' column not found; no imputation performed.")
        return df

    df2 = df.copy()
    target_cols = [c for c in df2.columns if c not in ['eid', 'Disease']]
    imput_count = 0

    for col in target_cols:
        # Mode by group (if no mode, leaves NaN)
        modes = df2.groupby('Disease')[col].agg(
            lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan
        )
        # Only impute where there is NA
        na_mask = df2[col].isna()
        if na_mask.any():
            df2.loc[na_mask, col] = df2.loc[na_mask, 'Disease'].map(modes)
            imput_count += na_mask.sum()

    logger.info("impute_by_mode_disease: processed columns=%d; imputed values=%d.",
                len(target_cols), imput_count)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Sample after imputation:\n%s", df2.head().to_string(index=False))

    return df2


def eliminate_fields_by_fieldID(irrelevant_ids, df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes columns that belong to certain UKB field IDs (list of strings/ints).
    Matches pattern f_<fieldID>_<cohort>_<instance>.
    """
    irrelevant_ids = [str(x) for x in irrelevant_ids]
    if not irrelevant_ids:
        logger.info("eliminate_fields_by_fieldID: irrelevant ID list is empty; nothing removed.")
        return df

    # Escape IDs in case they contain metacharacters
    ids_pat = "|".join(re.escape(x) for x in irrelevant_ids)
    pat = re.compile(rf"^f_({ids_pat})_\d+_\d+$")

    to_drop = [c for c in df.columns if pat.match(c)]
    if to_drop:
        logger.info("eliminate_fields_by_fieldID: %d columns will be removed due to irrelevant IDs.",
                    len(to_drop))
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("Removed columns: %s", to_drop)
        return df.drop(columns=to_drop)
    else:
        logger.info("eliminate_fields_by_fieldID: no columns found to remove.")
        return df