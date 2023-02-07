all:
        gcc -I$$(pg_config --includedir-server) -shared -fPIC -o pg_exec.so pg_exec.c
