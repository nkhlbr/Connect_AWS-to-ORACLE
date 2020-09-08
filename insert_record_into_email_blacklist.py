import cx_Oracle

try:  
	dsn_tns = cx_Oracle.makedsn('162.70.7.163', '1521', service_name='XXXX>XXX>XX.COM')
	connection = cx_Oracle.connect(user='appvend', password='appvenddev1', dsn=dsn_tns)         
    #con = cx_Oracle.connect("!#%$^", "E@$@$@", "162.70.7.163:1521/XXX>XXX>XX.COM", encoding="UTF-8")      
    
	cursor = connection.cursor() 
    
	cursor.execute("insert into email_blacklist (EMAIL_AD,EMAIL_AD_UP,BLACKLIST_REASON) values('sfggd1@sd.com','asf.fghfh','testing')")
	
	connection.commit()
	print("value inserted successful") 
	
	#cursor.execute("select * from email_blacklist")	
	#for line in cursor:
	#	print(line)		
  	
	cursor.close()
	connection.close()
	      
	  
except cx_Oracle.DatabaseError as e: 
    print("There is a problem with Oracle", e) 