
'''
ZADANIE 3.
Należy wygenerować listę liczb od 2 do 5.5 ze skokiem co 0.5.
Dane wynikowe muszą być typu decimal.
'''


def count(start, stop, step):

    lista = []

    # Licz od 'start' do 'stop', zapisz do 'lista' i co loopa dodawaj 'step'
    while start <= stop:
        lista.append(start)
        start += step
    print(lista)


# SET VARIABLES
start = 2
stop = 5
step = 0.5

# RUN APP
count(start, stop, step)