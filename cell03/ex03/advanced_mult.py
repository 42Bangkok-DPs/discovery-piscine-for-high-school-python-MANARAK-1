#!/usr/bin/env python3

i = 0
multiply = 10

while i <= multiply :
  print(f"Table de {i}:", end=" ")
  table = 0

  while table <= multiply :
    print(f"{i * table}", end=" ")
    table += 1
  
  print("")
  i += 1  