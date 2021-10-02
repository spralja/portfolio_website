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


def createExperience(year1, year2):
    if year2 is None:
        return Experience(
            authority="",
            title="",
            start_date=createDate(1, year1),
            end_date=None
        )

    return Experience(
        authority="",
        title="",
        start_date=createDate(1, year1),
        end_date=Date(1, year2)
    )


class ExperienceTest(TestCase):
    def test_started_later_finished_later(self):
        e1 = createExperience(2, 2)
        e2 = createExperience(1, 1)
        self.assertGreater(e1.compare(e2), 0)

    def test_started_later_finished_same(self):
        e1 = createExperience(2, 2)
        e2 = createExperience(1, 2)
        self.assertGreater(e1.compare(e2), 0)

    def test_started_later_finished_earlier(self):
        e1 = createExperience(2, 2)
        e2 = createExperience(1, 3)
        self.assertLess(e1.compare(e2), 0)

    def test_started_same_finished_later(self):
        e1 = createExperience(1, 2)
        e2 = createExperience(1, 1)
        self.assertGreater(e1.compare(e2), 0)

    def test_started_same_finished_same(self):
        e1 = createExperience(1, 1)
        e2 = createExperience(1, 1)
        self.assertEqual(e1.compare(e2), 0)

    def test_started_same_finished_earlier(self):
        e1 = createExperience(1, 1)
        e2 = createExperience(1, 2)
        self.assertLess(e1.compare(e2), 0)

    def test_started_earlier_finished_later(self):
        e1 = createExperience(1, 3)
        e2 = createExperience(2, 2)
        self.assertGreater(e1.compare(e2), 0)

    def test_started_earlier_finished_same(self):
        e1 = createExperience(1, 2)
        e2 = createExperience(2, 2)
        self.assertLess(e1.compare(e2), 0)

    def test_started_earlier_finished_earlier(self):
        e1 = createExperience(1, 1)
        e2 = createExperience(2, 2)
        self.assertLess(e1.compare(e2), 0)

    def test_started_later_finished_not_not(self):
        e1 = createExperience(2, None)
        e2 = createExperience(1, None)
        self.assertGreater(e1.compare(e2), 0)

    def test_started_later_finished_yes_not(self):
        e1 = createExperience(2, 2)
        e2 = createExperience(1, None)
        self.assertLess(e1.compare(e2), 0)

    def test_started_later_finished_not_yes(self):
        e1 = createExperience(2, None)
        e2 = createExperience(1, 1)
        self.assertGreater(e1.compare(e2), 0)

    def test_started_same_finished_not_not(self):
        e1 = createExperience(1, None)
        e2 = createExperience(1, None)
        self.assertEqual(e1.compare(e2), 0)

    def test_started_same_finished_yes_not(self):
        e1 = createExperience(1, 1)
        e2 = createExperience(1, None)
        self.assertLess(e1.compare(e2), 0)

    def test_started_same_finished_not_yes(self):
        e1 = createExperience(1, None)
        e2 = createExperience(1, 1)
        self.assertGreater(e1.compare(e2), 0)

    def test_started_earlier_finished_not_not(self):
        e1 = createExperience(1, None)
        e2 = createExperience(2, None)
        self.assertLess(e1.compare(e2), 0)

    def test_started_earlier_finished_yes_not(self):
        e1 = createExperience(1, 1)
        e2 = createExperience(2, None)
        self.assertLess(e1.compare(e2), 0)

    def test_started_earlier_finished_not_yes(self):
        e1 = createExperience(1, None)
        e2 = createExperience(2, 2)
        self.assertGreater(e1.compare(e2), 0)

