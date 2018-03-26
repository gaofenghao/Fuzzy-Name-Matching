"""
Created on 01/23/2018 03:26 PM

@author: e612495
"""

import string
import numpy as np
import pandas as pd
import difflib
from functools import partial

"""
cdms_curr = pd.read_excel('H:/Client Name Truth/Data/CDMS hierarchy.xlsx')

#remove duplicates 
cdms_curr_clean = cdms_curr.drop_duplicates(['CDMS UP'], keep = 'first')
#remove substring of '(PARENT)'
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('(PARENT)',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('(PARENTS)',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('(PARENT',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('(PARENTS',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('PARENT)',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('PARENTS)',''))
#remove trailing substring of 'CLSD'
for i in range(len(cdms_curr)):
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('CLSD')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - CLSD')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('- CLSD')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('-CLSD')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('CLOSED')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - CLOSED')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('- CLOSED')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('-CLOSED')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos]
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' CLO ')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - IFS')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - SSKC')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - GSAS')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos]
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - WMS')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - SSGM')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - ST SSGM')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - GX')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos]
    if cdms_curr_clean['CDMS UP Name'].values[i] == '-':
         cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:-1]
#strip heading and trailing spaces
    cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i].strip()
    if cdms_curr_clean['CDMS UP Name'].values[i] == '-':
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:-1]
#
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: if x.rfind('CLSD') != -1: x[:x.rfind('CLSD')])
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x[:x.rfind('CLOSD')])
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x[:x.rfind(' - CLOSD')])
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x[:x.rfind('- CLOSD')])
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x[:x.rfind('-CLOSD')])
"""
def stringmatcher(x1, x2):
    s =difflib.SequenceMatcher(isjunk=None,a=x1.lower().strip(),b=x2.lower().strip())
    return s.ratio()
#manual cleaned version of CDMS data

cdms_curr_clean = pd.read_excel('H:/Client Name Truth/Data/CDMS hierarchy cleaned.xlsx')


#load GEMS
GEMS_UNIVERSE = pd.read_excel('H:/Client Name Truth/Data/Copy of FULL_UNIVERSE.xlsx')

cdms_to_gems = cdms_curr_clean
cdms_to_gems = cdms_to_gems.rename(columns = {'CDMS UP':'CDMS CODE','CDMS UP Name':'CDMS NAME'})
cdms_to_gems['GEM ID'] = ''
cdms_to_gems['GEM LEGAL_NAME'] = ''
cdms_to_gems['MATCH QUALITY'] = ''


