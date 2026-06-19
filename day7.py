import pandas as pd
# data = [10,20,30,40]

# ps = pd.Series(data , index=['a','b','c','d'], dtype = 'float' , name = "Integer Series")
# print(ps)
# print(type(ps))

# data2={
#     "Sub":["Phy","Chem","C++"],
#     "Marks" :[20,40,50]
# }

# ps=pd.DataFrame(data2)
# print(ps)
# print(type(ps))
# print(pd.__version__)


# data_3 = [10,20,30,40]
# ps = pd.Series(data_3 , index=['a','b','c','d'], dtype = 'float' , name = "Integer Series")
# print(ps['c'])

# data4={'day1':[400,500],"day2":450}
# df=pd.Series(data4)
# print(df)

# res=df.tolist()
# print(res,type(res))

# data5={
#     "Marks":[24,36,70],
#     "duration":[12,50,60]
# }
# df=pd.DataFrame(data5,index=[1,2,3])
# #Single vs Double Brackets
# #Single===Series will be printed
# print(df.loc[[1]])     #Double brackets taki df k dono columns print ho 

# print(df.loc[[1,3,2]])      #Order specify kr raha h 

# data6={
#     "Marks":[24,36,70],
#     "duration":[12,50,60]
# }
# df =pd.DataFrame(data6)
# print(df)
# df.index=['d1','d2','d3']
# res = df.columns
# print(res)

# df.columns = ['s1','s2']
# print(df)

#SLicing...............DOUBT

# df3= pd.DataFrame([['a','b'],['c','d'],['e','f'],['g','h']], columns=['col1','col2'])
# print(df3)
# df3.index=['r1','r2','r3','r4']
# res= df3.loc['r1':'r4', 'col1':'col3']
# print(res)


#DROP
# df=pd.DataFrame([1,2,3,4,5,6], columns=['r1'])
# print(df)
# res=df.drop('r1')
# print(df)