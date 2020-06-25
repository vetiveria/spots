import quantities as qt


class Measures:

    def __init__(self):
        self.name = ''

    @staticmethod
    def pounds_to_grams(y):

        measure = 1 * qt.pound
        measure.units = qt.gram
        grams = measure.magnitude.take(0)

        weight = y * grams
        return weight

    @staticmethod
    def pounds_to_kilograms(y):

        measure = 1 * qt.pound
        measure.units = qt.kilogram
        kilograms = measure.magnitude.take(0)

        weight = y * kilograms
        return weight
