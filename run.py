# -*- coding: utf-8 -*-
""" Showoff module for the app
"""
from random import randint
from vecvis import API


def hotel_example():
    """ Which Hotel do you choose?
    """
    names = ["Stars", "Distance to the sea", "Price per night"]
    min_better = {1, 2}
    value_ranges = [(0, 5, 1), (10, 1000), (50, 100)]
    app = API(3, names=names, minimize=min_better, value_ranges=value_ranges)
    """
    for i in range(0, 3):
        app.set_dimension_name(i, names[i])
        app.set_dimension_value_range(i, value_ranges[i][0], value_ranges[i][1])
        app.set_dimension_minimize(i, min_better[i])
    """
    app.add_vectors([(3, 500, 70), (3, 400, 60), (5, 300, 100)])
    app.set_marker_amount(0, 4)


def simple_example():
    """doc
    """
    # Initialize with 5 axes
    app = API(5)
    # add some vectors
    app.add_vectors({(1, 0.3, 1.0, 0.5, 0.7),
                     (0.53, 0.32, 0.51, 0.14, 0.28),
                     (0.66, 0.81, 0.28, 0.17, 0.8)})


def startup_conf_examle():
    """doc"""
    names = ["One", None, "Three"]
    minimize_dimensions = {3, 2}
    value_ranges = [None, (0, 10), (-100, 0), (1, 1.5)]
    app = API(4, names=names, minimize=minimize_dimensions,
              value_ranges=value_ranges, num_markers=[None, 9])
    app.add_vectors({(1,3,-10,1.25),(0,0,-50,1.3),(1,1,-75.89,1.26)})


def later_conf_example():
    """ dooc """
    app = API(3)
    app.add_vector((78,2,9))
    app.set_names(["One", "toow", "Three"])
    app.add_vectors({(50,20,64),(0,32,80),(2,-10,45.896)})
    app.set_name(1, "Two")
    app.calculate_value_ranges(reset_filter=False)
    app.set_marker_amount(0, 4)


def auoscale_example(num, min_value=0):
    """ Runs an example with num vectors.
    Each vectors has the form (x, x, x, x, x, x, x) min_value<= x < num
    """
    app = API(7)
    vectors_to_add = set()
    for i in range(min_value, min_value + num):
        vectors_to_add.add((i, i, i, i, i, i, i))
    app.add_vectors(vectors_to_add)
    app.calculate_value_ranges()


def autoscale_test():
    """ Demo of the autoscale function """
    app = API(3)
    app.add_vector((10, 5, -1))
    app.add_vector((20, 6, -3))
    app.calculate_value_ranges()


def random_example(num):
    """ Runs an example with num randomized vectors.
    """
    app = API(7)
    vectors_to_add = set()
    for i in range(0, num):
        vector = (randint(0, num),)
        for _ in range(1, 7):
            vector = vector + (randint(0, num),)
        vectors_to_add.add(vector)
    app.add_vectors(vectors_to_add)
    for i in range(7):
        app.set_value_range(i, (0, num), reset_filter=True)

def benutzbar(axes, vectors):
    app = API(axes)
    vectors_to_add = set()
    for i in range(0,vectors):
        vector = (randint(0, vectors * 100)/100,)
        for _ in range(1, axes):
            vector = vector + (randint(0, vectors * 100) / 100,)
        vectors_to_add.add(vector)
    app.add_vectors(vectors_to_add)
    app.calculate_value_ranges()

def warnings_example():
    """ Runs the app and trys to add some malformed vectors.
    """
    app = API(7)
    app.add_vector("a")
    app.add_vector(object)
    app.add_vector((-10, 0))
    app.add_vector((-10, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


def disabled_warnings_example():
    """ Same as the warnings_example but this time with turned off
    warnings
    """
    app = API(7)
    app.disable_warnings()
    app.add_vector("a")
    app.add_vector(object)
    app.add_vector((-10, 0))
    app.add_vector((-10, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


hotel_example()
# benutzbar(17,1)
#warnings_example()