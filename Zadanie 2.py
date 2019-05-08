
'''
ZADANIE 2.

Podana jest lista zawierająca elementy o wartościach 1-n. Napisz funkcję, która sprawdzi, jakich elementów brakuje:

1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]
'''


def znajdz_brakujace(wejscie, n):

    wyjscie = []

    # Licz od 1 do n. Jeżeli n liczby nie ma na liście 'wejscie' to dodaj ją do listy 'wyjscie'
    for i in range(1, n + 1):
        if i not in wejscie:
            wyjscie.append(i)
    print(wyjscie)


# SET VARIABLES
n = 10
wejscie = [2, 3, 7, 4, 9]

# RUN APP
znajdz_brakujace(wejscie, n)