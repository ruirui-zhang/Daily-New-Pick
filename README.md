# Daily-New-Pick
The 'Daily New Picks' platform aims to assist in stock investment. The platform provides daily stock recommendations to investors by analyzing the latest financial news. Meanwhile, investors can create their own selected stocks and investment portfolios on the platform, view stock market quotations, review historical backtests, and monitor changes in stock indicators.

## Function 1: Recommend Stocks

By using the Tushare Pro financial data interface, we retrieve the latest 150 financial news headlines. The sentiment analysis of the news titles is carried out using the Python SnowNLP library. Based on the average sentiment value of each stock, they are sorted, and the top 6 stocks with the most positive sentiment are recommended daily.

## Function 2: Quantitative Investment

Based on the stocks added by investors to their portfolios, the platform recommends the optimal asset allocation ratio for investors in two ways: maximizing the Sharpe ratio and minimizing risk, catering to the needs of investors with different risk preferences. At the same time, investors can select a backtest period to conduct historical backtesting on the returns of their portfolio.

<img width="795" alt="image" src="https://github.com/ruirui-zhang/Daily-New-Pick/assets/63785649/ac7ca75e-3957-4c27-b3da-89159ea5ec9b">
