import pandas as pd

def engineer_features(df):
    df = df.sort_values(by=["user_id", "timestamp"])
    df["label"] = (df["pnl"] > 0).astype(int)
    df["action"] = df["action"].map({"buy": 1, "sell": 0})
    df["hour"] = df["timestamp"].dt.hour
    df["dayofweek"] = df["timestamp"].dt.dayofweek

    df = pd.get_dummies(df, columns=["asset"])

    df["rolling_avg_pnl_5"] = df.groupby("user_id")["pnl"].transform(lambda x: x.shift(1).rolling(5).mean())
    df["rolling_success_rate_5"] = df.groupby("user_id")["label"].transform(lambda x: x.shift(1).rolling(5).mean())

    return df.dropna()