from pprint import pprint

'''
ZADANIE 1.
Napisz generator kodów pocztowych, który przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi.
'''


def gen_kod(kod1, kod2):

    # Funkcja dodająca zera do kodu pocztowego tak aby jego druga część po myślniku składała się z 3 cyfr
    # oraz dodaje całe kody do je do listy w formacie string
    def dodaj_zera(n):

        if len(str(n)) == 1:
            n = '00' + str(n)
        elif len(str(n)) == 2:
            n = '0' + str(n)
        lista_kodow.append(str(i) + '-' + str(n))

    # Przygotuj liste
    lista_kodow = []

    # Podziel kody pocztowe na dwie części w miejscu myślnika
    start0 = kod1.split('-')[0]
    start1 = kod1.split('-')[1]
    stop0 = kod2.split('-')[0]
    stop1 = kod2.split('-')[1]

    # Główna funkcja generująca kody pocztowe pomiędzy podanymi dwoma
    # Pierwszy loop wyszukuje liczbe z pierwszego człony kodu pocztowego
    for i in range(int(start0), int(stop0) + 1):

        # jeżeli jest to pierwsza liczba pierwszego kodu pocztowego to licz od liczby po myslniku do 1000
        if i == int(start0):
            for n in range(int(start1) + 1, 1000):
                dodaj_zera(n)

        # Jeżeli jest to pierwsza liczba drugiego kodu pocztowego to licz od zera do liczby po myślniku
        elif i == int(stop0):
            for n in range(0, int(stop1)):
                dodaj_zera(n)

        # Jeżeli nie jest to pierwsza liczba pierwszego ani drugiego kodu pocztowego to po myślniku wypisz
        # liczby od 0 do 1000
        else:
            for n in range(0, 1000):
                dodaj_zera(n)

    pprint(lista_kodow)


# SET VARIABLES
kod1 = '79-008'
kod2 = '80-100'

#RUN APP
gen_kod(kod1, kod2)
