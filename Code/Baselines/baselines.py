import numpy as np
import pandas as pd

class NaiveBaseline:
    def __init__(self):
        self.last_value = None

    def fit(self, ts):
        """Fit the model by storing the last value of the time series.
        Args:
            ts (numpy array or pandas Series): The time series data.
        """
        # Convert pandas Series to numpy array if input is a pandas Series
        if isinstance(ts, pd.Series):
            ts = ts.values  # Convert to numpy array
        self.last_value = ts[-1]
        
    def forecast(self, h):
        """Forecast for the next h time periods using the last observed value.
        Args:
            h (int): Number of periods to forecast.
        Returns:
            numpy array: Forecasted values.
        """
        return np.full(h, self.last_value)

class SeasonalAverage:
    
    def __init__(self,season_length):
        self.season_length = season_length
        self.seasonality_averages = None

    def fit(self, ts):
        """Fit the model to the time series data."""
        
        if isinstance(ts, pd.Series):
            ts = ts.values

        s = self.season_length
        self.train_len = len(ts)

        if len(ts) < s + 1:
            raise ValueError("Need more data than one season")
        
        seasonality_averages = np.ones(self.season_length)
        for i in range(self.season_length):
            seasonality_averages[i] = ts[np.arange(self.train_len)%self.season_length == i].mean()
        self.seasonality_averages = seasonality_averages


    def forecast(self, h):
        """Generate a forecast for the next 'h' time periods."""
        # Check if model has been fitted
        if self.seasonality_averages is None:
            raise ValueError("The model has not been fitted yet. Call 'fit' first.")
        
        # Generate forecast
        seasonality_forecast = np.ones(h)
        for i, j in enumerate(np.arange(self.train_len,self.train_len+h)):
            seasonality_forecast[i] = self.seasonality_averages[j%self.season_length]
        return seasonality_forecast

class SeasonalRandomWalk:
   
    def __init__(self, season_length):
        self.season_length = season_length
        self.last_season_values = None
        self.train_len = None

    def fit(self, ts):
        if isinstance(ts, pd.Series):
            ts = ts.values

        s = self.season_length
        self.train_len=len(ts)

        if len(ts) < s + 1:
            raise ValueError("Need more data than one season")
        
        self.last_season_values = ts[-s:]
        

    def forecast(self, h):
        if self.last_season_values is None:
            raise ValueError("The model has not been fitted yet. Call 'fit' first.")
        
        s=self.season_length
        tl=self.train_len

        # Generate the absolute timeline indices for the future forecast horizon
        future_indices = np.arange(tl, tl + h)

        # Use modulo arithmetic to index directly back into the last observed season
        seasonal_naive_forecast = self.last_season_values[future_indices % s]

        return seasonal_naive_forecast