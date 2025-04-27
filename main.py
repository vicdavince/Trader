from simulate_data import generate_fake_trading_data
from features_engineering import engineer_features
from train_model import train_model

def main():
    print("🔄 Generating fake trading data...")
    df = generate_fake_trading_data()

    print("🧠 Engineering features...")
    df = engineer_features(df)

    print("📈 Training model...")
    train_model(df)

if __name__ == "__main__":
    main()