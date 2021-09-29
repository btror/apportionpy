"""
Created on Mon Sep 27 18:30:00 2021

@author: Brandon Rorie
"""

import unittest
import apportionpy.apportionment as ap


class TestApportionMethods(unittest.TestCase):

    def test_calculate_adam(self):
        method = ap.Apportion(seats=10, populations=[10, 20, 30, 35], method="adam")
        self.assertEqual(method.initial_fair_shares, [2, 3, 4, 4])
        self.assertEqual(method.fair_shares, [1, 2, 3, 4])
        self.assertEqual(method.initial_quotas,
                         [1.0526315789473684, 2.1052631578947367, 3.1578947368421053, 3.6842105263157894])
        self.assertEqual(method.final_quotas,
                         [0.935672514619883, 1.871345029239766, 2.807017543859649, 3.2748538011695905])
        self.assertEqual(method.initial_divisor, 9.5)
        self.assertEqual(method.modified_divisor, 10.6875)

    def test_calculate_hamilton(self):
        method = ap.Apportion(seats=10, populations=[10, 20, 30, 35], method="hamilton")
        self.assertEqual(method.initial_fair_shares, [1, 2, 3, 3])
        self.assertEqual(method.fair_shares, [1, 2, 3, 4])
        self.assertEqual(method.initial_quotas,
                         [1.0526315789473684, 2.1052631578947367, 3.1578947368421053, 3.6842105263157894])
        self.assertEqual(method.final_quotas,
                         [1.0526315789473684, 2.1052631578947367, 3.1578947368421053, 3.6842105263157894])
        self.assertEqual(method.initial_divisor, 9.5)
        self.assertEqual(method.modified_divisor, 9.5)

    def test_calculate_jefferson(self):
        method = ap.Apportion(seats=10, populations=[10, 20, 30, 35], method="jefferson")
        self.assertEqual(method.initial_fair_shares, [1, 2, 3, 3])
        self.assertEqual(method.fair_shares, [1, 2, 3, 4])
        self.assertEqual(method.initial_quotas,
                         [1.0526315789473684, 2.1052631578947367, 3.1578947368421053, 3.6842105263157894])
        self.assertEqual(method.final_quotas,
                         [1.2307692307692308, 2.4615384615384617, 3.6923076923076925, 4.3076923076923075])
        self.assertEqual(method.initial_divisor, 9.5)
        self.assertEqual(method.modified_divisor, 8.125)

    def test_calculate_webster(self):
        method = ap.Apportion(seats=10, populations=[11, 13, 15, 65], method="webster")
        self.assertEqual(method.initial_fair_shares, [1, 1, 1, 6])
        self.assertEqual(method.fair_shares, [1, 1, 2, 6])
        self.assertEqual(method.initial_quotas, [1.0576923076923077, 1.25, 1.4423076923076923, 6.25])
        self.assertEqual(method.final_quotas, [1.1, 1.3, 1.5, 6.5])
        self.assertEqual(method.initial_divisor, 10.4)
        self.assertEqual(method.modified_divisor, 10.0)

    def test_calculate_equal_proportions(self):
        method = ap.Apportion(seats=70, populations=[300500, 200000, 50000, 38000, 21500], method="equal proportions")
        self.assertEqual(method.fair_shares, [34, 23, 6, 4, 3])


if __name__ == "__main__":
    unittest.main()
