def transform(df):
    # BAD PRACTICES (AI should catch these)

    data = df.collect()  # ❌ bad (driver memory issue)

    result = []
    for row in data:
        if row["amount"] > 100:
            result.append(row)

    return result