import sqlite3
conn = sqlite3.connect("db1.db")

#Create the db table
# sql = """
# CREATE TABLE emp(
# id integer primary key autoincrement,
# name varchar(50),
# mob varchar(20),
# city varchar(50)
# )
# """

# #Insert the data
# sql= """
# insert into emp (name,mob,city) values
#  ('Kanishka','7300427924','Chittorgarh'),
#  ('Darshil','8529722466','Udaipur')
#  """

#Read the data

#SQL is not  case sensitive , but the name of the rows and coulmn is case sensitive.

# sql='select *from emp'
# res = conn.execute(sql)

# for row in res:
#     print(row)

#Delete the data
# sql='Delete from emp where id=1'
# conn.execute(sql)
# conn.commit()
# #Again read!!!!
# sql='select * from emp'
# res = conn.execute(sql)

# for row in res:
#     print(row)


#Queries
sql='select * from emp order by id desc limit 1'
res = conn.execute(sql)

for row in res:
    print(row)

conn.close()




