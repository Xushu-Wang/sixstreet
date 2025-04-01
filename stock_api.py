import requests
from datetime import datetime
from typing import Dict, Any


class StockAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"
        self.cache = {}  # Stores fetched data to minimize API calls

    def _fetch_data(self, symbol):
        """Fetches daily time series data for the given symbol from Alpha Vantage."""

        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key,
            "outputsize": "compact"
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        
        if 'Time Series (Daily)' not in data:
            error_message = data.get('Note', data.get('Error Message', 'Unknown error occurred.'))
            raise ValueError(f"Failed to fetch data for {symbol}: {error_message}")
        
        daily_data = data['Time Series (Daily)']
        # Parse and sort dates in reverse chronological order (newest first)
        sorted_dates = sorted(
            daily_data.keys(),
            key=lambda x: datetime.strptime(x, '%Y-%m-%d'),
            reverse=True
        )
        # Cache both the dictionary and sorted list of dates for the symbol
        self.cache[symbol] = {
            'by_date': daily_data,
            'sorted_dates': sorted_dates
        }

    def lookup(self, symbol, date_str):
        """Returns the OHLCV data for the given symbol and date."""
        if symbol not in self.cache:
            try:
                self._fetch_data(symbol)
            except ValueError as e:
                raise e
        
        symbol_data = self.cache[symbol]['by_date']
        daily_entry = symbol_data.get(date_str)
        if not daily_entry:
            return None
        
        try:
            return {
                'open': float(daily_entry['1. open']),
                'high': float(daily_entry['2. high']),
                'low': float(daily_entry['3. low']),
                'close': float(daily_entry['4. close']),
                'volume': int(daily_entry['5. volume'])
            }
        except KeyError as e:
            raise ValueError(f"Unexpected data format for {symbol} on {date_str}") from e

    def min(self, symbol, n):
        """Finds the lowest low price over the last n data points for the symbol."""
        if n <= 0:
            raise ValueError("n must be a positive integer")
        
        if symbol not in self.cache:
            try:
                self._fetch_data(symbol)
            except ValueError as e:
                raise e
        
        symbol_cache = self.cache[symbol]
        dates = symbol_cache['sorted_dates']
        # Ensure we don't exceed available data points
        selected_dates = dates[:n]
        if not selected_dates:
            return None
        
        lows = []
        for date in selected_dates:
            entry = symbol_cache['by_date'][date]
            lows.append(float(entry['3. low']))
        
        return min(lows) if lows else None

    def max(self, symbol, n):
        """Finds the highest high price over the last n data points for the symbol."""
        if n <= 0:
            raise ValueError("n must be a positive integer")
        
        if symbol not in self.cache:
            try:
                self._fetch_data(symbol)
            except ValueError as e:
                raise e
        
        symbol_cache = self.cache[symbol]
        dates = symbol_cache['sorted_dates']
        selected_dates = dates[:n]
        if not selected_dates:
            return None
        
        highs = []
        for date in selected_dates:
            entry = symbol_cache['by_date'][date]
            highs.append(float(entry['2. high']))
        
        return max(highs) if highs else None


if __name__ == "__main__":
    # Example usage
    api_key = "JMWC1IWUBQMFY6ZP"
    fetcher = StockAPI(api_key)

    # Lookup example
    print(fetcher.lookup("IBM", "2025-03-28"))

    # Min example
    print(fetcher.min("IBM", 5))

    # Max example
    print(fetcher.max("IBM", 5))
