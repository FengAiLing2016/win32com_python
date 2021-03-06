#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 16:17
# @Author  : Feng_xia
# @File    : sql


import win32com.client

class sql_conn(object):

    def __init__(self, *args):
        server_name,data_name,user_name,pwd = args[0]
        self.server_name = server_name
        self.data_name = data_name
        self.user_name = user_name
        self.pwd = pwd
        try:
            self.conn_sql = win32com.client.Dispatch('ADODB.Connection')
            self.conn_sql.Open(
                "Provider=SQLOLEDB;SERVER=%s;DATABASE=%s" %
                (self.server_name, self.data_name), self.user_name, self.pwd)
        except Exception as e:
            print("sql_server Error "% e)
            raise



    # select函数
    def select_sql(self, sql):
        self.select_Sql = self.conn_sql.Execute(sql)[0]

    # 返回SQL数据
    def fetchall(self, sql):
        self.select_sql(sql)
        data = {}
        value = self.select_Sql.GetRows()
        for i in range(len(value)):
            data[self.select_Sql.Fields(i).Name] = value[i]
        return data

    def sql_close(self):
        self = None
        return self
