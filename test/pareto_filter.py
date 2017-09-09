from vecvis import API



def test1():
    # Herstellen der Vorbedingungen
    app = API(3)
    app.add_vectors({(1,1,0.6),(0.5,0.5,0.5), (0.4,0.4,0.7), (0.1,0.3,0.3)})
    # Vorgehen
    #
    app.close()


def test2():
    # Herstellen der Vorbedingungen
    app = API(3)
    app.add_vectors({(1,1,1),(0.5,0.5,0.5), (0.4,0.4,0.7), (0.1,0.3,0.3)})
    # Vorgehen
    # Pareto-Filter aktivieren
    app.set_minimizes({0,1,2})
    app.set_minimize(0, False)
    app.close()


def test():
    test1()
    test2()


test()
