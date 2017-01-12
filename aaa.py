from sqlalchemy import create_engine
import tushare as ts

df = ts.get_tick_data('600848', date='2016-07-22')
engine = create_engine('mysql://user:123456@127.0.0.1/Qing?charset=utf8')

#存入数据库
df.to_sql('tick_data',engine)
#test
#test2