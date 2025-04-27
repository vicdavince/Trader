import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_fake_trading_data(num_users=10, trades_per_user=100):
    data = []

    for user_id in range(1, num_users + 1):
        current_time = datetime(2023, 1, 1)
        for _ in range(trades_per_user):
            action = random.choice(["buy", "sell"])
            asset = random.choice(["AAPL", "TSLA", "GOOG", "AMZN"])
            volume = random.randint(1, 100)
            price = round(random.uniform(50, 2000), 2)
            pnl = round(np.random.normal(loc=10, scale=50), 2)  # +/- random profit
            timestamp = current_time
            current_time += timedelta(minutes=random.randint(10, 240))

            data.append([f"user_{user_id}", timestamp, action, asset, volume, price, pnl])

    df = pd.DataFrame(data, columns=["user_id", "timestamp", "action", "asset", "volume", "price", "pnl"])
    df.to_csv("trading_ai/data/trades.csv", index=False)
    return df
