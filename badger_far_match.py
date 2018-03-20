# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:37:26 2017

@author: e610086
"""

import string
import numpy as np
import pandas as pd

badger_funds = pd.read_csv('G:/CassandraGraph/Old/BADGer_funds.csv')
far_funds = pd.read_excel('G:/CassandraGraph/Old/FUND_LIST_Descriptors.xlsx')


badger_funds.loc[:,'ICI_Code'] = pd.Series('',index = badger_funds.index)
badger_funds.loc[:,'DIV_Code'] = pd.Series('',index = badger_funds.index)
badger_funds.loc[:,'Type_Code'] = pd.Series('',index = badger_funds.index)
badger_funds.loc[:,'Fund_Class'] = pd.Series('',index = badger_funds.index)
badger_funds.loc[:,'GEMSID'] = pd.Series('',index = badger_funds.index)

for i in range(len(badger_funds)):
    sub_far = far_funds[far_funds['F_FUND_NO'] == 'F_'+str(badger_funds['FundNum'].values[i])]
    if len(sub_far) != 0:
        badger_funds['ICI_Code'].values[i] = sub_far['ICI_CODE'].values[0]
        badger_funds['DIV_Code'].values[i] = sub_far['DIV_CODE'].values[0]
        badger_funds['Type_Code'].values[i] = sub_far['TYPE_CODE'].values[0]
        badger_funds['Fund_Class'].values[i] = sub_far['FUND_CLASS'].values[0]
        badger_funds['GEMSID'].values[i] = str(badger_funds.index.values[i])
    else:
        badger_funds['ICI_Code'].values[i] = 'N/A'
        badger_funds['DIV_Code'].values[i] = 'N/A'
        badger_funds['Type_Code'].values[i] = 'N/A'
        badger_funds['Fund_Class'].values[i] = 'N/A'
        badger_funds['GEMSID'].values[i] = str(badger_funds.index.values[i])

#badger_funds_clean = badger_funds[badger_funds['ICI_Code'] != '']
#badger_funds_clean_short = badger_funds_clean.drop('Fund_Type',axis=1)
#badger_funds_clean_short = badger_funds_clean_short.drop('Hold_Type',axis=1)
#badger_funds_clean_short = badger_funds_clean_short.drop('Division',axis=1)
#badger_funds_clean_short_final = badger_funds_clean_short.drop('FundNum',axis=1)
for i in range(len(ver_holdings)):
    tmp = badger_funds[badger_funds['Fund_ID'] == ver_holdings['Fund_ID'].values[i]]
    if len(tmp) !=0:
        ver_holdings['FundID'].values[i] =tmp.index.values[0]
    tmp = sub_cusip[sub_cusip['CUSIP'] == ver_holdings['CUSIP'].values[i]]
    if len(tmp) != 0:
        ver_holdings['AssetID'].values[i] == tmp.index.values[0]