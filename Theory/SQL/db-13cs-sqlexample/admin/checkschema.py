'''
this program allows you to inspect a table in a schema to see the names of the columsn, theri datatype etc
'''

import sqlite3

# define connection to database and establish a cursor for accessing data
connection = sqlite3.connect("myDatabase.db")
cursor = connection.cursor()

# dict for table def
tabledef = {	
}

# dict for field/column def 
fielddef = {
	"colid": 0,
	"colname": "",
	"coldatatype": "",
	"colnotnull": 0,
	"coldefault": "",
	"colpk": 0
}


def tbldeftodict(tbldetails):
	
	studenttbl = cursor.execute(tbldetails).fetchall()

	for col in studenttbl:
		print("***",col,type(col))
	#end for

	# assign to dict from tuple schema details
	columns = 0
	
	for tuple in studenttbl:
		
		fielddef["colid"] = tuple[0]
		fielddef["colname"] = tuple[1]
		fielddef["coldatatype"] = tuple[2]
		fielddef["colnotnull"] = tuple[3]
		fielddef["coldefault"] = tuple[4]
		fielddef["colpk"] = tuple[5]
		
		tabledef[columns] = fielddef
		columns = columns + 1
	
	#end for
	
	return tabledef

#end def

# main starst here
while True:

	tbl = input("Enter table name or <enter> to finish: ")
	if tbl == "":
		break
	else:
		command = "PRAGMA table_info('"+tbl+"');"
		tbldetails = cursor.execute(command).fetchall()
		#print(tbldetails)
		
		print(f'{"ColId":^5}|{"ColName":^15}|{"DataType":^15}|{"Null":^5}|{"Default":^7}|{"PK":^5}')
		
		for col in tbldetails:
			print(f"{col[0]:^5}|{col[1]:^15}|{col[2]:^15}|{col[3]:^5}|{col[4]}|{col[5]^5}")
		
		#end for

	#end if

#end while

connection.close()
