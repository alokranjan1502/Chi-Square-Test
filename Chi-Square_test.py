# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:03:07 2019

@author: Alok
"""

#Chi-Square Test

# Chi-Square test is used to find association between two categorial
# variables. It is similar to correlation.
# Chi-square will be measured by below formula
# x-square = sum(observed-expected)^2/expected)
# Value of x-square will be compared with x-square critical value which
# comes from chi-square table(predefined table)
# Chi-Square test assumptions
# H0: there is no association between given variables
# H1: there is association between given variables

# you can decide acceptance of H0 based on either pvalue or
# x-square critical value
# if pvalue>=0.05 or x-square > x-square critical then accept H0
# else reject H0.
# rejection of H0 means you have to accept H1

# degree of freedom (df) = (r-1)*(c-1)
# expected value = (RT*CT)/Total
# r = row number, c=column number
# RT = row total , CT = column total , total=total observation

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

data=pd.read_table("D:/Python/Python Class notes/Part 2/Class 10/Hair_Eye_Color.txt",
                   
                   header=0,delim_whitespace=True)
print(data)

data.shape


cont_table=pd.pivot_table(data,values=['n'],
                          index=['Hair'],columns=['Eye'],
                          aggfunc=np.sum)
print(cont_table)

# replace missing value with zero

cont_table2=cont_table.replace(np.nan,0)

xsq,pvalue,dof,expected=chi2_contingency(cont_table2)

print(xsq)  # 20.92
print(pvalue) # 0.007
print(dof)   # 8
print(expected)
(6.0+51.0+69.0+68.0+28.0)*(51.0+94+37)/np.sum(data['n'])
# As p-value is below 0.05, so we reject H0 and accept H1.
# these is association between Hair and Eye color.

# second use of chi-square test
# it is also used for goodness of fit test.
# goodness of fit test is used to compare a given sample with 
# expected values.

# A company higher management want to open gym for their employee,
# so that their employee should be health.
# Second level management think that expected_data=[.30,.30,.40]
# 30% want to go to gym, 30% using some gym, 40% - say not needed

sample_data=[75,105,120]
sample_per=sample_data/np.sum(sample_data)
expected_data=[.30,.30,.40]
from scipy.stats import chisquare

#H0: Sample data is consistent with expected data
#H1: Sample data is not consistent with expected data
#accept H0 when pvalue is greater than 0.05

xsq,pvalue=chisquare(f_obs=sample_per,f_exp=expected_data)

print(xsq)
print(pvalue)

# as p-value=0.992 > 0.05, we accept H0.
#so we accept sample data, as sample is consistent with expected_data

# degress of freedom = n-1 (3-1=2)
