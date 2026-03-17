import pandas as pd

def load_and_preprocess():
    data = pd.read_csv("data/train_delay_dataset.csv")

    X = data.drop("arrival_delay", axis=1)
    y = data["arrival_delay"]

    return X, y

if __name__ == "__main__":
    X, y = load_and_preprocess()
    print(X.head())