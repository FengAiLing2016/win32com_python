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
    def cursor(self):
        n = self.conn_sql.Execute()
        return n
    def sql_close(self):
        self.conn_sql.Close()

