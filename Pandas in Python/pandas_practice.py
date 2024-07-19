'''
1. Pandas store tabular form using a Dataframe
2. A DataFrame is a two-dimensional labelled data structure like a table in databases.
3. Every Dataframe consists of rows and columns, and therefore has both row and column index.
4. Each column can have different type of values.
'''
import pandas as pd

# std_data=[(1,'Varun',30,'male','Chandigarh',172.3),
#           (2,'Arun',34,'male','Delhi',177),
#           ('3','Kokila',58,'female','Kutch',160.5),
#           (4,'Iyyer',35,'male','Chennai',169.4),
#           (5,'Babita',25,'female','Kolkata',190),]
# df=pd.DataFrame(std_data, columns=['seat_no','name','age','gender','city','height(in cm)'])  # dataframe created using list
# print(df)
# print('Columns of above DataFrame is',df.columns)
# print(df.age) # or 
# print(df['age']) # or
# print(df[['age']])
# print(df[['name','age','height(in cm)']]) # double square braket is must, column wise data of name, age, ht.
# print(df.loc[0]) # or 
# print(df.loc[[0]]), # or row wise data of index 0
# print(df.iloc[0]) # or
# print(df.iloc[[0]]) # 2D presentation, row wise data of index 0
# print(df.loc[[0,2,4]]) # double square braket is must, row wise data of index 0,2,4
# print(df.iloc[[1,2,3]]) # double square braket is must, row wise data of index 0,2,4
# print('Total no. of elements (size of DataFrame):',df.size)
# print('Shape of DataFrame:',df.shape)
# print(df.dtypes)
# print(df.values)
# print(df.index)

# df=pd.read_csv('customers-100.csv')  # dataframe created using csv file
# print(df,'\n') #  actual index values will remain as it is for each operations below
# print('*** .head() operations:\n\n',df.head()) # by default shows only top 5 datasets/rows
# print(df.head(16)) # top 16 rows
# print(df.head(160)) # for value more than no. of rows (out of range values) it will not give error and print whole dataset, same for df.tail(160)
# print(df.head(0)) # Empty DataFrame, same for df.tail(160)
# print(df.head(-1),'\n') # prints whole datasets - 1 (from last)
# print('*** .tail() operations:\n\n',df.tail()) # by default shows only last 5 datasets/rows
# print(df.tail(6)) # last 6 rows
# print(df.tail(-2)) # prints whole datasets - 2 (from top)

# data={'Name':['Bhide','Anjali','Sonu'],
#       'Age':[45,30,20],
#       'Salary':[120000,17500,10.5]}
# df=pd.DataFrame(data) # dataframe created using dictionary
# print(df)

# import numpy as np
# data=np.array([[1,'Sodhi',40],[2,'Roshan',35],[3,'Gogi',16]])
# df=pd.DataFrame(data, columns=['Family member','Name','Age']) # dataframe created using Numpy array
# print(df)

std_data=[(1,'Mehtoos',32,'male','Bhopal',177.3),
          (2,'Jethiya',40,'male','Bhuj',170),
          (3,'Champakiya',78,'male','Kutch',170.9),
          (4,'Iyyerdi',38,'male','Chennai',169.4),
          (5,'Babita',25,'female','Kolkata',190)]
df=pd.DataFrame(std_data, columns=['seat_no','name','age','gender','city','height(in cm)'])
print(df['age']>35)
print(df[df['age']>35])
df['block']=['B','B','B','c','C']
df['Soceity']='GokulDham'
df.insert(4,'child',[None,'Tapuda','Jethiya','Pinku','Pinku']) # NOT df=df.insert(....) that will give error
df=df.drop(columns=['age','seat_no']) # or
del df['gender'] # delets only one column at a time
print(df)
df.rename(columns={'child':'child_name'}) # No changes
df=df.rename(columns={'child':'child_name'}) # actual way of renaming
df=df.rename(columns={'something':'anything'}) # will not give any error
print(df)
df=df.drop(2) # deleting row of index value 2
print(df) # actual index value remains same
# df.loc[4]=[2,'Daya',28,'female','Ahmedabad',160] # --> this will give error as after the previous operations the table is changed, a'dd a ro in accordance of new table
df.loc[2]=['Daya','Tapuda','Ahmedabad',166,'A','GokulDham'] # printing at last but index 2
print(df)
df.loc[3, 'child_name']=None # updating values one by one
df.loc[4, 'child_name']=None
print(df)
df.loc[[0,3,4],'child_name']=['Chutanku','Nanhu','Nanhu']
print(df)

# import sqlite3
# conn=sqlite3.connect('University.db')
# query='SELECT * FROM STUDENTS'
# df=pd.read_sql_query(query,conn)  # dataframe using SQL database (NOT Working)
# print(df)
# conn.close()