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
