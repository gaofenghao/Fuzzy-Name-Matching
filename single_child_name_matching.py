"""
Created on 2/5/2018 11:14 AM

@author: e612495
"""

import os
import sys
import string
import numpy as np
import pandas as pd
import difflib
from functools import partial
from fuzzywuzzy import process
import re
import time

from math import *
from decimal import Decimal

def stringmatcher(x1, x2):
    s = difflib.SequenceMatcher(isjunk=None, a=x1, b=x2)
    return s.ratio()

def stringmatcher1(x1, x2):
    x1 = x1.lower()
    x2 = x2.lower()
    s = difflib.SequenceMatcher(isjunk=None, a=x1.split(' '), b=x2.split(' '))
    return s.ratio()

def rm_div(x1):
    return x1.rsplit('-', 1)[0]

def rm_clsd(x1):
    return x1.rsplit('clsd', 1)[0]

def rm_parentheses(x1):
    return re.sub('\(.*?\)', '', str(x1))

sys.stdout.write("Loading workbook ...\n")
sys.stdout.flush()

CDMS = pd.read_excel('H:/CDMS P&Ls Name Matching/DATA/multiple child_non_servicing.xlsx', sheet_name='Sheet1')
KYC = pd.read_excel('H:/CDMS P&Ls Name Matching/DATA/Legal Entity Details_1.xlsx', sheet_name='Sheet1')

# Create a copy of name
CDMS['copy of CDMS Parent Name'] = CDMS['CDMS Parent Name']
CDMS['copy of CDMS Name'] = CDMS['CDMS Name']
KYC['copy of Legal Name'] = KYC['Legal Entity Name']

sys.stdout.write("Name Cleaning ...\n")
sys.stdout.flush()

