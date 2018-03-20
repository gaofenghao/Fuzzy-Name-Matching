# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:04:12 2017

@author: e610086
"""

import string
import numpy as np
import pandas as pd

full_cbs_addr = pd.read_excel('C:/Users/e610086/Desktop/Name_match/Cleint_address_from_CBS_Mark.xlsx')
full_cbs_addr.loc[:,'Address'] = pd.Series('',index = full_cbs_addr.index)

active_cbs_addr = full_cbs_addr[full_cbs_addr.Status == 'Active']
active_cbs_addr = active_cbs_addr.drop_duplicates(['Cust Long Desc'], keep = 'first')

for row in range(len(active_cbs_addr)):
    tmp = ''
    if str(active_cbs_addr['Address1'].values[row]) != 'nan' and str(active_cbs_addr['Address1'].values[row]) != ' ':
        tmp = tmp + str(active_cbs_addr['Address1'].values[row])
    if str(active_cbs_addr['Address2'].values[row]) != 'nan' and str(active_cbs_addr['Address2'].values[row]) != ' ':
        if tmp != ' ':
            tmp = tmp + ', ' + str(active_cbs_addr['Address2'].values[row])
        else:
            tmp = tmp + str(active_cbs_addr['Address2'].values[row])
    if str(active_cbs_addr['Address3'].values[row]) != 'nan' and str(active_cbs_addr['Address3'].values[row]) != ' ':
        if tmp != ' ':
            tmp = tmp + ', ' + str(active_cbs_addr['Address3'].values[row])
        else:
            tmp = tmp + str(active_cbs_addr['Address3'].values[row])
    if str(active_cbs_addr['AddressCity'].values[row]) != 'nan'  and  str(active_cbs_addr['AddressCity'].values[row]) != ' ' \
          and tmp != '':
              if tmp != '':
                  tmp = tmp + ', ' + str(active_cbs_addr['AddressCity'].values[row])
              else:
                  tmp = tmp + str(active_cbs_addr['AddressCity'].values[row])
    if str(active_cbs_addr['State'].values[row]) != 'nan' and str(active_cbs_addr['State'].values[row]) != ' ' \
          and tmp != '':
              if tmp != '':
                  tmp = tmp + ', ' + str(active_cbs_addr['State'].values[row])
              else:
                   tmp = tmp + str(active_cbs_addr['State'].values[row])
    if str(active_cbs_addr['Zip'].values[row]) != 'nan' and str(active_cbs_addr['Zip'].values[row]) != ' ' \
          and tmp != '':
              if tmp != '':
                  tmp = tmp + ' ' + str(active_cbs_addr['Zip'].values[row])
              else:
                  tmp = tmp + str(active_cbs_addr['Zip'].values[row])
    if str(active_cbs_addr['Cntry'].values[row]) != 'nan' and str(active_cbs_addr['Cntry'].values[row]) != ' ':
        tmp = tmp + ', ' + str(active_cbs_addr['Cntry'].values[row])
    else:
        if tmp != '' and tmp != ' ':
            tmp = tmp + ', USA'
        else:
            tmp = 'N/A'                               
    active_cbs_addr['Address'].values[row] = tmp               
