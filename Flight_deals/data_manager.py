import pandas as pd


def get_data():
    df = pd.read_csv(r"Flight Deals - prices.csv")
    return df


def save_data(data):
    df = pd.DataFrame(data, columns=['Price', 'Departure', 'Arrival'])
    df.to_csv("flights.csv")
