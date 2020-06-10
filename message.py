#!/usr/bin/env python3.6


message = input("Enter the message: ")
count = input("Enter the number of times to repeat the message: ").strip()

if count:
    count = int(count)
else:
    count = 1


def messageCounter( message, count):
    counter = 1
    while counter <= count:
         print(f"{message}")
         counter+=1
messageCounter(message, count)




