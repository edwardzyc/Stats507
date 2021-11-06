# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Q3 

# ### a

# first we need to import the data, and determine the path 

import pandas as pd 
pathG=r'C:\Users\chen3\Desktop\Academic\Umich\Y2S1\STATS 507\Homework\Homework II\Data\DEMO_G.XPT'
pathH=r'C:\Users\chen3\Desktop\Academic\Umich\Y2S1\STATS 507\Homework\Homework II\Data\DEMO_H.XPT'
pathI=r'C:\Users\chen3\Desktop\Academic\Umich\Y2S1\STATS 507\Homework\Homework II\Data\DEMO_I.XPT'
pathJ=r'C:\Users\chen3\Desktop\Academic\Umich\Y2S1\STATS 507\Homework\Homework II\Data\DEMO_J.XPT'

# +
columns_to_keep=['SEQN','RIDAGEYR','RIAGENDR','RIDRETH3','DMDEDUC2','DMDMARTL',
                 'RIDSTATR','SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']
dfG = pd.read_sas(pathG)
dfG=dfG[columns_to_keep]
dfH = pd.read_sas(pathH)
dfH=dfH[columns_to_keep]
dfI = pd.read_sas(pathI)
dfI=dfI[columns_to_keep]
dfJ = pd.read_sas(pathJ)
dfJ=dfJ[columns_to_keep]

df1=pd.concat([dfG,dfH,dfI,dfJ],
              keys=['2011-2012','2013-2014',
                    '2015-2016','2017-2018'])
df1=df1.reset_index()
#print(df1.columns)
df1=df1.drop(columns=['level_1'])
df1=df1.rename(columns={'level_0':'cohort'})
# -

# then we can change the columns names 

df1=df1.rename(columns={'SEQN':'sequence number',
                        'RIDAGEYR':'age',
                        'RIDRETH3':'race and ethnicity',
                        'DMDEDUC2':'education',
                        'DMDMARTL':'marital status',
                        'RIDSTATR':'Interview and examination status'.lower(),
                        'SDMVPSU':'masked variance unit pseudo-PSU variable'.lower(),
                        'SDMVSTRA':'Masked variance unit pseudo-stratum variable'.lower(),
                        'WTMEC2YR':'Full sample 2 year MEC exam weight'.lower(),
                        'WTINT2YR':'Full sample 2 year interview weight'.lower()})



# +
df1['gender'] = pd.Categorical(df1['gender'].replace({1:'Male',
                                                                   2:'Female'}))
                                                                   

df1['race and ethnicity'] = pd.Categorical(df1['race and ethnicity'].replace({1:'Mexican American',
                                                                   2:'Other Hispanic',
                                                                   3: 'Non-Hispanic White',
                                                                   4: 'Non-Hispanic Black',
                                                                   5: 'Other Race - Including Multi-Racial'}))
df1['marital status'] = pd.Categorical(df1['marital status'].replace({1:'Married',
                                                                           2: 'Widowed',
                                                                           3: 'Divorced',
                                                                           4: 'Separated',
                                                                           5: 'Never married',
                                                                           6: 'Living with partner',
                                                                           77: 'Refused',
                                                                           99: 'Dont know'}))
df1['interview and examination status'] = pd.Categorical(df1['interview and examination status']. replace({1: 'Interview only',
                                                                                                          2: 'Both interview and MEC examined'}))



# -


display(df1)

# then we can change it into other format 

df1.to_pickle('df1_pickle.pickle')

print('there are a total of {} cases in the table'.format(df1.shape[0]))

# There are a total of 39156 cases in the first part 

# # b

# just like before we need the path first and then we need to work on the columns to keep 

pathDG=r'C:\Users\chen3\Desktop\Academic\Umich\Y2S1\STATS 507\Homework\Homework II\Data\OHXDEN_G.XPT'
pathDH=r'C:\Users\chen3\Desktop\Academic\Umich\Y2S1\STATS 507\Homework\Homework II\Data\OHXDEN_H.XPT'
pathDI=r'C:\Users\chen3\Desktop\Academic\Umich\Y2S1\STATS 507\Homework\Homework II\Data\OHXDEN_I.XPT'
pathDJ=r'C:\Users\chen3\Desktop\Academic\Umich\Y2S1\STATS 507\Homework\Homework II\Data\OHXDEN_J.XPT'

columns_to_keep_den = ['SEQN','OHDDESTS']
for i in range(1,33):
    columns_to_keep_den.append('OHX{:02d}TC'.format(i))
for i in range(2,16):    
    columns_to_keep_den.append('OHX{:02d}CTC'.format(i))
for i in range(18,32):    
    columns_to_keep_den.append('OHX{:02d}CTC'.format(i))


# we have the columns to keep then we will be able to clean the data 
# and then connect all four sheets to create the whole table 

# +
dfG = pd.read_sas(pathDG)
dfG=dfG[columns_to_keep_den]
dfH = pd.read_sas(pathDH)
dfH=dfH[columns_to_keep_den]
dfI = pd.read_sas(pathDI)
dfI=dfI[columns_to_keep_den]
dfJ = pd.read_sas(pathDJ)
dfJ=dfJ[columns_to_keep_den]

df2=pd.concat([dfG,dfH,dfI,dfJ],
              keys=['2011-2012','2013-2014',
                    '2015-2016','2017-2018'])
df2=df2.reset_index()
df2=df2.drop(columns=['level_1'])
df2=df2.rename(columns={'level_0':'cohort'})

# now we can change the variables names into more literate ones 

namechange_dic={'SEQN':'sequence number',
                'OHDDESTS': 'Dentition Status Code'.lower()}
for i in range(1,33):    
    namechange_dic['OHX{:02d}TC'.format(i)] \
        = 'tooth count: # {:02d}'.format(i)
for i in range(2,15):    
    namechange_dic['OHX{:02d}CTC'.format(i)] \
        ='Coronal Carries: tooth count  # {:02d}'.format(i).lower()
for i in range(18,32):    
    namechange_dic['OHX{:02d}CTC'.format(i)] \
        ='Coronal Carries: tooth count  # {:02d}'.format(i).lower()
df2=df2.rename(columns=(namechange_dic))
# -

# then we will need to change the data type 

# +
df2['Dentition Status Code'.lower()] = pd.Categorical(df2['Dentition Status Code'.lower()].replace({1: 'Complete',
                                                                                                   2: 'Partial',
                                                                                                   3: 'Not Done'}))

for i in range(1,33):
    df2['tooth count: # {:02d}'.format(i)] = pd.Categorical(df2['tooth count: # {:02d}'.format(i)].replace({1:'Primary tooth (deciduous) present',
                                                                                                2:'Permanent tooth present',
                                                                                                3: 'Dental implant',
                                                                                                4: 'Tooth not present',
                                                                                                5:'Permanent dental root fragment present',
                                                                                                 9: 'Could not assess',
                                                                                                6: 'Could not assess'}))

for i in range(2,15):
    df2['coronal carries: tooth count  # {:02d}'.format(i)] = df2['coronal carries: tooth count  # {:02d}'.format(i)].astype('category')
    
for i in range(18,32):
    df2['coronal carries: tooth count  # {:02d}'.format(i)] = df2['coronal carries: tooth count  # {:02d}'.format(i)].astype('category')
    
    
df2['coronal carries: tooth count  # 31'] = df2['coronal carries: tooth count  # 31'].astype('category')
print(df2.dtypes)
display(df2)  
# -

# then we will be able to other format

df2.to_pickle('df1_pickle.pickle')

print('there are a total of {} cases in the table'.format(df2.shape[0]))

# There are a total of 35909 cases in the second part 

