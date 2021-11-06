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