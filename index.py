#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 21:55
# @Author  : Feng_xia
# @File    : index.py

from utility import sql
import pandas as pd
from pandas import Series,DataFrame

def main():
    sql_connection=sql.sql_conn('win7-pc','CXHBI_010_2015','sa','123')
    query='''select dbo.outt.员工姓名,substring(dbo.bill.类别编号,1,3) as 编号,SUM(dbo.outdata.金额) as 金额
            from dbo.outdata join dbo.outt
            on dbo.outdata.单号=dbo.outt.单号
            join dbo.bill
            on dbo.outdata.编号=dbo.bill.编号
            where (dbo.outdata.日期 between '2015-1-1' and '2015-1-31')
            group by dbo.outt.员工姓名,substring(dbo.bill.类别编号,1,3) '''
    d=sql_connection.fetchall(query)
    sql_connection.sql_close()
    df = pd.DataFrame(d)
    df['金额']=df['金额'].astype(float)  #转换数据类型
    a=pd.pivot_table(df, index=['员工姓名','编号'],values=['金额'])
    a.to_excel('foo.xls', index=True)
if __name__ == '__main__':
    main()
