# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:46:35 2017

@author: e610086
"""

import string
import numpy as np
import pandas as pd

client_name = input('Input Clien Name')
client_name = client_name.lower()

full_universe = pd.read_csv('C:/Users/e610086/Desktop/Name_match/FULL_UNIVERSE.csv')
CBS_client = pd.read_excel('C:/Users/e610086/Desktop/Name_match/CBS_address_from_CBS_Mark.xlsx')
badger_funds = pd.read_excel('C:/Users/e610086/Desktop/Name_match/badger_funds_2017_0522.xlsx')
