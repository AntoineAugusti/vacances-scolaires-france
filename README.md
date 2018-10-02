[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/AntoineAugusti/vacances-scolaires-france/blob/master/LICENSE.md)
![CircleCI](https://img.shields.io/circleci/project/github/AntoineAugusti/vacances-scolaires-france.svg?style=flat-square)
![PyPI](https://img.shields.io/pypi/vacances_scolaires_france.svg?style=flat-square)

# Vacances scolaires France
Permet de connaître les dates des vacances scolaires en France, depuis 2009, pour les zones A, B et C.

## Installation
```
pip install vacances-scolaires-france
```

## Utilisation

```python
from vacances_scolaires_france import SchoolHolidayDates

import datetime

d = SchoolHolidayDates()
# Is it an holiday for zone A, B or C?
d.is_holiday(datetime.date(2017, 12, 25))
# True
# Is it an holiday for a given zone?
d.is_holiday_for_zone(datetime.date(2009, 2, 7), 'A')
# True
# Get holidays for any zone in a year
d.holidays_for_year(2018)
# {datetime.date(2018, 1, 1): OrderedDict([('date', datetime.date(2018, 01, 01)), ('vacances_zone_a', True), ('vacances_zone_b', True), ('vacances_zone_c', True), ('nom_vacances', 'Vacances de Noël')]), ...}
# Get holiday dates given a year and an holiday name
d.holiday_for_year_by_name(2017, 'Vacances de la Toussaint')
# {datetime.date(2017, 10, 21): OrderedDict([('date', datetime.date(2017, 10, 21)), ('vacances_zone_a', True), ('vacances_zone_b', True), ('vacances_zone_c', True), ...}
# Get holiday dates for a given year and zone
d.holidays_for_year_and_zone(2017, 'A')
# {datetime.date(2017, 1, 1): OrderedDict([('date', datetime.date(2017, 01, 01)), ('vacances_zone_a', True), ('vacances_zone_b', True), ('vacances_zone_c', True), ...}
# Get holiday dates for a given year, zone and holiday name
d.holidays_for_year_zone_and_name(2017, 'A', 'Vacances de Noël')
# {datetime.date(2017, 1, 1): OrderedDict([('date', datetime.date(2017, 1, 1)), ('vacances_zone_a', True), ('vacances_zone_b', True), ('vacances_zone_c', True), ('nom_vacances', 'Vacances de Noël')]), ...}
```

## Notice
This software is available under the MIT license and was developed as part of the [Entrepreneur d'Intérêt Général program](https://entrepreneur-interet-general.etalab.gouv.fr) by the French government.

Projet développé dans le cadre du programme « [Entrepreneur d’intérêt général](https://entrepreneur-interet-general.etalab.gouv.fr) ».
