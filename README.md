# Daily-New-Pick
The 'Daily New Picks' platform aims to assist in stock investment. The platform provides daily stock recommendations to investors by analyzing the latest financial news. Meanwhile, investors can create their own selected stocks and investment portfolios on the platform, view stock market quotations, review historical backtests, and monitor changes in stock indicators.

## Function 1: Recommend Stocks

By using the Tushare Pro financial data interface, we retrieve the latest 150 financial news headlines. The sentiment analysis of the news titles is carried out using the Python SnowNLP library. Based on the average sentiment value of each stock, they are sorted, and the top 6 stocks with the most positive sentiment are recommended daily.

## Function 2: Quantitative Investment

Based on the stocks added by investors to their portfolios, the platform recommends the optimal asset allocation ratio for investors in two ways: maximizing the Sharpe ratio and minimizing risk, catering to the needs of investors with different risk preferences. At the same time, investors can select a backtest period to conduct historical backtesting on the returns of their portfolio.

<img width="795" alt="image" src="https://github.com/ruirui-zhang/Daily-New-Pick/assets/63785649/ac7ca75e-3957-4c27-b3da-89159ea5ec9b">

Here's the translation for the provided content:

---

### I. System Operation Steps:

1. Firstly, run the "sentiment_analysis.ipynb" within the "Sentiment Analysis" folder to update the stock recommendation list in the database.
2. Then, navigate to the folder path. In the command prompt (cmd), enter "python manage.py runserver 0.0.0.0:8000".
3. Access the website by entering the URL "127.0.0.1:8000/finweb".

### II. Required Packages for the System:

```python
# Required packages
Django ——4.0
tushare ——1.2.77
easyquotation ——0.7.4
jieba ——0.42.1
snownlp ——0.12.3
scipy ——1.7.3
pymysql
urllib
http.client
rpy2.robjects
statsmodels.api
matplotlib.pyplot
pandas
numpy
random
time
datetime
os
re
sys

# Usage method for the tushare package
import tushare as ts
ts.set_token('your token')
pro=ts.pro_api()
```

### III. Database:

```
host = 'localhost'
port = 3306
user = 'root'
password = 'your password'
db = 'fintech'
```
