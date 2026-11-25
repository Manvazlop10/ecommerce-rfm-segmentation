"""Download the UCI Online Retail dataset and save it as data/online_retail.csv.

Source: https://archive.ics.uci.edu/dataset/352/online+retail (CC BY 4.0).
Usage: python scripts/download_data.py
"""
import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
TARGET = Path(__file__).resolve().parents[1] / "data" / "online_retail.csv"


def main() -> None:
    TARGET.parent.mkdir(exist_ok=True)
    print(f"Downloading {URL} ...")
    with urllib.request.urlopen(URL) as response:
        archive = zipfile.ZipFile(io.BytesIO(response.read()))
    with archive.open("Online Retail.xlsx") as workbook:
        df = pd.read_excel(workbook, dtype={"InvoiceNo": str, "StockCode": str})
    df.to_csv(TARGET, index=False)
    print(f"Saved {len(df):,} rows to {TARGET}")


if __name__ == "__main__":
    main()
