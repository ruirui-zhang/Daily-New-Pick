# -*- coding: utf-8 -*-
from django.urls import path,re_path
from finweb import views

urlpatterns =[ 
             path(r'',views.index,name='index'),
             path('register/',views.register,name='register'),
             path('login/',views.user_login,name='login'),
            #  path('rules/',views.rules,name='rules'),
             path('changepassword/',views.changepassword,name='changepassword'),
             path('changeinfo/',views.changeinfo,name='changeinfo'),
             path('logout/',views.user_logout,name='logout'),
             path('get_index_data/',views.get_index_data,name='get_index_data'),
             path('get_span_data/',views.get_span_data,name='get_span_data'),
             path('get_stocks_data/',views.get_stocks_data,name='get_stocks_data'),
             path('stocks_to_info/',views.stocks_to_info,name='stocks_to_info'),
             path('delete_stocks/',views.delete_stocks,name='delete_stocks'),
             path('add_stocks_toport/',views.add_stocks_toport,name='add_stocks_toport'),
             path('userinfo/',views.userinfo,name='userinfo'),
             path('quant/',views.quant,name='quant'), #量化投资
             path('operate/',views.operate,name='operate'),#股票操作
             path('stocks/',views.stocks,name='stocks'),#我的自选股
             path('portfolio/',views.portfolio,name='portfolio'),#我的投资组合
             path('add_portfolio/',views.add_portfolio,name='add_portfolio'),#创建投资组合
             path('port_to_info',views.port_to_info,name='port_to_info'),#跳转
             path('delete_stocks_inp/',views.delete_stocks_inp,name='delete_stocks_inp'),#删除组合中的股票
             path('delete_portfolio/',views.delete_portfolio,name='delete_portfolio'),#删除组合
             path('stockinfo/',views.stockinfo,name='stockinfo'),#个股信息页面
             path('get_info_stockdata/',views.get_info_stockdata,name='get_info_stockdata'),#个股信息页面上更新span
             path('get_info_kdata/',views.get_info_kdata,name='get_info_kdata'),#个股信息页面上获取k线数据
             path('get_info_search/',views.get_info_search,name='get_info_search'),#个股信息页面搜索
             path('addto_stocks/',views.addto_stocks,name='addto_stocks'),#个股信息,添加到自选股
            #  path('indicator/',views.indicator,name='indicator'),#技术指标
            #  path('get_macd/',views.get_macd,name='get_macd'), #获得MACD指标图像
            #  path('get_adx/',views.get_adx,name='get_adx'), #获得ADX指标图像
            #  path('get_sma/',views.get_sma,name='get_sma'), #获得SMA指标图像
            #  path('get_bbands/',views.get_bbands,name='get_bbands'), #获得BBands指标图像
             path('get_quant_data/',views.get_quant_data,name='get_quant_data'),#选择组合
            #  path('factor_analysis/',views.factor_analysis,name='factor_analysis'),#多因子分析
             path('stock_ratio/',views.stock_ratio,name='stock_ratio'), #资产配置
             path('get_stock_ratio/',views.get_stock_ratio,name='get_stock_ratio'),
             path('revenue_test/',views.revenue_test,name='revenue_test'),#收益回测
             path('fin_data/',views.fin_data,name='fin_data'),
             path('notices/',views.notices,name='notices'),
             path('candle1/',views.candle1,name='candle1'),#test
             path('news_test/',views.news_test,name='news_test'),#test
             path('candle/',views.candle,name='candle'),#test
             path('echarts/',views.echarts,name='echarts'), #test
             path('test/',views.test,name='test'), #test
]
