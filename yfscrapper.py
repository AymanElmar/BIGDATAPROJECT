import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Get the data for the stock TSLA
data = yf.download('TSLA','2021-01-01','2023-11-24')
# save to csv
data.to_csv('TSLAYF.csv')