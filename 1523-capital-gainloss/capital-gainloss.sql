SELECT stock_name,
       SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) -
       SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END) AS capital_gain_loss
FROM STOCKS
GROUP BY stock_name;
