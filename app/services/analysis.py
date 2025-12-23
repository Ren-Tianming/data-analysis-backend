import pandas as pd

def analyze_csv(file):
    df = pd.read_csv(file.file)

    result = {
        "rows": len(df),
        "columns": list(df.columns),
        "summary": df.describe().to_dict()
    }

    return result
