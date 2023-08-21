### 一、系统运行步骤

1. 首先运行情感分析文件夹中的 ”情感分析.ipynb“，更新数据库中推荐股票列表。
2. 之后在“STOCKWEBSITE”文件夹路径下，在cmd中输入"python manage.py runserver 0.0.0.0:8000"
3. 输入网址“127.0.0.1:8000/finweb”即可。

### 二、系统需要的包


```python
#需要的包
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

#tushare包使用方法
import tushare as ts
ts.set_token('0c1528160ad2b51ea43872ded226137ff7ece65d54d806db191d68e6')
pro=ts.pro_api()
```

### 三、数据库

```
host = 'localhost'
port = 3306
user = 'root'
password = 'Cliu123#'
db = 'fintech'
```

