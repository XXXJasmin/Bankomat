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
                self.trezor[int(bill)] = int(count)
        self.bills=sorted(self.trezor.keys(), reverse=True)
        return True 

    def write(self):
        with open(self.trezorfile, 'w') as f:
            for key in self.trezor:
                f.write (f"{key:7} {self.trezor[key]:7}\n")
        return True 

    def make(self, castka):
        max_cislo = 0
        automat = int(castka)

        

        for key in self.trezor.keys():
            max_cislo += self.trezor[key] * key

        if automat > max_cislo:
            print("V tomto zařízení se nenachází zadaná hodnota peněz.")
            exit()

        vysledek = ''
        for key in self.trezor.keys():
            if automat // key != 0:
                pocet = automat // key
                if pocet <= self.trezor[key]:
                    automat -= pocet * key
                    self.trezor.update({key : self.trezor[key] - pocet})
                    vysledek += f"Výběr částky: {key} Kč {pocet} krát\n" 
                else:
                    pocet = self.trezor[key]
                    automat -= pocet * key
                    self.trezor.update({key : self.trezor[key] - self.trezor[key]})
                    vysledek += f"Výběr částky: {key} Kč {pocet} krát\n"
                
        return vysledek


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
