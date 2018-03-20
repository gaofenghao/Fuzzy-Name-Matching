# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:22:29 2017

@author: e610086
"""


import string
import numpy as np
import pandas as pd

cdms_matched = pd.read_excel('H:/Client Name Truth/Data/CDMS_TO_GEMS_6850_06_22_2017.xlsx')

tdr_rank_data = pd.read_excel('H:/Client Name Truth/Data/rev_rank_data.xlsx')

tdr_rank_data['GEM ID'] = ''
tdr_rank_data['GEM LEGAL_NAME'] = ''
tdr_rank_data['MATCH QUALITY'] = ''

for i in range(len(tdr_rank_data)):
    print(i)
    tdrnm = tdr_rank_data['CDMS NAME'].values[i].lower().strip()
    for j in range(len(cdms_matched)):
        matchednm = cdms_matched['CDMS NAME'].values[j].lower().strip()
    if tdrnm.find(matchednm) >=0:
        tdr_rank_data['GEM ID'].values[i] = cdms_matched['GEM ID'].values[j]
        tdr_rank_data['GEM LEGAL_NAME'].values[i] = cdms_matched['GEM LEGAL_NAME'].values[j]
        tdr_rank_data['MATCH QUALITY'].values[i] = cdms_matched['MATCH QUALITY'].values[j]
        


