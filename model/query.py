#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/27 10:10
# @Author  : Feng_xia
# @File    : query

import time

# sql查询员工姓名、类别编号、金额
def query_seller():
    input_time=input('请输入日期：')
    if input_time == '':
        time_start, time_end=time.strftime('%Y-%m-01',time.localtime(time.time())),\
                             time.strftime('%Y-%m-%d',time.localtime(time.time()))
    else:
        time_start, time_end = input_time.split()
    print(time_start,time_end)
    seller = '''select dbo.outt.员工姓名,dbo.outt.客户名称,dbo.bill.类别编号 as 编号,SUM(dbo.outdata.金额) as 金额
                from dbo.outdata join dbo.outt
                on dbo.outdata.单号=dbo.outt.单号
                join dbo.bill
                on dbo.outdata.编号=dbo.bill.编号
                where (dbo.outdata.日期 between '{}' and '{}')
                group by dbo.outt.员工姓名,dbo.outt.客户名称,dbo.bill.类别编号 '''.format(
        time_start, time_end)
    return seller
