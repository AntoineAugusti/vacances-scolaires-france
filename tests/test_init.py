# -*- coding: utf-8 -*-
import unittest
import datetime

from vacances_scolaires_france import SchoolHolidayDates
from vacances_scolaires_france import UnsupportedYearException
from vacances_scolaires_france import UnsupportedZoneException
from vacances_scolaires_france import UnsupportedHolidayException


class TestInit(unittest.TestCase):
    EXPECTED_KEYS = [
        "date",
        "nom_vacances",
        "vacances_zone_a",
        "vacances_zone_b",
        "vacances_zone_c",
    ]

    def parse_date(self, date):
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()

    def test_is_holiday(self):
        d = SchoolHolidayDates()

        self.assertTrue(d.is_holiday(datetime.date(2017, 12, 25)))
        self.assertFalse(d.is_holiday(datetime.date(2017, 12, 1)))

        with self.assertRaisesRegex(UnsupportedYearException, "No data for year: 1985"):
            d.is_holiday(datetime.date(1985, 2, 7))

        with self.assertRaisesRegex(ValueError, "date should be a datetime.date"):
            d.is_holiday(datetime.datetime(2017, 12, 1, 2, 0))

    def test_is_holiday_for_zone(self):
        d = SchoolHolidayDates()

        self.assertTrue(d.is_holiday_for_zone(datetime.date(2009, 2, 7), "A"))
        self.assertFalse(d.is_holiday_for_zone(datetime.date(2009, 2, 7), "B"))
        self.assertFalse(d.is_holiday_for_zone(datetime.date(2009, 2, 7), "C"))
        self.assertFalse(d.is_holiday_for_zone(datetime.date(2009, 3, 7), "A"))
        self.assertFalse(d.is_holiday_for_zone(datetime.date(2009, 6, 7), "A"))

        with self.assertRaisesRegex(UnsupportedYearException, "No data for year: 1985"):
            d.is_holiday_for_zone(datetime.date(1985, 2, 7), "D")
        with self.assertRaisesRegex(UnsupportedZoneException, "Unsupported zone: D"):
            self.assertFalse(d.is_holiday_for_zone(datetime.date(2009, 2, 7), "D"))
        with self.assertRaisesRegex(ValueError, "date should be a datetime.date"):
            d.is_holiday_for_zone(datetime.datetime(2017, 12, 1, 2, 0), "A")

    def test_holidays_for_year(self):
        d = SchoolHolidayDates()

        res = d.holidays_for_year(2018)

        self.assertEqual(len(res), 151)

        for k, v in res.items():
            self.assertEqual(sorted(v.keys()), self.EXPECTED_KEYS)

        with self.assertRaisesRegex(UnsupportedYearException, "No data for year: 2027"):
            self.assertEqual({}, d.holidays_for_year(2027))

    def test_holiday_for_year_by_name(self):
        d = SchoolHolidayDates()

        res = d.holiday_for_year_by_name(2017, "Vacances de la Toussaint")

        self.assertEqual(len(res), 16)
        for k, v in res.items():
            self.assertEqual(sorted(v.keys()), self.EXPECTED_KEYS)
        expected_dates = [
            self.parse_date(date)
            for date in [
                "2017-10-21",
                "2017-10-22",
                "2017-10-23",
                "2017-10-24",
                "2017-10-25",
                "2017-10-26",
                "2017-10-27",
                "2017-10-28",
                "2017-10-29",
                "2017-10-30",
                "2017-10-31",
                "2017-11-01",
                "2017-11-02",
                "2017-11-03",
                "2017-11-04",
                "2017-11-05",
            ]
        ]
        self.assertEqual(sorted([v["date"] for v in res.values()]), expected_dates)

        with self.assertRaisesRegex(UnsupportedYearException, "No data for year: 1985"):
            self.assertEqual(
                {}, d.holiday_for_year_by_name(1985, "Vacances de la Toussaint")
            )

        with self.assertRaisesRegex(
            UnsupportedHolidayException, "Unknown holiday name: Foo"
        ):
            self.assertEqual({}, d.holiday_for_year_by_name(2017, "Foo"))

    def test_holidays_for_year_and_zone(self):
        d = SchoolHolidayDates()

        res = d.holidays_for_year_and_zone(2017, "A")

        self.assertEqual(len(res), 118)
        for k, v in res.items():
            self.assertEqual(sorted(v.keys()), self.EXPECTED_KEYS)

            self.assertTrue(v["vacances_zone_a"])

        with self.assertRaisesRegex(UnsupportedYearException, "No data for year: 1985"):
            self.assertFalse(d.holidays_for_year_and_zone(1985, "D"))

        with self.assertRaisesRegex(UnsupportedZoneException, "Unsupported zone: D"):
            self.assertFalse(d.holidays_for_year_and_zone(2017, "D"))

    def test_holidays_for_year_zone_and_name(self):
        d = SchoolHolidayDates()

        res = d.holidays_for_year_zone_and_name(2017, "A", "Vacances de printemps")
        self.assertEqual(len(res), 17)

        for k, v in res.items():
            self.assertEqual(sorted(v.keys()), self.EXPECTED_KEYS)
        expected_dates = [
            self.parse_date(date)
            for date in [
                "2017-04-15",
                "2017-04-16",
                "2017-04-17",
                "2017-04-18",
                "2017-04-19",
                "2017-04-20",
                "2017-04-21",
                "2017-04-22",
                "2017-04-23",
                "2017-04-24",
                "2017-04-25",
                "2017-04-26",
                "2017-04-27",
                "2017-04-28",
                "2017-04-29",
                "2017-04-30",
                "2017-05-01",
            ]
        ]
        self.assertEqual(sorted([v["date"] for v in res.values()]), expected_dates)

        with self.assertRaisesRegex(UnsupportedYearException, "No data for year: 1985"):
            d.holidays_for_year_zone_and_name(1985, "A", "Vacances de printemps")

        with self.assertRaisesRegex(UnsupportedZoneException, "Unsupported zone: D"):
            d.holidays_for_year_zone_and_name(2017, "D", "Vacances de printemps")

        with self.assertRaisesRegex(
            UnsupportedHolidayException, "Unknown holiday name: Foo"
        ):
            d.holidays_for_year_zone_and_name(2017, "A", "Foo")

    def test_supported_holidays_are_complete(self):
        d = SchoolHolidayDates()

        res = d.holidays_for_year(2019)

        names = set()
        for _, v in res.items():
            names.add(v["nom_vacances"])

        expected = set(SchoolHolidayDates.SUPPORTED_HOLIDAY_NAMES)

        self.assertEquals(names, expected)

    def test_holidays_between(self):
        d = SchoolHolidayDates()

        res = d.holidays_between('2022-01-01', '2022-02-01')
        for k, v in res.items():
            self.assertEquals(sorted(v.keys()), self.EXPECTED_KEYS)

