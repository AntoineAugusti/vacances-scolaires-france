# -*- coding: utf-8 -*-
import csv
import os
import datetime


class Dates(object):
    SUPPORTED_ZONES = ['A', 'B', 'C']

    def __init__(self):
        super(Dates, self).__init__()
        self.data = {}
        self.load_data()

    def load_data(self):
        filename = os.path.join(os.path.dirname(__file__), '../data/data.csv')

        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = datetime.datetime.strptime(
                    row['date'], '%Y-%m-%d'
                ).date()
                for zone in self.SUPPORTED_ZONES:
                    zone_key = self.zone_key(zone)
                    row[zone_key] = row[zone_key] == 'True'
                self.data[key] = row

    def check_zone(self, zone):
        if zone not in self.SUPPORTED_ZONES:
            raise ValueError('Unsupported zone: ' + zone)

    def zone_key(self, zone):
        self.check_zone(zone)
        return 'vacances_zone_' + zone.lower()

    def is_holiday(self, date):
        row = self.data[date]
        res = False
        for zone in self.SUPPORTED_ZONES:
            res = res or row[self.zone_key(zone)]
        return res

    def is_holiday_for_zone(self, date, zone):
        row = self.data[date]
        return row[self.zone_key(zone)]

    def holidays_for_year(self, year):
        return {
            k: self.data[k] for k in self.data.keys()
            if self.is_holiday(k) and k.year == year
        }

    def holiday_for_year_by_name(self, year, name):
        return {
            k: self.data[k] for k, v in self.data.items()
            if v['nom_vacances'] == name and k.year == year
        }

    def holidays_for_year_and_zone(self, year, zone):
        return {
            k: self.data[k] for k in self.data.keys()
            if self.is_holiday_for_zone(k, zone) and k.year == year
        }
