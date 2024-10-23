# Uses yfinance to analyse the Nasdaq 100 stocks for technical formations: golden cross, death cross, upper, and lower band crosses
#
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
 
# Function to check for Golden Cross or Death Cross
def check_crosses(data):
    sma_50 = data['Close'].rolling(window=50).mean()
    sma_200 = data['Close'].rolling(window=200).mean()
    
    # Check for Golden Cross (50-day SMA crosses above 200-day SMA)
    golden_cross = (sma_50.shift(1) < sma_200.shift(1)) & (sma_50 > sma_200)
    
    # Check for Death Cross (50-day SMA crosses below 200-day SMA)
    death_cross = (sma_50.shift(1) > sma_200.shift(1)) & (sma_50 < sma_200)
    
    return pd.DataFrame({
        'Golden Cross': golden_cross,
        'Death Cross': death_cross
    }, index=data.index)
 
# Function to calculate Bollinger Bands and check if price crosses them
def bollinger_cross(data, window=20, num_of_std=2):
    rolling_mean = data['Close'].rolling(window).mean()
    rolling_std = data['Close'].rolling(window).std()
    upper_band = rolling_mean + (rolling_std * num_of_std)
    lower_band = rolling_mean - (rolling_std * num_of_std)
    
    # Check if price crosses above or below Bollinger Bands
    upper_cross = (data['Close'].shift(1) < upper_band.shift(1)) & (data['Close'] > upper_band)
    lower_cross = (data['Close'].shift(1) > lower_band.shift(1)) & (data['Close'] < lower_band)
    
    return pd.DataFrame({
        'Upper Band Cross': upper_cross,
        'Lower Band Cross': lower_cross
    }, index=data.index)
 
# Function to get NASDAQ-100 stocks
def get_nasdaq_100_stocks():
    return [
        'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'FB', 'TSLA', 'NVDA', 'UNH', 'JNJ', 
        'V', 'PG', 'MA', 'HD', 'WMT', 'ABT', 'ABBV', 'ACN', 'ATVI', 'ADBE', 
        'AMD', 'AAP', 'AMGN', 'AOS', 'APA', 'AIV', 'AEP', 'AMT', 'AWK', 'AZO', 
        'BA', 'BHF', 'BK', 'BIIB', 'BLK', 'BKNG', 'BAX', 'BDX', 'BRK.B', 'BBY', 
        'BII', 'BMY', 'CHTR', 'CVX', 'CMCSA', 'COF', 'CPRT', 'KO', 'CTAS', 'CSCO', 
        'CERN', 'CF', 'SCHW', 'CHD', 'XEC', 'CTSH', 'CME', 'COST', 'CTVA', 'DHI', 
        'DHR', 'DRI', 'DVN', 'ETR', 'ECL', 'EQR', 'ESS', 'ELV', 'EXC', 'EXPD', 
        'ES', 'FAST', 'FANG', 'FBHS', 'FISV', 'FITB', 'FE', 'FIS', 'GILD', 'IT', 
        'GNRC', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GWW', 'HAL', 'HIG', 'HAS', 'HSIC', 
        'HCA', 'PEAK', 'HSY', 'HUM', 'HBAN', 'IDXX', 'ILMN', 'INCY', 'INFO', 'INTC', 
        'ICE', 'INTU', 'ISRG', 'IVZ', 'IP', 'JBHT', 'JKHY', 'JPM', 'JNPR', 'KDP', 
        'KEY', 'KMB', 'KIM', 'KLAC', 'LHX', 'LH', 'LRCX', 'LEG', 'LEN', 'LLY', 
        'LMT', 'L', 'LOW', 'LUMN', 'M', 'MAR', 'MKC', 'MCD', 'MDLZ', 'MPWR', 
        'MRNA', 'MRLN', 'MPC', 'MS', 'MSI', 'MTCH', 'MTD', 'MU', 'NDAQ', 'NSC', 
        'NTRS', 'NOC', 'NUE', 'ODFL', 'OXY', 'PARA', 'PAYX', 'PEP', 'PKI', 'PFE', 
        'PM', 'PSX', 'PNC', 'POOL', 'PPG', 'PXD', 'PNR', 'PTC', 'PYPL', 'QCOM', 
        'RMD', 'RJF', 'RTN', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RVTY', 'CRM', 'SBAC', 
        'SLB', 'SNI', 'SWKS', 'SBUX', 'STT', 'STE', 'SYK', 'SIVB', 'SYF', 'SNPS', 
        'SRE', 'WBA', 'WRK', 'WBD', 'WM', 'WAT', 'WEC', 'WELL', 'WFC', 'ITW', 'WMB', 
        'WRB', 'WY', 'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS'
    ]
 
# Main analysis function
def analyze_nasdaq_stocks():
    nasdaq_stocks = get_nasdaq_100_stocks()
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)  # Data for the last year
    
    results = []
    for symbol in nasdaq_stocks:
        try:
            stock_data = yf.download(symbol, start=start_date, end=end_date)
            if stock_data is not None and not stock_data.empty:
                crosses = check_crosses(stock_data)
                bollinger_crosses = bollinger_cross(stock_data)
                recent_indicators = crosses.loc[crosses.index[-1]]
                recent_bollinger = bollinger_crosses.loc[bollinger_crosses.index[-1]]
                
                formations = []
                if recent_indicators['Golden Cross']:
                    formations.append("Golden Cross")
                if recent_indicators['Death Cross']:
                    formations.append("Death Cross")
                if recent_bollinger['Upper Band Cross']:
                    formations.append("Upper Band Cross")
                if recent_bollinger['Lower Band Cross']:
                    formations.append("Lower Band Cross")
                
                if formations:
                    results.append({
                        'Symbol': symbol,
                        'Formations': ', '.join(formations)
                    })
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
    
    return pd.DataFrame(results)
 
# Run the analysis
nasdaq_crosses = analyze_nasdaq_stocks()
print(nasdaq_crosses)
