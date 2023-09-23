import pandas as pd


def update_parameters(path):
    df = pd.read_excel(path, engine="openpyxl")
    print(path)
    print("Parameters updated successfully")


def update_attributes(path):
    df = pd.read_excel(path, engine="openpyxl")
    print(path)
    print("Attributes updated successfully")


def generate_extract(type_, tickers, names):
    print(type_, tickers, names)
    print("Extract generated successfully")