# Round 1: Soft Cleaning
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].apply(rm_div)
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].apply(rm_clsd)
CDMS['copy of CDMS Name'] = ' ' + CDMS['copy of CDMS Name'].astype(str) + ' '
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.lower()
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('(', '')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(')', '')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(',', '')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('.', '')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('\'', '')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('/', '')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('-', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('&', ' & ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' & ', ' and ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' mgmt ', ' management ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' ltd ', ' limited ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' co ', ' company ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' ins ', ' insurance ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' corp ', ' corporation ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' ag ', ' aktiengesellaschaft ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' inv ', ' investment ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' inc ', ' incorporated ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' fdtn ', ' foundation ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' assoc ', ' association ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' intl ', ' international ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' svsc ', ' service ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' services ', ' service ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' svgs ', ' savings ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' univ ', ' university ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' govt ', ' government ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' assoc ', ' associates ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' the ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('   ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('  ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.strip()

CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].apply(rm_clsd)
CDMS['copy of CDMS Parent Name'] = ' ' + CDMS['copy of CDMS Parent Name'].astype(str) + ' '
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.lower()
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('parent', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('(', '')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(')', '')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(',', '')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('.', '')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('\'', '')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('/', '')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('-', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('&', ' & ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' & ', ' and ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' mgmt ', ' management ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' ltd ', ' limited ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' co ', ' company ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' ins ', ' insurance ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' corp ', ' corporation ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' ag ', ' aktiengesellaschaft ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' inv ', ' investment ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' inc ', ' incorporated ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' fdtn ', ' foundation ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' assoc ', ' association ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' intl ', ' international ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' svgs ', ' savings ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' svsc ', ' service ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' services ', ' service ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' univ ', ' university ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' govt ', ' government ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' assoc ', ' associates ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' the ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('   ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('  ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.strip()

KYC['copy of Legal Name'] = ' ' + KYC['copy of Legal Name'].astype(str) + ' '
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.lower()
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('(', '')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(')', '')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(',', '')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('.', '')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('\'', '')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('/', '')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('-', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('&', ' & ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' & ', ' and ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' mgmt ', ' management ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' ltd ', ' limited ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' co ', ' company ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' ins ', ' insurance ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' corp ', ' corporation ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' ag ', ' aktiengesellaschaft ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' inv ', ' investment ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' inc ', ' incorporated ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' fdtn ', ' foundation ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' assoc ', ' association ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' intl ', ' international ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' svsc ', ' service ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' services ', ' service ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' svgs ', ' savings ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' univ ', ' university ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' svsc ', ' university ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' govt ', ' government ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' assoc ', ' associates ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' the ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('   ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('  ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.strip()

CDMS['GEMS Legal Entity Name'] = ''
CDMS['GEMS_ID'] = ''
CDMS['MATCH QUALITY'] = ''
CDMS['DECISION'] = ''
CDMS['copy of Legal Name'] = ''

CDMS = CDMS.fillna(' ')

KYC_SSGA = KYC[KYC['Product Division'] == "SSGA"]
KYC_SSGM = KYC[(KYC['Product Division'] == "GSNV - Other") | (KYC['Product Division'] == "Global Markets") | (KYC['Product Division'] == "Corporate Management")]
KYC_SSGS = KYC[(KYC['Product Division'] == "Global Services America") | (KYC['Product Division'] == "Global Services International")]
KYC_SSGX = KYC[KYC['Product Division'] == "Global Exchange"]

for j in range(len(CDMS)):
    score = 0.0
    score1 = 0.0
    matchq = 0.0
    decision = ''

    cdms_parent_name = CDMS['copy of CDMS Parent Name'].values[j]
    cdms_child_name = CDMS['copy of CDMS Name'].values[j]

    if CDMS['CALC_DIV'].values[j] == "SSGA":
        tmp = KYC_SSGA['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
        score = max(tmp)
        ind = np.argmax(tmp)
        score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
        matchq = max(score, score1)
        if matchq == 1.0:
            decision = 'PERFECT MATCH'
        else:
            decision = ''

    elif CDMS['CALC_DIV'].values[j] == "SSGS":
        tmp = KYC_SSGS['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
        score = max(tmp)
        ind = np.argmax(tmp)
        score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
        matchq = max(score, score1)
        if matchq == 1.0:
            decision = 'PERFECT MATCH'
        else:
            decision = ''

    elif CDMS['CALC_DIV'].values[j] == "SSGX":
        tmp = KYC_SSGX['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
        score = max(tmp)
        ind = np.argmax(tmp)
        score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
        matchq = max(score, score1)
        if matchq == 1.0:
            decision = 'PERFECT MATCH'
        else:
            decision = ''

    elif CDMS['CALC_DIV'].values[j] == "SSGM":
        tmp = KYC_SSGM['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
        score = max(tmp)
        ind = np.argmax(tmp)
        score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
        matchq = max(score, score1)
        if matchq == 1.0:
            decision = 'PERFECT MATCH'
        else:
            decision = ''

    else:
        CDMS['GEMS_ID'].values[j] = ''
        CDMS['GEMS Legal Entity Name'].values[j] = ''
        CDMS['MATCH QUALITY'].values[j] = ''
        CDMS['copy of Legal Name'].values[j] = ''
        CDMS['DECISION'].values[j] = ''

    CDMS['GEMS_ID'].values[j] = KYC['GEMS ID'].values[ind]
    CDMS['GEMS Legal Entity Name'].values[j] = KYC['Legal Entity Name'].values[ind]
    CDMS['MATCH QUALITY'].values[j] = matchq
    CDMS['DECISION'].values[j] = decision
    CDMS['copy of Legal Name'].values[j] = KYC['copy of Legal Name'].values[ind]

    sys.stdout.write(str(round(j/len(CDMS), 3)*100) + '%\n')
    sys.stdout.flush()

# Round 2: Hard Cleaning
CDMS['copy of CDMS Name'] = ' ' + CDMS['copy of CDMS Name'].astype(str) + ' '
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('-', '')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' llc ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' limited ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' lt ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' lp ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' company ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' companies ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' incorporated ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' managment ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' management ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' aktiengesellaschaft ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' gmbh ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' sa ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' & ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('&', '')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' and ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' pty ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' plc ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' corporation ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' foundation ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' assoc ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' association ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace(' plc ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('   ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.replace('  ', ' ')
CDMS['copy of CDMS Name'] = CDMS['copy of CDMS Name'].str.strip()

CDMS['copy of CDMS Parent Name'] = ' ' + CDMS['copy of CDMS Parent Name'].astype(str) + ' '
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('-', '')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' llc ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' limited ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' lt ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' lp ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' company ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' companies ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' incorporated ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' managment ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' management ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' aktiengesellaschaft ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' gmbh ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' sa ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' & ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('&', '')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' and ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' pty ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' plc ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' corporation ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' foundation ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' assoc ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' association ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace(' plc ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('   ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.replace('  ', ' ')
CDMS['copy of CDMS Parent Name'] = CDMS['copy of CDMS Parent Name'].str.strip()

KYC['copy of Legal Name'] = ' ' + KYC['copy of Legal Name'].astype(str) + ' '
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('-', '')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' llc ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' limited ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' lt ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' lp ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' company ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' companies ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' incorporated ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' managment ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' management ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' aktiengesellaschaft ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' gmbh ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' sa ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' & ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('&', '')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' and ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' pty ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' plc ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' corporation ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' foundation ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' assoc ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' association ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace(' plc ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('   ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.replace('  ', ' ')
KYC['copy of Legal Name'] = KYC['copy of Legal Name'].str.strip()

KYC_SSGA = KYC[KYC['Product Division'] == "SSGA"]
KYC_SSGM = KYC[(KYC['Product Division'] == "GSNV - Other") | (KYC['Product Division'] == "Global Markets") | (KYC['Product Division'] == "Corporate Management")]
KYC_SSGS = KYC[(KYC['Product Division'] == "Global Services America") | (KYC['Product Division'] == "Global Services International")]
KYC_SSGX = KYC[KYC['Product Division'] == "Global Exchange"]

for i in range(len(CDMS)):
    score = 0.0
    score1 = 0.0
    matchq = 0.0
    decision = ''

    cdms_parent_name = CDMS['copy of CDMS Parent Name'].values[i]
    cdms_child_name = CDMS['copy of CDMS Name'].values[i]

    if CDMS['MATCH QUALITY'].values[i] < 1.0:
        if CDMS['CALC_DIV'].values[i] == "SSGA":
            tmp = KYC_SSGA['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
            score = max(tmp)
            ind = np.argmax(tmp)
            score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
            matchq = max(score, score1)
            if matchq == 1.0:
                decision = 'SOFT MATCH'
            else:
                decision = ''

        elif CDMS['CALC_DIV'].values[i] == "SSGS":
            tmp = KYC_SSGS['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
            score = max(tmp)
            ind = np.argmax(tmp)
            score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
            matchq = max(score, score1)
            if matchq == 1.0:
                decision = 'SOFT MATCH'
            else:
                decision = ''

        elif CDMS['CALC_DIV'].values[i] == "SSGX":
            tmp = KYC_SSGX['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
            score = max(tmp)
            ind = np.argmax(tmp)
            score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
            matchq = max(score, score1)
            if matchq == 1.0:
                decision = 'SOFT MATCH'
            else:
                decision = ''

        elif CDMS['CALC_DIV'].values[i] == "SSGM":
            tmp = KYC_SSGM['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
            score = max(tmp)
            ind = np.argmax(tmp)
            score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
            matchq = max(score, score1)
            if matchq == 1.0:
                decision = 'SOFT MATCH'
            else:
                decision = ''

        else:
            CDMS['GEMS_ID'].values[i] = ''
            CDMS['GEMS Legal Entity Name'].values[i] = ''
            CDMS['MATCH QUALITY'].values[i] = ''
            CDMS['copy of Legal Name'].values[i] = ''
            if matchq == 1.0:
                decision = 'SOFT MATCH'
            else:
                decision = ''

        CDMS['GEMS_ID'].values[i] = KYC['GEMS ID'].values[ind]
        CDMS['GEMS Legal Entity Name'].values[i] = KYC['Legal Entity Name'].values[ind]
        CDMS['MATCH QUALITY'].values[i] = matchq
        CDMS['DECISION'].values[i] = decision
        CDMS['copy of Legal Name'].values[i] = KYC['copy of Legal Name'].values[ind]

    else:
        pass

    sys.stdout.write(str(round(i/len(CDMS), 3)*100) + '%\n')
    sys.stdout.flush()

# Round 3: First one/two word(s) matching, giving extra bonus
for n in range(len(CDMS)):
    score = 0.0
    score1 = 0.0
    matchq = 0.0
    decision = ''

    cdms_name = CDMS['CDMS Name'].values[n].split(' ')[0].lower()
    kyc_name = CDMS['GEMS Legal Entity Name'].values[n].split(' ')[0].lower()

    cdms_name1 = CDMS['CDMS Name'].values[n].split(' ')[1].lower()
    try:
        kyc_name1 = CDMS['GEMS Legal Entity Name'].values[n].split(' ')[1].lower()
    except:
        kyc_name1 = ' '


    if CDMS['MATCH QUALITY'].values[n] < 1.0:
        matchq = stringmatcher(CDMS['copy of CDMS Name'].values[n], CDMS['copy of Legal Name'].values[n])
        if matchq > CDMS['MATCH QUALITY'].values[n]:
            CDMS['MATCH QUALITY'].values[n] = matchq
    else:
        pass

    if CDMS['MATCH QUALITY'].values[n] < 1.0 and (cdms_name == kyc_name and cdms_name1 == kyc_name1):
        CDMS['MATCH QUALITY'].values[n] = CDMS['MATCH QUALITY'].values[n] * 1.15
    if CDMS['MATCH QUALITY'].values[n] < 1.0 and (cdms_name == kyc_name):
        CDMS['MATCH QUALITY'].values[n] = CDMS['MATCH QUALITY'].values[n] * 1.1
    else:
        pass

    sys.stdout.write(str(round(n/len(CDMS), 3)*100) + '%\n')
    sys.stdout.flush()

# Round 4: Matching with whole KYC poll
for l in range(len(CDMS)):
    score = 0.0
    score1 = 0.0
    matchq = 0.0
    decision = ''

    cdms_child_name = CDMS['copy of CDMS Name'].values[l]

    if CDMS['MATCH QUALITY'].values[l] < 1.0:
        tmp = KYC['copy of Legal Name'].apply(partial(stringmatcher1, cdms_child_name))
        score = max(tmp)
        ind = np.argmax(tmp)
        score1 = stringmatcher1(cdms_parent_name, KYC['copy of Legal Name'].values[ind])
        matchq = max(score, score1)

        if matchq > CDMS['MATCH QUALITY'].values[l]:
            CDMS['GEMS_ID'].values[l] = KYC['GEMS ID'].values[ind]
            CDMS['GEMS Legal Entity Name'].values[l] = KYC['Legal Entity Name'].values[ind]
            CDMS['MATCH QUALITY'].values[l] = matchq
            CDMS['copy of Legal Name'].values[l] = KYC['copy of Legal Name'].values[ind]
            if matchq == 1.0:
                decision = 'PERFECT MATCH FROM ' + KYC['Product Division'].values[l]
            elif matchq > 0.9:
                decision = 'HIGHLY MATCH FROM ' + KYC['Product Division'].values[l]
            else:
                decision = ''
            CDMS['DECISION'].values[l] = decision
        else:
            pass

        sys.stdout.write(str(round(l / len(CDMS), 3) * 100) + '%\n')
        sys.stdout.flush()

CDMS.loc[(CDMS['MATCH QUALITY'] > 1.0), ['MATCH QUALITY']] = 1.0
CDMS.loc[(CDMS['MATCH QUALITY'] < 0.50), ['GEMS_ID', 'GEMS Legal Entity Name']] = ''

for m in range (len(CDMS)):
    if CDMS['MATCH QUALITY'].values[m] > 0.9 and CDMS['DECISION'].values[m] == '':
        CDMS['DECISION'].values[m] = 'HIGHLY MATCH'

sys.stdout.write("Saving File ...\n")
sys.stdout.flush()
CDMS.to_excel('H:/CDMS P&Ls Name Matching/Output/output_Non_servicing_' + str(time.time()) + '.xlsx',
              sheet_name='Sheet1', index=False)

sys.stdout.write("Done!")
sys.stdout.flush()