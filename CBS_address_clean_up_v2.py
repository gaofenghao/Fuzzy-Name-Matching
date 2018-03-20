# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:26:37 2017

@author: e610086
"""

import string
import numpy as np
import pandas as pd

full_cbs_addr = pd.read_excel('C:/Users/e610086/Desktop/Name_match/Cleint_address_from_CBS_Mark.xlsx')
full_cbs_addr.loc[:,'Address'] = pd.Series('',index = full_cbs_addr.index)

active_cbs_addr = full_cbs_addr[full_cbs_addr.Status == 'Active']
#active_cbs_addr = active_cbs_addr.drop_duplicates(['Cust Long Desc'], keep = 'first')

for row in active_cbs_addr.itertuples(index = True, name = 'Pandas'):
    tmp = ''
    if str(getattr(row,'Address1')) != 'nan' and str(getattr(row,'Address1')) != ' ':
        tmp = tmp + str(getattr(row,'Address1'))
    if str(getattr(row,'Address2')) != 'nan' and str(getattr(row,'Address2')) != ' ':
        if tmp != '':
            tmp = tmp + ', ' + str(getattr(row,'Address2'))
        else:
            tmp = tmp + str(getattr(row,'Address2'))
    if str(getattr(row,'Address3')) != 'nan' and str(getattr(row,'Address2')) != ' ':
        if tmp != '':
            tmp = tmp + ', ' + str(getattr(row,'Address2'))
        else:
            tmp = tmp + str(getattr(row,'Address2'))
    if str(getattr(row,'AddressCity')) != 'nan'  and  str(getattr(row,'AddressCity')) != ' ' \
          and tmp != '':
              if tmp != '':
                  tmp = tmp + ', ' + str(getattr(row,'AddressCity'))
              else:
                  tmp = tmp + str(getattr(row,'AddressCity'))
    if str(getattr(row,'State')) != 'nan' and str(getattr(row,'State')) != ' ' \
          and tmp != '':
              if tmp != '':
                  tmp = tmp + ', ' + str(getattr(row,'State'))
              else:
                   tmp = tmp + str(getattr(row,'State'))
    if str(getattr(row,'Zip')) != 'nan' and str(getattr(row,'Zip')) != ' ' \
          and tmp != '':
              if tmp != '':
                  tmp = tmp + ' ' + str(getattr(row,'Zip'))
              else:
                  tmp = tmp + str(getattr(row,'Zip'))
    if str(getattr(row,'Cntry')) != 'nan' and str(getattr(row,'Cntry')) != ' ':
        tmp = tmp + ', ' + str(getattr(row,'Cntry'))
    else:
        if tmp != '' and tmp != ' ':
            tmp = tmp + ', USA'
        else:
            tmp = 'N/A'                               
    active_cbs_addr.set_value(index = row.Index, col = 'Address',value = tmp)              
