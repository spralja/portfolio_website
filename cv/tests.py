from django.test import TestCase

# Create your tests here.
from cv.models import Date


class DateTest(TestCase):
    def test_compare_is_newer_test(self):
        d1 = Date(1, 100)
        d2 = Date(1, 10)
        self.assertIs(d1.compare(d2) > 0, True)

    def test_compare_is_older_test(self):
        d1 = Date(1, 10)
        d2 = Date(1, 100)
        self.assertIs(d1.compare(d2) < 0, True)

    def test_compare_is_same(self):
        d1 = Date(1, 1)
        d2 = Date(1, 1)
        self.assertIs(d1.compare(d2) == 0, True)