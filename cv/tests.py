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


class ExperienceTest(TestCase):
    def test_is_newer(self):
        e1 = createExperience(1, 1, 1, 10)
        e2 = createExperience(1, 1, 1, 1)
        self.assertIs(e1.compare(e2) > 0, True)

    def test_is_older(self):
        e1 = createExperience(1, 1, 1, 1)
        e2 = createExperience(1, 1, 1, 10)
        self.assertIs(e1.compare(e2) < 0, True)

    def test_is_same(self):
        e1 = createExperience(1, 1, 1, 1)
        e2 = createExperience(1, 1, 1, 1)
        self.assertIs(e1.compare(e2) == 0, True)

    def test_is_newer_month(self):
        e1 = createExperience(1, 1, 10, 1)
        e2 = createExperience(1, 1, 1, 1)
        self.assertIs(e1.compare(e2) > 0, True)

    def test_is_older_month(self):
        e1 = createExperience(1, 1, 1, 1)
        e2 = createExperience(1, 1, 10, 1)
        self.assertIs(e1.compare(e2) < 0, True)

    def test_is_in_progress_other_is_not(self):
        e1 = createExperience(1, 1, None, None)
        e2 = createExperience(10, 10, 1, 1)
        self.assertIs(e1.compare(e2) > 0, True)

    def test_is_not_in_progress_other_is(self):
        e1 = createExperience(1, 1, 10, 10)
        e2 = createExperience(1, 1, None, None)
        self.assertIs(e1.compare(e2) < 0, True)

    def test_both_are_in_progress_is_newer(self):
        e1 = createExperience(1, 10, None, None)
        e2 = createExperience(1, 1, None, None)
        self.assertIs(e1.compare(e2) > 0, True)

    def test_both_are_in_progress_is_older(self):
        e1 = createExperience(1, 1, None, None)
        e2 = createExperience(1, 10, None, None)
        self.assertIs(e1.compare(e2) < 0, True)

    def test_both_are_in_progress_is_same(self):
        e1 = createExperience(1, 1, None, None)
        e2 = createExperience(1, 1, None, None)
        self.assertIs(e1.compare(e2) == 0, True)

    def test_both_are_in_progress_is_newer_month(self):
        e1 = createExperience(10, 1, None, None)
        e2 = createExperience(1, 1, None, None)
        self.assertIs(e1.compare(e2) > 0, True)

    def test_both_are_in_progress_is_older_month(self):
        e1 = createExperience(1, 1, None, None)
        e2 = createExperience(10, 1, None, None)
        self.assertIs(e1.compare(e2) < 0, True)
