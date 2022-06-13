# -*- coding: utf-8 -*-
import csv
import os
import datetime
import requests


class UnsupportedYearException(Exception):
    pass


class UnsupportedZoneException(Exception):
    pass


class UnsupportedHolidayException(Exception):
    pass


class SchoolHolidayDates(object):
    SUPPORTED_ZONES = ["A", "B", "C"]
    SUPPORTED_HOLIDAY_NAMES = [
        "Vacances de Noël",
        "Vacances d'hiver",
        "Vacances de printemps",
        "Vacances d'été",
        "Vacances de la Toussaint",
        "Pont de l'Ascension",
    ]
    STABLE_URL = "https://www.data.gouv.fr/fr/datasets/r/c3781037-dffb-4789-9af9-15a955336771"
    BASE_FILE = os.path.join(os.path.dirname(__file__), "data/data.csv")

    def __init__(self, download=False, file=None):
        super(SchoolHolidayDates, self).__init__()
        self.data = {}
        self.load_data(download, file)

    def load_data(self, download=False, file=None):
        if download:
            r = requests.get(SchoolHolidayDates.STABLE_URL, allow_redirects=True)
            open(file, 'wb').write(r.content)
        filename = file if file and os.path.isfile(file) else SchoolHolidayDates.BASE_FILE

        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                date = datetime.datetime.strptime(row["date"], "%Y-%m-%d").date()
                row["date"] = date

                # Only append rows where at least 1 zone is on holiday
                is_holiday = False
                for zone in self.SUPPORTED_ZONES:
                    zone_key = self.zone_key(zone)
                    row[zone_key] = row[zone_key] == "True"
                    is_holiday = is_holiday or row[zone_key]

                if is_holiday:
                    if len(row["nom_vacances"]) == 0:
                        raise ValueError("Holiday name not set for date: " + str(date))
                    self.data[date] = row

    def zone_key(self, zone):
        if zone not in self.SUPPORTED_ZONES:
            raise UnsupportedZoneException("Unsupported zone: " + zone)
        return "vacances_zone_" + zone.lower()

    def check_name(self, name):
        if name not in self.SUPPORTED_HOLIDAY_NAMES:
            raise UnsupportedHolidayException("Unknown holiday name: " + name)

    def is_holiday(self, date):
        if not type(date) is datetime.date:
            raise ValueError("date should be a datetime.date")
        return date in self.holidays_for_year(date.year)

    def is_holiday_for_zone(self, date, zone):
        if not type(date) is datetime.date:
            raise ValueError("date should be a datetime.date")
        try:
            holidays_for_year = self.holidays_for_year(date.year)
            return holidays_for_year[date][self.zone_key(zone)]
        except KeyError:
            return False

    def holidays_for_year(self, year):
        res = {k: v for k, v in self.data.items() if k.year == year}

        if len(res) == 0:
            raise UnsupportedYearException("No data for year: " + str(year))

        return res

    def holiday_for_year_by_name(self, year, name):
        self.check_name(name)

        return {
            k: v
            for k, v in self.holidays_for_year(year).items()
            if v["nom_vacances"] == name
        }

    def holidays_for_year_and_zone(self, year, zone):
        return {
            k: v
            for k, v in self.holidays_for_year(year).items()
            if self.is_holiday_for_zone(k, zone)
        }

    def holidays_for_year_zone_and_name(self, year, zone, name):
        self.check_name(name)

        return {
            k: v
            for k, v in self.holidays_for_year(year).items()
            if self.is_holiday_for_zone(k, zone) and v["nom_vacances"] == name
        }
