#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 21:55
# @Author  : Feng_xia
# @File    : index.py

from utility import sql
from model import pandas_model,query
import pandas as pd
import numpy as np
from pandas import Series,DataFrame


def main():

    sql_connection=sql.sql_conn('gqserver','CXHBI_010_2014','sa','2016guangQIANG')
    query_seller=query.query_seller()
    data=sql_connection.fetchall(query_seller)
    sql_connection.sql_close()
    df = pd.DataFrame(data)   #创建pandas的DataFrame
    df['金额']=df['金额'].astype(float)  #转换数据类型
    df['品牌']=df['编号'].map(pandas_model.brand) #编号对应品牌
    df['员工姓名']=df['员工姓名'].map(pandas_model.seller_strip)  #去空格
    a=pd.pivot_table(df, index=['员工姓名','品牌'],values=['金额'],aggfunc=np.sum)  #数据透视表
    a.to_excel('coo.xls', index=True)  #导出EXCEL
if __name__ == '__main__':
    main()
