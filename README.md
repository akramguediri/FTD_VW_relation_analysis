# Financial Analysis of Short Selling Impact on Volkswagen During the 2008-2009 Financial Crisis

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Data Sources](#data-sources)
5. [Running the Scripts](#running-the-scripts)
   - [Download Data](#download-data)
   - [Analyze Data](#analyze-data)
   - [Sentiment Analysis](#sentiment-analysis)
6. [Analysis and Results](#analysis-and-results)
7. [Dependencies](#dependencies)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction

This project aims to analyze the impact of short selling on Volkswagen stock and the broader market during the 2008-2009 financial crisis. The analysis includes:

- Correlation analysis between Volkswagen stock prices and Failures to Deliver (FTD) volumes.
- Regression analysis to explore the relationship between FTD volumes and stock prices.
- Sentiment analysis of news articles related to Volkswagen during the period of interest.

---

## Project Structure

financial_analysis/<br>
├── data/<br>
│ ├── volkswagen_stock_prices.csv<br>
│ ├── ftd_data.csv<br>
│ ├── sp500_index.csv<br>
│ └── news_articles.json<br>
├── scripts/<br>
│ ├── download_data.py<br>
│ ├── analyze_data.py<br>
│ └── sentiment_analysis.py<br>
├── requirements.txt<br>
└── README.md<br>

- **data/**: Directory to store all datasets.
- **scripts/**: Directory containing Python scripts for data download, analysis, and sentiment analysis.
- **requirements.txt**: File listing all Python dependencies.
- **README.md**: Detailed project documentation.

---

## Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/financial_analysis.git
   cd financial_analysis

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt

## Data Sources
The data used in this project includes:

- Volkswagen Stock Prices: Historical stock prices for Volkswagen.
- Failures to Deliver (FTD) Data: FTD data for Volkswagen.
- S&P 500 Index Data: Historical S&P 500 index data.
- News Articles: News articles related to Volkswagen.

## Running the Scripts
1. **Download and Parse Data**
This script downloads the required datasets and saves them into the data/ directory.
    ```bash
    python scripts/download_data.py
paste the data of 2007-2008 files from [SEC FTD](https://www.sec.gov/data/foiadocsfailsdatahtm) in the data folder (use curl)
these two scripts will parse the data accordingly.

   ```bash
   python scripts/parseftd.py
   python scripts/convert_text_csv.py

2. **Analyze Data**
This script loads and analyzes the data, performing correlation and regression analysis.
    ```bash
    python scripts/analyze_data.py
3. **Sentiment Analysis**
This script performs sentiment analysis on the news articles related to Volkswagen.
    ```bash
    python scripts/sentiment_analysis.py

## Analysis and Results
The analysis includes the following components:

1. Correlation Analysis: Identifies correlations between Volkswagen stock prices and FTD volumes.
2. Regression Analysis: Explores the relationship between FTD volumes and stock prices.
3. Sentiment Analysis: Analyzes the sentiment of news articles related to Volkswagen during the period of interest.
**Example Outputs:**
***Correlation Analysis***
The correlation matrix showing the relationship between Volkswagen stock prices and FTD volumes.

***Regression Analysis***
A summary of the regression analysis exploring the relationship between FTD volumes and Volkswagen stock prices.

***Sentiment Analysis***
A plot showing the sentiment of news articles over time.

## Dependencies
The project relies on the following Python libraries:

- `yfinance`
- `requests`
- `pandas`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `textblob`

These dependencies are listed in the `requirements.txt` file and can be installed using `pip install -r requirements.txt`.

## Contributing
Contributions are welcome! Please create a pull request or submit an issue if you have any suggestions or find any bugs.
