import csv
from random import choice, randint


def read_csv(path):
    # FIXME
    return [('Model', ['A', ]), ('Wynik', [17, ]), ('Czas', [465, ])]

def write_to_csv(path, columns):
    # TODO: uzycie biblioteki csv albo path
    # TODO 2: sprawdzic czy sciezka istnieje lub czy plik istnieje
    plik = open(path + 'Dane.csv', 'w')
    plik.write('Model; Wynik; Czas;\n')
    model = choice(['A', 'B', 'C'])
    wynik = randint(0, 1000)
    czas = randint(0, 1000)
    plik.write(model + '; ' + str(wynik) + '; ' + str(czas) + '\n')
    plik.close()
    return