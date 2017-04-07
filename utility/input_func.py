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
    print('''
    1.输入客户
    2.输入品牌
    3.输入业务员
    4.查询所有
    ''')
    input_sel=input()
    if  input_sel =='1':
        input_client=input('输入客户编号，空格分开').split()
        return input_client

def query_seller():
    input_time=input('请输入日期：')
    if input_time == '':
        Time_start, Time_end=time.strftime('%Y-%m-01',time.localtime(time.time())),\
                             time.strftime('%Y-%m-%d',time.localtime(time.time()))
    else:
        Time_start, Time_end = input_time.split()
    return Time_start, Time_end