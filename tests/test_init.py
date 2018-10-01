# -*- coding: utf-8 -*-
import unittest
import datetime

from vacances_scolaires_france import Dates


class TestInit(unittest.TestCase):
    EXPECTED_KEYS = ['date', 'nom_vacances', 'vacances_zone_a', 'vacances_zone_b', 'vacances_zone_c']

    def test_is_holiday(self):
        d = Dates()

        self.assertTrue(d.is_holiday(datetime.date(2017, 12, 25)))
        self.assertFalse(d.is_holiday(datetime.date(2017, 12, 1)))

    def test_is_holiday_for_zone(self):
        d = Dates()

        self.assertTrue(d.is_holiday_for_zone(datetime.date(2009, 2, 7), 'A'))
        self.assertFalse(d.is_holiday_for_zone(datetime.date(2009, 2, 7), 'B'))
        self.assertFalse(d.is_holiday_for_zone(datetime.date(2009, 2, 7), 'C'))

        with self.assertRaisesRegexp(ValueError, 'Unsupported zone: D'):
            self.assertFalse(d.is_holiday_for_zone(datetime.date(2009, 2, 7), 'D'))

    def test_holidays_for_year(self):
        d = Dates()

        res = d.holidays_for_year(2018)

        self.assertEquals(len(res), 151)

        for k, v in res.items():
            self.assertEquals(sorted(v.keys()), self.EXPECTED_KEYS)

        self.assertEquals({}, d.holidays_for_year(2020))

    def test_holiday_for_year_by_name(self):
        d = Dates()

        res = d.holiday_for_year_by_name(2017, 'Vacances de la Toussaint')

        self.assertEquals(len(res), 16)
        for k, v in res.items():
            self.assertEquals(sorted(v.keys()), self.EXPECTED_KEYS)
        self.assertEquals(
            sorted([v['date'] for v in res.values()]),
            [
                '2017-10-21', '2017-10-22', '2017-10-23', '2017-10-24',
                '2017-10-25', '2017-10-26', '2017-10-27', '2017-10-28',
                '2017-10-29', '2017-10-30', '2017-10-31', '2017-11-01',
                '2017-11-02', '2017-11-03', '2017-11-04', '2017-11-05'
            ]
        )

        self.assertEquals({}, d.holiday_for_year_by_name(2017, 'Foo'))

    def test_holidays_for_year_and_zone(self):
        d = Dates()

        res = d.holidays_for_year_and_zone(2017, 'A')

        self.assertEquals(len(res), 120)
        for k, v in res.items():
            self.assertEquals(sorted(v.keys()), self.EXPECTED_KEYS)

            self.assertTrue(v['vacances_zone_a'])
