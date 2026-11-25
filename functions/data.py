import pandas as pd 
import yfinance as yf

def download_data(ticker:str) -> pd.DataFrame:
    """"
    download histirucak data.

    Arg:
        ticker(stry): Ticker name.
    """
    df = yf.download(
        tickers = ticker,
        multi_level_index = False
    ).reset_index()

    return df
