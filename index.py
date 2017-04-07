#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 21:55
# @Author  : Feng_xia
# @File    : index.py

import numpy as np
import pandas as pd

from model import query
from utility import sql, pandas_model,input_func
import re


def main():

    #创建类
    sql_connection = sql.sql_conn(pandas_model.input_name())

    #生成SQL查询函数
    query_seller = query.query_seller()

    # 调用类的fetchall方法
    data = sql_connection.fetchall(query_seller)

    # 调用类的close方法
    sql_connection.sql_close()

    # 创建pandas的DataFrame
    df = pd.DataFrame(data)

    # 转换数据类型
    df['金额'] = df['金额'].astype(float)


    # 遍历每列去空格
    for col_name in df.columns:
        df[col_name] = df[col_name].map(pandas_model.seller_strip)

    # 编号对应品牌
    df['品牌'] = df['编号'].map(pandas_model.brand)

    # df['辅助列']=df['客户编号'].str.find('2014')
    # 数据透视表
    index_pt,columns_pt=pandas_model.index_columns()

    client = input_func.input_select()

    a = pd.pivot_table(df[df['客户编号'].isin(client)],index=index_pt,columns=columns_pt,
                       values=['金额'], aggfunc=np.sum,margins=True)

    # 导出EXCEL
    a.to_excel(pandas_model.file_data(), index=True)

if __name__ == '__main__':
    main()
