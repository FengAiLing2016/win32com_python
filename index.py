#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 21:55
# @Author  : Feng_xia
# @File    : index.py

from utility import sql
import pandas as pd
from pandas import Series,DataFrame

def brand(num):
    brand_dict = {'010':'强生',
'020':'利华用品',
'030':'欧莱雅',
'040':'庄臣',
'050':'利华食品',
'060':'苏菲',
'070':'登康',
'080':'味事达',
'090':'白猫',
'100':'高露洁',
'110':'丁家宜',
'120':'滋洁',
'121':'榄霸',
'130':'威露士',
'140':'娇妍',
'150':'劳工',
'160':'潘雪',
'170':'艾诗',
'180':'曼秀雷敦',
'190':'爱家',
'200':'雷治',
'210':'珍妮诗',
'220':'澳雪流通',
'230':'亮晶晶',
'240':'日之泉',
'250':'春风',
'251':'上海制皂',
'260':'诺丝',
'270':'六神',
'380':'太阳神',
'410':'西瓜霜',
'420':'舒适达',
'470':'净逸',
'480':'嘉丽华',
'500':'天品洗衣膏',
'510':'清风',
'520':'纳美',
'530':'可爱宝贝',
'550':'鹏兴',
'580':'露施',
'610':'澳雪',
'630':'爱护系列',
'690':'蓝月亮',
'710':'江中',
'720':'银鹭',
'730':'进口食品',
'810':'凤球麦',
'820':'心之源',
'830':'晨光奶',
'840':'骆驼唛系列',
'850':'太港',
'860':'三利和',
'870':'傲鹏',
}
    if num in brand_dict:
        return brand_dict[num]
    else:
        return 'kong'


def main():

    sql_connection=sql.sql_conn('gqserver','CXHBI_010_2014','sa','2016guangQIANG')
    query='''select dbo.outt.员工姓名,substring(dbo.bill.类别编号,1,3) as 编号,SUM(dbo.outdata.金额) as 金额
            from dbo.outdata join dbo.outt
            on dbo.outdata.单号=dbo.outt.单号
            join dbo.bill
            on dbo.outdata.编号=dbo.bill.编号
            where (dbo.outdata.日期 between '2017-1-1' and '2017-1-31')
            group by dbo.outt.员工姓名,substring(dbo.bill.类别编号,1,3) '''
    d=sql_connection.fetchall(query)
    sql_connection.sql_close()
    df = pd.DataFrame(d)
    df['金额']=df['金额'].astype(float)  #转换数据类型
    # df['品牌']=df['编号'].map(brand)
    df.head()
    a=pd.pivot_table(df, index=['员工姓名'])
    print(a)
    # a.to_excel('too.xls', index=True)
if __name__ == '__main__':
    main()
