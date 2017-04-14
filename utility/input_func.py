#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/2 10:08
# @Author  : Feng_xia
# @File    : input_func


def index_columns():
    index_num=input('''请输入所要查询的内容：
1.客户查询
2.某区段客户
3.客户+品牌
4.业务员+品牌
5.业务员+客户+品牌
6.某区段品牌
''')
    if index_num == '1':
        return ['品牌'],['员工姓名']
    elif index_num == '2':
        return ['客户名称'],['品牌']
    elif index_num == '3':
        return ['客户名称','品牌'],['员工姓名']


def input_select():
    input_sum=input('''
    1.按客户查询
    2.按业务员查询
    ''')
    if input_sum == '1':
        input_client=input('''
        1.客户品牌销售报表
        2.客户区段品牌销售报表
        3.区段客户区段品牌销售报表
        ''')
        if input_client=='1':
            return ['客户名称'], ['品牌']
        elif input_client=='2':
            return
    elif input_sum =='2':
        input_clerk=input('''
        1.业务员销售报表
        2.业务员品牌销售报表
        3.业务员区段品牌销售报表
        ''')



def query_seller():
    input_time=input('请输入日期：')
    if input_time == '':
        Time_start, Time_end=time.strftime('%Y-%m-01',time.localtime(time.time())),\
                             time.strftime('%Y-%m-%d',time.localtime(time.time()))
    else:
        Time_start, Time_end = input_time.split()
    return Time_start, Time_end