"""
for j in range(len(cdms_to_gems)):
    print(j)
    gemsid = ''
    gemsnm = ''
    matchq = ''
    cdmsnm =  cdms_curr_clean['CDMS UP Name'].values[j].lower()
    tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['LEGAL_NAME'].str.lower().str.contains(cdmsnm) == True]
    if len(tmp) != 0:
        gemsid = tmp['GEM_ID'].values[0]
        gemsnm = tmp['LEGAL_NAME'].values[0]
        if gemsnm.lower() == cdmsnm.lower():
            matchq = 'EXACT'
        else:
            q =0.0
            qin = 0
            for k in range(len(tmp)):
                if stringmatcher(tmp['LEGAL_NAME'].values[k].lower(),cdmsnm) > q:
                    qin = k
                    q = stringmatcher(tmp['LEGAL_NAME'].values[k].lower(),cdmsnm)
            gemsid = tmp['GEM_ID'].values[qin]
            gemsnm = tmp['LEGAL_NAME'].values[qin]
            matchq = 'PARTIAL - ' + str(int(q*100))       
    else:
         tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['PREVIOUS_NAMES'].str.lower().str.contains(cdmsnm) == True]
         if len(tmp) != 0:
              gemsid = tmp['GEM_ID'].values[0]
              gemsnm = tmp['PREVIOUS_NAMES'].values[0]
              if gemsnm.lower() == cdmsnm.lower():
                  matchq = 'EXACT (with PREVIOUS_NAMES)'
              else:
                  q =0.0
                  qin = 0
                  for k in range(len(tmp)):
                      if stringmatcher(tmp['PREVIOUS_NAMES'].values[k].lower(),cdmsnm) > q:
                          qin = k
                          q = stringmatcher(tmp['PREVIOUS_NAMES'].values[k].lower(),cdmsnm)
                  gemsid = tmp['GEM_ID'].values[qin]
                  gemsnm = tmp['PREVIOUS_NAMES'].values[qin]
                  matchq = 'PARTIAL (PREVIOUS_NAMES) - ' + str(int(q*100))  
         else:
              tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['TRADES_AS_NAMES'].str.lower().str.contains(cdmsnm) == True]
              if len(tmp) != 0:
                  gemsid = tmp['GEM_ID'].values[0]
                  gemsnm = tmp['TRADES_AS_NAMES'].values[0]
                  if gemsnm.lower() == cdmsnm.lower():
                      matchq = 'EXACT (with TRADES_AS_NAMES)'
                  else:
                      q =0.0
                      qin = 0
                      for k in range(len(tmp)):
                          if stringmatcher(tmp['TRADES_AS_NAMES'].values[k].lower(),cdmsnm) > q:
                              qin = k
                              q = stringmatcher(tmp['TRADES_AS_NAMES'].values[k].lower(),cdmsnm)
                      gemsid = tmp['GEM_ID'].values[qin]
                      gemsnm = tmp['TRADES_AS_NAMES'].values[qin]
                      matchq = 'PARTIAL (TRADES_AS_NAMES) - ' + str(int(q*100))  
    
    cdms_to_gems['GEM ID'].values[j] = gemsid
    cdms_to_gems['GEM LEGAL_NAME'].values[j] = gemsnm
    cdms_to_gems['MATCH QUALITY'].values[j] = matchq
    del tmp
"""
for j in range(len(cdms_to_gems)):
    print(j)
    gemsid = ''
    gemsnm = ''
    matchq = ''
    cdmsnm =  cdms_curr_clean['CDMS UP Name'].values[j].lower()
    tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['LEGAL_NAME'].str.lower() == cdmsnm]
    if len(tmp) != 0:
        gemsid = tmp['GEM_ID'].values[0]
        gemsnm = tmp['LEGAL_NAME'].values[0]
        matchq = 'EXACT'
    else:
        tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['PREVIOUS_NAMES'].str.lower() == cdmsnm]
        if len(tmp) != 0:
              gemsid = tmp['GEM_ID'].values[0]
              gemsnm = tmp['PREVIOUS_NAMES'].values[0]
              matchq = 'EXACT (with PREVIOUS_NAMES)'
        else:
              tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['TRADES_AS_NAMES'].str.lower() == cdmsnm]
              if len(tmp) != 0:
                  gemsid = tmp['GEM_ID'].values[0]
                  gemsnm = tmp['TRADES_AS_NAMES'].values[0]
                  matchq = 'EXACT (with TRADES_AS_NAMES)'
              else:
                  #partial match
                  tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['LEGAL_NAME'].apply(partial(stringmatcher,cdmsnm)) > 0.8]
                  if len(tmp) != 0:
                      q =0.0
                      qin = 0
                      for k in range(len(tmp)):
                          if stringmatcher(tmp['LEGAL_NAME'].values[k],cdmsnm) > q:
                              qin = k
                              q = stringmatcher(tmp['LEGAL_NAME'].values[k],cdmsnm)
                      gemsid = tmp['GEM_ID'].values[qin]
                      gemsnm = tmp['LEGAL_NAME'].values[qin]
                      matchq = 'PARTIAL - ' + str(int(q*100)) +'%'
                      
    cdms_to_gems['GEM ID'].values[j] = gemsid
    cdms_to_gems['GEM LEGAL_NAME'].values[j] = gemsnm
    cdms_to_gems['MATCH QUALITY'].values[j] = matchq
    del tmp

#rearrange columns
cdms_to_gems = cdms_to_gems[['CDMS CODE','CDMS NAME','GEM ID','GEM LEGAL_NAME','MATCH QUALITY']]
