import joblib
import pandas as pd

def load_model():
    return joblib.load("trading_ai/model/trade_model.pkl")

def predict_trade(model, trade_row_df: pd.DataFrame):
    return model.predict(trade_row_df)[0]