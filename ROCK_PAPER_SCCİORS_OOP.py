import numpy as np
import math
import random
import time

class rock_paper_scciors():
    def __init__(self):
        self.secim()
        # self.computer()
        # self.person()
    
    def secim(self):
        print("******TAŞ KAĞIT MAKAS OYUNU******")
        while True:
            secim = input("Oyuna girmek için 1 basınız çıkmak için 2 ye basın ?\nCevap: ")
            
            if secim == "1":
                print("Oyuna giriş başarılı...")
                self.rockpaperscciors()
            elif secim == "2":
                print("Oyundan çıkılıyor...")
                self.oyundancik()
                break
            else:
                print("Yanlış bir karakter girdiniz !")
                break
          
    def oyundancik(self):
        while True:    
            print("Oyundan çıkmak istediğinize emin misiniz :)\n"
              "Eğer çıkmak istiyorsanız 1 e basın\n"
              "Eğer çıkmak istemiyorsanız 2 e basın")
            self.cevap = input("Cevap: ")
            if self.cevap == "1":
                break
            elif self.cevap == "2":
                self.secim()
            else:
                self.yanliskarakter()
    def  yanliskarakter(self):
        self.secim()
    
    def rockpaperscciors(self):
        Computer = 0
        Person = 0
        while True:
            elementler = ["taş","kağit","makas"]
            bilgisayar = elementler[random.randint(0,2)]
            kullanici = input("taş , kağit, makas ?\nHangisini seçmek istersiniz ? \nCevap: ")
            if kullanici == bilgisayar:
                print("Berabere kaldiniz..")
            elif kullanici == "taş":
                if bilgisayar == "kağit":
                    Computer +=1
                    print("Kaybettiniz..")
                else:
                    Person +=1
                    print("Kazandınız..")
            elif kullanici == "kağit":
                if bilgisayar == "makas":
                    Computer +=1
                    print("Kaybettiniz..")
                else:
                    Person +=1
                    print("Kazandınız..")
            elif kullanici == "makas":
                if bilgisayar == "taş":
                    Computer +=1
                    print("Kaybettiniz..")
                else:
                    Person +=1
                    print("Kazandınız..")
            else:
                print("Sizin Skorunuz: ",Person)
                print("Computer Skoru: ",Computer)    
                if Person < Computer:
                    print("TAŞ KAĞIT MAKAS OYUNUNU KAYBETTİNİZ...")
                elif Computer < Person:
                    print("TAŞ KAĞIT MAKAS OYUNUNU KAZANDINIZ...") 
                else:
                    print("Berabera kaldınız..")      
                break

if __name__ == "__main__":
    rock_paper_scciors()
    time.sleep(1)
