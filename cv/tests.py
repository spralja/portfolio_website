from django.test import TestCase

from .models import *


def quick_date(month, year):
    return Date(month=month, year=year)


class DateTest(TestCase):

    def test_compare_month_is_less_year_is_less(self):
        d1 = quick_date(1, 1)
        d2 = quick_date(2, 2)
        self.assertLess(Date.compare(d1, d2), 0)

    def test_compare_month_is_less_year_is_same(self):
        d1 = quick_date(1, 1)
        d2 = quick_date(2, 1)
        self.assertLess(Date.compare(d1, d2), 0)

    def test_compare_month_is_less_year_is_greater(self):
        d1 = quick_date(1, 2)
        d2 = quick_date(2, 1)
        self.assertGreater(Date.compare(d1, d2), 0)

    def test_compare_month_is_same_year_is_less(self):
        d1 = quick_date(1, 1)
        d2 = quick_date(1, 2)
        self.assertLess(Date.compare(d1, d2), 0)

    def test_compare_month_is_same_year_is_same(self):
        d1 = quick_date(1, 1)
        d2 = quick_date(1, 1)
        self.assertEqual(Date.compare(d1, d2), 0)

    def test_compare_month_is_same_year_is_greater(self):
        d1 = quick_date(1, 2)
        d2 = quick_date(1, 1)
        self.assertGreater(Date.compare(d1, d2), 0)

    def test_compare_month_is_greater_year_is_less(self):
        d1 = quick_date(2, 1)
        d2 = quick_date(1, 2)
        self.assertLess(Date.compare(d1, d2), 0)

    def test_compare_month_is_greater_year_is_same(self):
        d1 = quick_date(2, 1)
        d2 = quick_date(1, 1)
        self.assertGreater(Date.compare(d1, d2), 0)

    def test_compare_month_is_greater_year_is_greater(self):
        d1 = quick_date(2, 2)
        d2 = quick_date(1, 1)
        self.assertGreater(Date.compare(d1, d2), 0)

    def test_compare_d1_null_d2_null(self):
        d1 = None
        d2 = None
        self.assertEqual(Date.compare(d1, d2), 0)

    def test_compare_d1_null_d2_not_null(self):
        d1 = None
        d2 = quick_date(1, 1)
        self.assertGreater(Date.compare(d1, d2), 0)

    def test_compare_d1_not_null_d2_null(self):
        d1 = quick_date(1, 1)
        d2 = None
        self.assertLess(Date.compare(d1, d2), 0)

