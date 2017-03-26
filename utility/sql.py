#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 16:17
# @Author  : Feng_xia
# @File    : sql
import win32com.client
class sql_conn(object):
    def __init__(self,server_name,data_name,user_name,pwd):
        self.server_name=server_name
        self.data_name=data_name
        self.user_name=user_name
        self.pwd=pwd
        try:
            self.conn_sql = win32com.client.Dispatch('ADODB.Connection')
            self.conn_sql.Open("Provider=SQLOLEDB;SERVER=%s;DATABASE=%s" % (self.server_name,self.data_name),
                      self.user_name, self.pwd)
        except win32com.Error as e:
            print("sql_server Error %d: %s" % (e.args[0], e.args[1]))
    def select_sql(self,sql):
        self.select_Sql = self.conn_sql.Execute(sql)[0]

    def fetchall(self,sql):
        self.select_sql(sql)
        value = []
        data = {}
        for i in range(len(self.select_Sql.Fields)):
            while not self.select_Sql.EOF:
                value.append(self.select_Sql.Fields(i).value.rstrip())
                self.select_Sql.MoveNext()
            data[self.select_Sql.Fields(i).Name] = value
            value = []
            self.select_Sql.MoveFirst()
        return data
    def sql_close(self):
        self = None
        return self

