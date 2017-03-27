#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/27 10:10
# @Author  : Feng_xia
# @File    : query

#sql查询员工姓名、类别编号、金额
def query_seller():
    time_start,time_end=input().split()
    seller='''select dbo.outt.员工姓名,dbo.bill.类别编号 as 编号,SUM(dbo.outdata.金额) as 金额
                from dbo.outdata join dbo.outt
                on dbo.outdata.单号=dbo.outt.单号
                join dbo.bill
                on dbo.outdata.编号=dbo.bill.编号
                where (dbo.outdata.日期 between '{}' and '{}')
                group by dbo.outt.员工姓名,dbo.bill.类别编号 '''.format(time_start,time_end)
    return seller