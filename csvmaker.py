import csv
class rzeczDan:
    def __init__(self,start,end,day,catego):
        self.start=start
        self.end=end
        self.day=day
        self.category=catego
    def getHours(self,startOf,endOf):
        return self.endOf-self.startOf
    def giveinfo(self):
        print("start",self.start," end=",self.end," day=",self.day," kategory",self.category)

kategoria=["Studia stacjonarnie",
"Siłownia/Praca ",
"Jedzenie+gotowanie",
"Transport",
"Nauka/programowanie",
"Przyjaciele/ółki",
"Dziewczyna",
"Sen",
"Muzyka/Dj-ka"]
czasOd=[]
czasDo=[]
days=[]
# ta lista bedzie przechowywac wszystkie posortowane po dniu i godzinie rozpoczecia
summaryArray=[]

def listPrinterwithIndex(kategoria):
    for number,kat in enumerate(kategoria):
        print(number+1," = ",kat)

listPrinterwithIndex(kategoria)
kat=input("Wybierz kategorie:")
odkiedy=input("Podaj od kiedy:")
czasOd.append(odkiedy)
dokiedy=input("Podaj od kiedy:")
czasDo.append(dokiedy)
day=input("Podaj ktorego dnia:")
days.append(day)
tere=rzeczDan(odkiedy,dokiedy,day,kat)
tere.giveinfo()


