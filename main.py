import keyboard
import csvmaker

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i = 0
    while True:
        csvmaker.zapytanie(i)

        i = i + 1
        inputcik=input("chcesz skonczyc")
        if(inputcik=="quit"):
            csvmaker.odczyt()
            csvmaker.podsumowanieby(1)
            break
