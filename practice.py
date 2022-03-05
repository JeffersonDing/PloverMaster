import serial
import random
import sys
from art import *
import os


def read(ser):
    while True:
        s = ser.read(size=6)
        if(s):
            return(s.hex())


def register_map(ser):
    keys = ["S_left_1","T_left","P_left","H","*_1","F","P_right","L","T_right","D","S_left_2","K","W","R_left","*_2","R_right","B","G","S_right","Z","A","O","E","U"]
    key_map = {}
    for key in keys:
        print(key)
        key_map[key] = read(ser)
        print(key_map)

def practice(ser):
    key_map = {'S_left_1': '804000000000', 'T_left': '801000000000', 'P_left': '800400000000', 'H': '800100000000', '*_1': '800008000000', 'F': '800000020000', 'P_right': '800000004000', 'L': '800000001000', 'T_right': '800000000400', 'D': '800000000100', 'S_left_2': '802000000000', 'K': '800800000000', 'W': '800200000000', 'R_left': '800040000000', '*_2': '800004000000', 'R_right': '800000010000', 'B': '800000002000', 'G': '800000000800', 'S_right': '800000000200', 'Z': '800000000001', 'A': '800020000000', 'O': '800010000000', 'E': '800000080000', 'U': '800000040000'}   
    while True:
        rand = random.choice(list(key_map.keys()))
        tprint(rand)
        while(not key_map[rand] == read(ser)):
            print("Incorrect!")
        print("Correct!")
        clearConsole();

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


if __name__ == "__main__":
    try:
        ser = serial.Serial('/dev/tty.usbmodem03', 9600, timeout=0.5)
        # print(ser.name)
        # register_map(ser)
        practice(ser)
    except KeyboardInterrupt:
        print("Ending")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
