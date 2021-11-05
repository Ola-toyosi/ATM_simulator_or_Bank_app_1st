import sqlite3

conn = sqlite3.connect('piggybank.db')
cursor = conn.cursor()

# stmt = 'create table Customers(customer_code int(4) primary key, last_name varchar(15) , first_name varchar(15) ,
# middle_name varchar(15), address varchar(35), email varchar(20), dob varchar(15), nok varchar(15), gender varchar(
# 15), pin int(4) )'
# cursor.execute(stmt)

# stmt = "insert into Customers(customer_code, last_name, first_name, middle_name, address, email, dob, nok, gender, pin) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
# values = [(1021, 'ubah', 'samuel', 'kelechi', '5 rufus idera ikorodu bus stop lagos', 'ubahsamuel78@gmail.com', '2000-08-07', 'ubah mary', 'm', 1111),
#           (1022, 'ubah', 'mary', 'jane', '5 rufus idera ikorodu bus stop lagos', 'samavel@yahoo.com', '1975-09-04', 'ubah alloy', 'f', 2222),
#         (1023, 'yusuf', 'george', 'taiwo', '45 old school ikorodu bus stop lagos', 'taiwo78@gmail.com', '1993-10-21', 'yusuf jacob', 'm', 3333)]
# cursor.executemany(stmt, values)

# stmt = 'create table customers_account(customer_code int(4) primary key, account_name varchar(30),
# account_type varchar(10), account_balance varchar(50), accountNo INTEGER(10))'
# cursor.execute(stmt)

# stmt = "insert into customers_account(customer_code, account_name, account_type, account_balance) values(?, ?, ?, ?)"
# values = [(1021, 'ubah samuel', 'savings', 20000000, 1100977824), (1022, 'ubah mary', 'current', 35000000, 1100977982),
# (1023, 'yusuf george', 'current', 15000000, 1100977765)]
# cursor.executemany(stmt, values)

# stmt = 'create table Trxn(trxn_id int(4) primary key, accountNo int(10), amount varchar(50), working_bal int(50),' \
#        ' trxn_date datetime(70) )'
# cursor.execute(stmt)


conn.commit()
conn.close()
