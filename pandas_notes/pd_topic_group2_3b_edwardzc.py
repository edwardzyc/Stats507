# ## Name: Ziyin Chen 
# ## email: edwardzc@umich.edu

# # Question 0

# ## Pandas.concat

# ## General Discription
# * Concatenate pandas objects along a particular axis with optional set logic along the other axes.
#
# * Can also add a layer of hierarchical indexing on the concatenation axis, which may be useful if the labels are the same (or overlapping) on the passed axis number.

# ## concat
# * used to combine tow dataframe or combining two series 
#     1. can be used to join two DataFrame or Series with or without similar column with the inclusion of `join = `
#     2. can be used to join two DataFrames either vertially or horizontally with `axis = 1`
#     

# ## Example 1 
# join two dataframe horizontaly and vertially

# +
import pandas as pd 
from IPython.display import display

dic1 = {'Name': ['Allen', 'Bill','Charle','David','Ellen'],
      'number':[1,2,3,4,5],
      'letter':['a','b','c','d','e']}
dic2 = {'A':['a','a','a','a','a'],
       'B':['b','b','b','b','b'],
       'number':[10,11,12,13,14]}
df1 = pd.DataFrame(dic1)
df2 = pd.DataFrame(dic2)
display(df1)
display(df2)
# -


# join vertially 

df = pd.concat([df1,df2])
display(df)

# join horizontally 

df = pd.concat([df1,df2],axis =1 )
display(df)

# # Example 2 
# join with the common column
#

df = pd.concat([df1,df2],join='inner')
display(df)

# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Table Styler](#Table Styler) 


# ## Table Styler
# ### Manipulate many parameters of a table using the table Styler object in pandas. *Xiying Gao*


# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
#
# + [Timestamp class](#Timestamp-class) 
# + [Topic 2 Title](#Topic-2-Title)

# ## Timestamp class
# Name: Name: **Yuelin He**
# UM email: yuelinhe@umich.edu
# 


# Timestamp is Pandas' equivalent (and usually interchangeable) class of 
# python’s Datetime. To construct a Timestamp, there are three calling 
# conventions:
#
# 1. Converting a datetime-like string.
#
# 1. Converting a float representing a Unix epoch in units of seconds.
#
# 1. Converting an int representing a Unix-epoch in units of seconds in a 
# specified timezone.
#
# The form accepts four parameters that can be passed by position or keyword.
#
# There are also forms that mimic the API for datetime.datetime (with year, 
# month, day, etc. passed separately through parameters).
#
# See the following code for corresponding examples:
#

# +
import pandas as pd

## datetime-like string
print(pd.Timestamp('2021-01-01T12'))

## float, in units of seconds
print(pd.Timestamp(889088900.5, unit='s'))

##int, in units of seconds, with specified timezone
print(pd.Timestamp(5201314, unit='s', tz='US/Pacific'))
# -

# In Pandas, there are many useful attributes to do quick countings in Timestamp.
#
# - Counting the day of the...
#     + week: using *day_of_week*, *dayofweek*
#     + year: using *day_of_year*, *dayofyear*
# - Counting the week number of the year: using *week*, *weekofyear*
# - Counting the number of days in that month: using *days_in_month*, *daysinmonth*
#

# +
# Counting the day of the week
ts = pd.Timestamp(2018, 3, 21)
print(ts.day_of_week)
print(ts.dayofweek)

# Counting the day of the year
print(ts.day_of_year)
print(ts.dayofyear)

# Counting the week number of the year
print(ts.week)
print(ts.weekofyear)

# Counting the number of days in that month
print(ts.days_in_month)
print(ts.daysinmonth)
# -

# Whether certain characteristic is true can also be determined.
#
# - Deciding if the date is the start of the...
#     + year: using *is_year_start*
#     + quarter: using *is_quarter_start*
#     + month: using *is_month_start*
# - Similarly, deciding if the date is the end of the...
#     + year: using *is_year_end*
#     + quarter: using *is_quarter_end*
#     + month: using *is_month_end*
# - Deciding if the year is a leap year: using *is_leap_year*

# +
# # Start?
print(pd.Timestamp(2000, 1, 1).is_year_start)
print(pd.Timestamp(2000, 2, 1).is_quarter_start)
print(pd.Timestamp(2000, 3, 1).is_month_start)

# # End?
print(pd.Timestamp(2000, 12, 31).is_year_end)
print(pd.Timestamp(2000, 12, 30).is_quarter_end)
print(pd.Timestamp(2000, 11, 30).is_month_start)

# Leap year?
print(pd.Timestamp(2000, 12, 31).is_leap_year)
print(pd.Timestamp(2001, 12, 30).is_leap_year)
# -

#
# Reference: 
# https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#

