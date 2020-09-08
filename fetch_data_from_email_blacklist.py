import cx_Oracle

#dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name') 
#conn = cx_Oracle.connect(user=r'User Name', password='Personal Password', dsn=dsn_tns) 

dsn_tns = cx_Oracle.makedsn('162.70.7.163', '1521', service_name='XXXXXXX.XXX.COM')
conn = cx_Oracle.connect(user='@#@#@', password='@#@$%^%', dsn=dsn_tns)

c = conn.cursor()

c.execute('select * from email_blacklist') 

for row in c:
    print (row[0], '-', row[1], '-', row[2], '-', row[3], '-', row[4]) 
	
conn.close()
