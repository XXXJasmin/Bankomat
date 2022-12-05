#!/usr/bin/env python3
from sys import stdout, stderr


class Bankomat:
    
    trezor = {}
    def __init__(self, trezorfile):
            self.trezor = {}
            self.trezorfile=trezorfile

    def read(self):
        with open(self.trezorfile, 'r') as f:
            while True:
                line= f.readline()
                if line=='':
                    break
                bill, count = line.split()
                self.trezor [int(bill)] = int(count)
        self.bills=sorted(self.trezor.keys(), reverse=True)
        return True 

    def write(self):
        with open(self.trezorfile, 'w') as f:
            for key in self.trezor:
                f.write (f"{key:7} {self.trezor[key]:7}\n")
        return True 

    def make(self, amount):
        slovnik = {}
        max_cislo = 0
        automat = int(input("Zadejte Vaši částku, prosím : "))

        with open("trezor.txt", "r") as t:
            for cisla in t.readlines():
                cisla = cisla.strip()
                cisla = cisla.split()
                slovnik.update({int(cisla[0]) : int(cisla[1])})

        for key in slovnik.keys():
            max_cislo += slovnik[key] * key

        if automat > max_cislo:
            print("V tomto zařízení se nenachází zadaná hodnota peněz.")
        else:
            exit()

        for key in slovnik.keys():
            if automat // key != 0:
                pocet = automat // key
                if pocet <= slovnik[key]:
                    automat -= pocet * key
                    slovnik.update({key : slovnik[key] - pocet})
                    print("Výběr částky: ", key,"Kč ", pocet, " krát")
                else:
                    pocet = slovnik[key]
                    automat -= pocet * key
                    slovnik.update({key : slovnik[key] - slovnik[key]})
                    print("Výběr částky: ", key,"Kč ", pocet, " krát")

        with open("trezor.txt", "w") as t:
            for key,value in slovnik.items():  
                t.write(f"{key}   {slovnik[key]}\n")
        
        return True or False


if __name__ == "__main__":
    bankomat = Bankomat('trezor.txt')
    
    
    try:
        line = input("bankomat >> ")
        number = int(line)
        bankomat.read()
        bankomat.make(number)
        bankomat.write()
    except EOFError:
        exit(0)
    except KeyboardInterrupt:
        stderr.write("Program byl přerušen z klávecnice.")
        exit(1)
    except ValueError:
        stdout.write("ERROR\n")
