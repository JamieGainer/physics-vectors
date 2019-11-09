class Vector():

    def __init__(self, input_data):
        self.value = tuple(input_data)

    def __eq__(self, other):
        self.assert_same_dimensionality_as_other(other)
        for x_i, y_i in zip(self.value, other.value):
            if x_i != y_i:
                return False
        return True

    def __add__(self, other):
        self.assert_same_dimensionality_as_other(other)
        sum_input_data = [x_i + y_i for x_i, y_i in zip(self.value, other.value)]
        return Vector(sum_input_data)

    def __sub__(self, other):
        self.assert_same_dimensionality_as_other(other)
        sub_input_data = [x_i - y_i for x_i, y_i in zip(self.value, other.value)]
        return Vector(sub_input_data)

    def __mul__(self, other):
        return Vector([x_i * other for x_i in self.value])

    def __rmul__(self, other):
        return Vector([other * x_i for x_i in self.value])


    def assert_same_dimensionality_as_other(self, other):
        if len(other.value) != len(self.value):
            raise ValueError("Vectors have different dimensions.")