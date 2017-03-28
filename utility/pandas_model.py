#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/27 10:02
# @Author  : Feng_xia
# @File    : pandas_model

def input_name():
    input_server=input('请输入服务器名:')
    input_data='CXHBI_010_'+input('请输入数据库：')
    input_pas=input('请输入密码：')
    return input_server,input_data,'sa',input_pas

# 品牌对应函数
def brand(num):
    brand_dict = {'010': '强生',
                  '020': '利华用品',
                  '030': '欧莱雅',
                  '040': '庄臣',
                  '050': '利华食品',
                  '060': '苏菲',
                  '070': '登康',
                  '080': '味事达',
                  '090': '白猫',
                  '100': '高露洁',
                  '110': '丁家宜',
                  '120': '滋洁',
                  '121': '榄霸',
                  '130': '威露士',
                  '140': '娇妍',
                  '150': '劳工',
                  '160': '潘雪',
                  '170': '艾诗',
                  '180': '曼秀雷敦',
                  '190': '爱家',
                  '200': '雷治',
                  '210': '珍妮诗',
                  '220': '澳雪流通',
                  '230': '亮晶晶',
                  '240': '日之泉',
                  '250': '春风',
                  '251': '上海制皂',
                  '260': '诺丝',
                  '270': '六神',
                  '380': '太阳神',
                  '410': '西瓜霜',
                  '420': '舒适达',
                  '470': '净逸',
                  '480': '嘉丽华',
                  '500': '天品洗衣膏',
                  '510': '清风',
                  '520': '纳美',
                  '530': '可爱宝贝',
                  '550': '鹏兴',
                  '580': '露施',
                  '610': '澳雪',
                  '630': '爱护系列',
                  '690': '蓝月亮',
                  '710': '江中',
                  '720': '银鹭',
                  '730': '进口食品',
                  '810': '凤球麦',
                  '820': '心之源',
                  '830': '晨光奶',
                  '840': '骆驼唛系列',
                  '850': '太港',
                  '860': '三利和',
                  '870': '傲鹏',
                  }
    if num == '90107':
        return '艾诗'
    elif num == '90108':
        return '强生'
    else:
        num_cut = num[0:3]
        if num_cut in brand_dict:
            return brand_dict[num_cut]
        else:
            return '其他'

# 去空格函数


def seller_strip(seller_str):
    try:
        if isinstance(seller_str, str):
            return seller_str.strip()
        else:
            return seller_str
    except AttributeError as e:
        print('有未知字段')
        return '未知字段'
