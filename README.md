# airia_python_examples
Example Python for Airia.ai

# Airia Pipeline Execution
call_airia_pipeline.py  
  
## Description
This Python script demonstrates how to execute an Airia Pipeline using the Airia API. It sends a POST request to the Airia Pipeline Execution endpoint with user input and receives the pipeline output.

## Features
- Executes an Airia Pipeline via API
- Sends user input to the pipeline
- Supports synchronous execution (can be modified for asynchronous)
- Uses API key authentication

# System Information Retriever
## Description
This Python script retrieves and displays various system information details about the environment where the code is executed. It provides a comprehensive overview of the system, including hardware, OS, and current runtime details.
  
## Features
- Retrieves system name, node name, release, version, and machine type
- Displays kernel version
- Shows user ID, group ID, process ID, and parent process ID
- Reports CPU count
- Provides system load averages for 1, 5, and 15 minutes

# Plot Generator and Encoder
## Description
This Python script generates a sine wave plot using Matplotlib, saves it as a PNG image, and then encodes the image to base64 format. This encoded image can be easily transmitted or embedded in other applications, such as web pages or documents.
  
## Features
- Generates a sine wave plot
- Saves the plot as a PNG image in memory
- Encodes the image to base64 format
- Outputs the base64-encoded string

# Wolfram Alpha API Caller
## Description
This Python script demonstrates how to make a call to the Wolfram Alpha API. It sends a user-provided query to the Wolfram Alpha LLM API and retrieves the response.
  
## Features
- Sends a user query to the Wolfram Alpha LLM API
- Retrieves and outputs the API response
- Simple and straightforward implementation
  
## Setup
Before running the script, you need to obtain a Wolfram Alpha API key:
- Go to the Wolfram Alpha Developer Portal.
- Sign up for an account or log in if you already have one.
- Create a new app to get an AppID (API key).
  
## Usage
- Save the script to a file (e.g., wolfram_alpha_api_caller.py).
- Replace the placeholder in the key variable with your actual Wolfram Alpha API key:
```key = "Your-Wolfram-Alpha-API-Key-Here"```
  
# Nasdaq 100 Stock Analysis Tool
## Description
This Python script analyzes Nasdaq 100 stocks for technical formations including golden cross, death cross, and Bollinger Band crosses. It uses the yfinance library to fetch historical stock data and pandas for data manipulation and analysis.
  
## Features
- Fetches historical data for Nasdaq 100 stocks
- Identifies Golden Cross and Death Cross formations
- Detects crosses of upper and lower Bollinger Bands
- Provides a summary of recent technical formations for each stock

## How it Works
- The script defines a list of Nasdaq 100 stocks.
- For each stock, it downloads the last year of historical data using yfinance.
- It then checks for the following technical formations:
-- Golden Cross (50-day SMA crosses above 200-day SMA)
-- Death Cross (50-day SMA crosses below 200-day SMA)
-- Upper Bollinger Band Cross
-- Lower Bollinger Band Cross
- The results are compiled into a DataFrame and printed.

# URL Content Type Detector
## Description
This Python script is designed to detect the content type of a given URL. It's primarily used to determine whether the URL points to a file or a webpage, which can then be used to decide which scraper to call (e.g., a file downloader-scraper or a webpage scraper).  
  
## Features
- Sends a GET request to the specified URL  
- Retrieves the Content-Type header from the response  
- Handles potential errors during the request  
- Returns the content type as a string  
  
# Web Scraping Tool for LLM Inference
## Description
This Python script is designed to scrape text content from a given webpage URL. It's primarily intended for use with Large Language Model (LLM) inference, providing clean, formatted text data from web sources.  
  
## Features  
- Scrapes text content from a specified URL  
- Cleans and formats the extracted text  
- Handles common web scraping challenges (e.g., user agent spoofing)  
- Returns the scraped content as a JSON string

# PDF Processing Tool for LLM Inference
## Description
This Python script is designed to extract and process text content from PDF documents accessed via URL. It's primarily intended for use with Large Language Model (LLM) inference, providing clean, formatted text data from PDF sources.  
  
## Features  
- Downloads PDF documents from a given URL  
- Extracts text content from all pages of the PDF  
- Handles multi-column layouts  
- Processes images within the PDF (though text extraction from images is not implemented)  
- Returns the extracted content as a single string  
