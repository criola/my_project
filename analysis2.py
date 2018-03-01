# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

    #working on oceania data

europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col = 'country')

oceania = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country')

africa = pd.read_csv('data/gapminder_gdp_africa.csv', index_col = 'country')
