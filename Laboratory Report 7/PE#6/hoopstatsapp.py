"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(df):
    """Cleans the data frame by splitting the 'FG', '3PT', and 'FT' columns into 'makes' and 'attempts'."""
    for col in ['FG', '3PT', 'FT']:
        if col in df.columns:
            makes_attempts = df[col].str.split('-', expand=True).astype(int)
            makes_col = col + 'M'
            attempts_col = col + 'A'
            df[makes_col] = makes_attempts[0]
            df[attempts_col] = makes_attempts[1]
            df.drop(columns=[col], inplace=True)
    return df

def main():
    """Creates the data frame and view and starts the app."""
    # Load the raw data
    raw_frame = pd.read_csv("rawbrogdonstats.csv")
    
    # Clean the data
    clean_frame = cleanStats(raw_frame)
    
    # Save the cleaned data
    clean_frame.to_csv("cleanbrogdonstats.csv", index=False)
    
    # Load the cleaned data and pass it to the view
    frame = pd.read_csv("cleanbrogdonstats.csv")
    HoopStatsView(frame)

if __name__ == "__main__":
    main()

