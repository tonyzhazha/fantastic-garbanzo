#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:56:46 2018

@author: zhayiqiang
"""

import pandas as pd
import numpy as np



if __name__ == '__main__':
	user_table = pd.read_csv('/Users/zhayiqiang/Downloads/tianchi_train/DataSet/tianchi_fresh_comp_train_user.csv') #2300万数据
	item_table = pd.read_csv('/Users/zhayiqiang/Downloads/tianchi_train/DataSet/tianchi_fresh_comp_train_item.csv') #62万数据
	user_table = user_table[user_table.item_id.isin(list(item_table.item_id))] #208万数据
	user_table['days'] = user_table['time'].map(lambda x:x.split(' ')[0])
	user_table['hours'] = user_table['time'].map(lambda x:x.split(' ')[1])
	user_table = user_table[user_table['days'] != '2014-12-12']
	user_table = user_table[user_table['days'] != '2014-12-11']
	user_table.to_csv('/Users/zhayiqiang/Downloads/tianchi_train/DataSet/drop1112_sub_item.csv',index=None)
