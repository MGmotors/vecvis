from vecvis import API


def konstruktor():
    # Valid
    app = API(3)
    app.close()
    app = API(9)
    app.close()
    # Warning
    app = API(-1)
    app.close()
    app = API(2)
    app.close()
    app = API("a")
    # Error
    # -
    app.close()

def add_vector():
    app = API(3)
    # Valid
    app.add_vector((0.3, 1.0, 0))
    app.add_vector((-0.3, 1, 0))
    # Warning
    app.add_vector((1,))
    app.add_vector((0.7, 0.2, 0.4, 0.2))
    # Error
    app.add_vector(1)
    app.add_vector(("a", 0.6, 1))
    app.close()

def add_vectors():
    app = API(3)
    # Valid
    app.add_vectors({(0, 0, 1), (1, 1, 0)})
    # Warning
    app.add_vectors({(0, 1)})
    app.add_vectors({(0, 1, 1, 1)})
    # Error
    app.add_vectors({1, 2})
    app.add_vectors({("a", 3, 3)})
    app.close()

def set_names():
    app = API(3)
    # Valid
    app.set_names([None, None, None])
    app.set_names(["0", None, 2])
    app.set_names(["Null"])
    app.set_names([None, 1, "Zwei", "Drei"])
    # Warning
    # Error
    app.set_names(1)
    app.close()

def set_value_ranges():
    app = API(3)
    # Valid
    app.set_value_ranges([(0, 3), (-1, 1), (-3, -2)])
    app.set_value_ranges([None, (-2, 1), None], reset_filters=False)
    app.set_value_ranges([(0,"2")])
    # Warning
    app.set_value_ranges([(1,2,3)])
    # Error
    app.set_value_ranges(1)
    app.set_value_ranges([(1),(0)])
    app.set_value_ranges(["a","b"])
    app.set_value_ranges([("a",1)])
    app.close()

def set_marker_amounts():
    app = API(3)
    # Valid
    app.set_marker_amounts([0,5,4])
    app.set_marker_amounts([None, 4, None])
    app.set_marker_amounts([1.2])
    app.set_marker_amounts([None,None,"2",3])
    # Warning
    # Error
    app.set_marker_amounts(1)
    app.set_marker_amounts(["a", "b"])
    app.close()

def set_minimizes():
    app = API(3)
    # Valid
    app.set_minimizes({0,1,2})
    app.set_minimizes({0})
    app.set_minimizes(set())
    # Warning
    # Error
    app.set_minimizes(1)
    app.set_minimizes({"a", "b"})
    app.close()

def dimensions():
    app = API(3)
    # Valid
    app.set_marker_amount(0, 6)
    app.set_marker_amount(2, 6)
    app.set_minimize(0, True)
    app.set_minimize(2, 4)
    app.set_name(0, "name0")
    app.set_name(2, "name2")
    app.set_value_range(0, (1,2))
    app.set_value_range(2, (1,2))
    # Warning
    # Error
    app.set_marker_amount(-1, 6)
    app.set_marker_amount(3, 6)
    app.set_marker_amount("advs", 8)
    app.set_minimize(-1, True)
    app.set_minimize(3, False)
    app.set_minimize("advs", False)
    app.set_name(-1, "name")
    app.set_name(3, "name")
    app.set_name("advs", "name")
    app.set_value_range(-1, (1,2))
    app.set_value_range(3, (1,2))
    app.set_value_range("advs", (1,2))

    app.close()

def test():
    konstruktor()
    add_vector()
    add_vectors()
    set_names()
    set_value_ranges()
    set_marker_amounts()
    set_minimizes()
    dimensions()

test()
