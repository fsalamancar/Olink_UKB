import re

def rename_columns_with_field_names(df, touchscreen_chars_df, exclude_cols=['eid', 'Disease']):
    touchscreen_chars_df = touchscreen_chars_df.dropna(subset=['FieldID', 'Field']).copy()
    touchscreen_chars_df['FieldID'] = touchscreen_chars_df['FieldID'].astype(int)
    touchscreen_chars_df['Field'] = touchscreen_chars_df['Field'].str.strip()

    fieldid_to_name = dict(zip(touchscreen_chars_df['FieldID'], touchscreen_chars_df['Field']))

    rename_dict = {}
    for col in df.columns:
        if col in exclude_cols:
            continue

        match = re.match(r'f_(\d+)_\d+_\d+', col)
        if match:
            fieldid = int(match.group(1))
            new_name = fieldid_to_name.get(fieldid)
            if new_name:
                rename_dict[col] = new_name
            else:
                print(f"FieldID {fieldid} encontrado en columna '{col}' no está en touchscreen_chars_df")
        else:
            print(f"No coincide con patrón: {col}")

    return df.rename(columns=rename_dict)