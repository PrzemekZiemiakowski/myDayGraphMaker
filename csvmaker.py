import csv


class rzeczDan:
    def __init__(self, start, end, day, catego):
        self.start = start
        self.end = end
        self.day = day
        self.category = catego

    def getHours(self):
        return int(self.end) - int(self.start)

    def Giveinfo(self):
        print("start", self.start, " end=", self.end, " day=", self.day, " kategory", self.category)

    def write(self):
        with open('alive.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            tup = (self.start, self.end, self.day, self.category)
            csvwriter.writerow(tup)


kategoria = ["Studia stacjonarnie",
             "Siłownia/Praca ",
             "Jedzenie+gotowanie",
             "Transport",
             "Nauka/programowanie",
             "Przyjaciele/ółki",
             "Dziewczyna",
             "Sen",
             "Muzyka/Dj-ka"]
czasOd = []
czasDo = []
days = []
# ta lista bedzie przechowywac wszystkie posortowane po dniu i godzinie rozpoczecia
summaryArray = []


def listPrinterwithIndex(kategoria):
    for number, kat in enumerate(kategoria):
        print(number, " = ", kat)


def quitChecker(inputcik):
    if inputcik == "quit":
        quit()


def zapytanie(i):
    listPrinterwithIndex(kategoria)
    kat = input("Wybierz kategorie:")
    quitChecker(kat)
    odkiedy = input("Podaj od kiedy:")
    quitChecker(odkiedy)
    czasOd.append(odkiedy)
    dokiedy = input("Podaj od kiedy:")
    czasDo.append(dokiedy)
    day = input("Podaj ktorego dnia:")
    days.append(day)
    summaryArray.append(rzeczDan(odkiedy, dokiedy, day, kat))
    summaryArray[i].write()


def odczyt():
    for obj in summaryArray:
        obj.Giveinfo()
        print(obj.start, " end=", obj.end, " day=", obj.day, " kategory", obj.category)


def podsumowanieby(categoryOfSearch):
    temp = 0
    for obj in summaryArray:
        if obj.category == "1":
            print("imin")
            temp += obj.getHours()
            print("tererere")
            print(obj.getHours())
            print("temp")
            print(temp)
