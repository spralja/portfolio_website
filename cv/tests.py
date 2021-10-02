from django.test import TestCase

# Create your tests here.
from cv.models import Date, Experience


def createDate(month, year):
    return Date(month=month, year=year)


class DateTest(TestCase):
    def test_compare_is_newer_year_test(self):
        d1 = createDate(1, 100)
        d2 = createDate(1, 10)
        self.assertIs(d1.compare(d2) > 0, True)

    def test_compare_is_older_year_test(self):
        d1 = createDate(1, 10)
        d2 = createDate(1, 100)
        self.assertIs(d1.compare(d2) < 0, True)

    def test_compare_is_same(self):
        d1 = createDate(1, 1)
        d2 = createDate(1, 1)
        self.assertIs(d1.compare(d2) == 0, True)

    def test_compare_is_newer_month(self):
        d1 = createDate(10, 1)
        d2 = createDate(1, 1)
        self.assertIs(d1.compare(d2) > 0, True)

    def test_compare_is_older_month(self):
        d1 = createDate(1, 1)
        d2 = createDate(10, 1)
        self.assertIs(d1.compare(d2) < 0, True)


def createExperience(month1, year1, month2, year2):
    if month2 is None and year2 is None:
        return Experience(
            authority="",
            title="",
            start_date=Date(month1, year1),
            end_date=None
        )

    return Experience(
        authority="",
        title="",
        start_date=Date(month1, year1),
        end_date=Date(month2, year2)
    )


