# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:37:26 2017

@author: e610086
"""

import string
import numpy as np
import pandas as pd

badger_funds = pd.read_csv('G:/CassandraGraph/BADGer_funds.csv')
far_funds = pd.read_excel('G:/CassandraGraph/FUND_LIST_Descriptors.xlsx')


badger_funds.loc[:,'ICI_Code'] = pd.Series('',index = badger_funds.index)
badger_funds.loc[:,'DIV_Code'] = pd.Series('',index = badger_funds.index)
badger_funds.loc[:,'Type_Code'] = pd.Series('',index = badger_funds.index)
badger_funds.loc[:,'Fund_Class'] = pd.Series('',index = badger_funds.index)

for i in range(len(badger_funds)):
    sub_far = far_funds[far_funds['F_FUND_NO'].str.find((badger_funds['FundNum'].values[i]))]
    if len(sub_far) != 0:
        badger_funds['ICI_Code'].values[i] = sub_far['ICI_CODE'].values[0]
        badger_funds['DIV_Code'].values[i] = sub_far['DIV_CODE'].values[0]
        badger_funds['Type_Code'].values[i] = sub_far['TYPE_CODE'].values[0]
        badger_funds['Fund_Class'].values[i] = sub_far['FUND_CLASS'].values[0]
