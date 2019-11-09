import unittest
# For now add vector to sys.path
import sys
sys.path.append('../')
import vector as vec

class TestVector(unittest.TestCase):

    c = 3.2
    assert type(c) in [float, int]

    v_tuple = (1, 2, 3)
    w_tuple = (-3, 4.2, 0)
    assert len(v_tuple) == len(w_tuple)
    assert v_tuple != w_tuple

    v_list = list(v_tuple)
    assert type(v_tuple) == type((1, 2, 3))
    assert type(v_list) == type([1, 2, 3])
    assert v_list == list(v_tuple)

    v_list_extended = v_list + [3]
    assert len(v_list_extended) > len(v_list)

    v = vec.Vector(v_tuple)
    w = vec.Vector(w_tuple)

    def assertVectorsEqual(self, vec_1, vec_2):
        return self.assertTrue(vec_1 == vec_2)

    def assertVectorsUnequal(self, vec_1, vec_2):
        return self.assertFalse(vec_1 == vec_2)

    # unit tests

    def test_equality_of_two_equal_vectors(self):
        self.assertVectorsEqual(self.v, vec.Vector(self.v_tuple))

    def test_for_exception_if_we_compare_different_length_vectors(self):
        with self.assertRaises(ValueError):
            truth_value = self.v == vec.Vector(self.v_list_extended)

    def test_equality_of_different_same_length_vetors(self):
        self.assertVectorsUnequal(self.v, self.w)

    def test_equality_of_vector_from_list_and_vector_from_tuple(self):
        self.assertVectorsEqual(vec.Vector(self.v_tuple), vec.Vector(self.v_list))

    def test_addition_of_vectors(self):
        sum_input = [v_i + w_i for v_i, w_i in zip(self.v_tuple, self.w_tuple)]
        self.assertVectorsEqual(self.v + self.w, vec.Vector(sum_input))

    def test_for_exception_if_we_add_vectors_of_unequal_length(self):
        with self.assertRaises(ValueError):
            w = self.v + vec.Vector(self.v_list_extended)

    def test_subtraction_of_vectors(self):
        sub_input = [v_i - w_i for v_i, w_i in zip(self.v_tuple, self.w_tuple)]
        self.assertVectorsEqual(self.v - self.w, vec.Vector(sub_input))

    def test_for_exception_if_we_subtract_vectors_of_unequal_length(self):
        with self.assertRaises(ValueError):
            w = self.v - vec.Vector(self.v_list_extended)

    def test_tuple_returned_equals_tuple_used_to_construct(self):
        self.assertEquals(self.v_tuple, self.v.value)

    def test_right_multiply_vector_by_constant(self):
        self.assertVectorsEqual(self.v * self.c, vec.Vector([v_i * self.c for v_i in self.v_list]))

    def test_left_multiply_vector_by_constant(self):
        self.assertVectorsEqual(self.c * self.v, vec.Vector([self.c * v_i for v_i in self.v_list]))


if __name__ == '__main__':
    unittest.main()
