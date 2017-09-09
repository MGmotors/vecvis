# encoding: utf-8
"""
Modul um die Testfälle für die Filter auszuführen.
Testen am Besten in einer IDE und setzen von Brakpoints
an den Stellen wo das Ergebnis überprüft werden muss.
"""
import random
from vecvis import API


def testfall1():
    # Vorbedingungen herstellen
    app = API(3)
    vectors = create_random_vectors(10, 3)
    app.add_vectors(vectors)
    # Ausfuehrung
    # Checken des Ergebnis
    app.close()


def testfall2():
    # Vorbedingungen herstellen
    app = API(3)
    vectors = create_random_vectors(10, 3)
    app.add_vectors(vectors)
    # Ausfuehrung
    # Checken des Ergebnis
    app.close()


def testfall3():
    # Vorbedingungen herstellen
    app = API(3, value_ranges=[(0, 1), (0, 2), (0, 2)])
    vectors = create_random_vectors(10, 3, max_value=2)
    app.add_vectors(vectors)
    # Ausfuehrung a
    app.set_value_range(0, (0, 2))
    # Ausfuehrung b
    app.set_value_range(0, (0, 1), reset_filter=False)
    # Ausfuehrung c
    app.set_value_range(0, (0, 2), reset_filter=False)
    # Ausfuehrung d
    app.set_value_range(0, (1, 2), reset_filter=False)
    # Ausfuehrung e
    app.set_value_range(0, (-1, 2), reset_filter=False)
    app.close()

def testfall4():
    # Vorbedingungen herstellen
    app = API(3)
    vectors = create_random_vectors(10, 3)
    app.add_vectors(vectors)
    # Ausfuehrung
    # Checken des Ergebnis
    app.close()

def create_random_vectors(how_many, dimensions, min_value=0, max_value=1):
    vectors = set()
    while len(vectors) < how_many:
        nvalue = random.randint(0, 1000) / 1000
        value = (max_value - min_value) * nvalue + min_value
        vector = (value,)
        while len(vector) < dimensions:
            nvalue = random.randint(0, 1000) / 1000
            value = (max_value - min_value) * nvalue + min_value
            vector = vector + (value,)
        vectors.add(vector)
    return vectors

def run_tests():
    testfall1()
    testfall2()
    testfall3()
    testfall4()

run_tests()
