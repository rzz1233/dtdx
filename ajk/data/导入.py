import pandas as pd
from sqlalchemy import create_engine
#
# # 读取Excel文件
df = pd.read_excel('ty_analysis.xlsx')

# 创建数据库连接（这里以MySQL为例）
engine = create_engine('mysql+pymysql://root:221266@localhost/ajk')

# 将数据写入数据库（如果表已存在，则追加数据；如果不存在，则由于我们已经手动创建了表，所以不会出现问题）
df.to_sql('ajkapp_taiyuan', con=engine, if_exists='append', index=False)