import pandas as pd
import numpy as np

def detect_column_types(df, threshold=20):
    column_types = {}
    for col in df.columns:
        series = df[col].dropna()

        if pd.api.types.is_numeric_dtype(series):
            if series.nunique() < threshold:
                column_types[col] = 'categorical (numeric codes)'
            else:
                column_types[col] = 'numerical'

        elif pd.api.types.is_object_dtype(series):
            if series.nunique() < threshold:
                column_types[col] = 'categorical (string labels)'
            else:
                column_types[col] = 'text'
        else:
            column_types[col] = 'unknown'
    return column_types

# Example usage:
if __name__ == "__main__":
    data = {
        'Age': [20, 21, 19, 20, 22],
        'ZipCode': [12345, 12345, 67890, 67890, 12345],
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
        'Feedback': ['Good service', 'Bad', 'Excellent', 'Average', 'Good service']
    }
    df = pd.DataFrame(data)
    print("\nInput DataFrame:")
    print(df)
    print("\nDetected Column Types:")
    print(detect_column_types(df))