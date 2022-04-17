import csv
class
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
summaryArray=[]
def getHours(poczatek,koniec):
    return koniec-poczatek
def listPrinterwithIndex(kategoria):
    for number,kat in enumerate(kategoria):
        print(number+1," = ",kat)
print("Wybierz kategorie:")
listPrinterwithIndex(kategoria)
odkiedy=input("Podaj od kiedy:")
czasOd.append(odkiedy)
dokiedy=input("Podaj od kiedy:")
czasDo.append(dokiedy)
day=input("Podaj ktorego dnia:")
days.append(day)

