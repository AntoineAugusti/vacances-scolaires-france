# -*- coding: utf-8 -*-
import unittest
import datetime

from vacances_scolaires_france import Dates


class TestInit(unittest.TestCase):
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
            self.assertEquals(sorted(v.keys()), ['date', 'nom_vacances', 'vacances_zone_a', 'vacances_zone_b', 'vacances_zone_c'])

        self.assertEquals({}, d.holidays_for_year(2020))

