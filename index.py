#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 21:55
# @Author  : Feng_xia
# @File    : index.py

from utility import sql
import pandas as pd

def main():
    sql_connection=sql.sql_conn('gqserver','CXHBI_010_2015','sa','2016guangQIANG')
    query="select 编号 from dbo.bill where 编号 like '01%' "
    pd.read_sql(query, sql_connection)
    sql_connection.sql_close()
if __name__ == '__main__':
    main()