# Data

This project uses the **Online Retail** dataset from the UCI Machine Learning Repository:

- Page: https://archive.ics.uci.edu/dataset/352/online+retail
- Citation: Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33
- License: CC BY 4.0
- 541,909 transactions from a UK-based online retailer, 01 Dec 2010 to 09 Dec 2011

The raw file (about 45 MB as CSV) is not committed. Get it with:

```bash
python scripts/download_data.py
```

This writes `data/online_retail.csv`. The notebook also downloads it automatically on first run if the file is missing.
