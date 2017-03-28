#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 21:55
# @Author  : Feng_xia
# @File    : index.py

import numpy as np
import pandas as pd

from model import query
from utility import sql, pandas_model


def main():

    sql_connection = sql.sql_conn(pandas_model.input_name())
    query_seller = query.query_seller()
    data = sql_connection.fetchall(query_seller)
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

    # 数据透视表
    a = pd.pivot_table(df, index=['客户名称'],columns=['员工姓名'], values=['金额'], aggfunc=np.sum,margins=True)

    # 导出EXCEL
    a.to_excel('coo.xls', index=True)


if __name__ == '__main__':
    main()
