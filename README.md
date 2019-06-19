[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/AntoineAugusti/vacances-scolaires-france/blob/master/LICENSE.md)
![CircleCI](https://img.shields.io/circleci/project/github/AntoineAugusti/vacances-scolaires-france.svg?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/vacances-scolaires-france.svg?style=flat-square)

# Vacances scolaires France
This package can be used to find the dates of school holidays in France, since 1990.

In French in the text: cette librairie permet de connaître les dates des vacances scolaires en France, depuis 1990, pour les zones A, B et C.

La répartition en trois zones de vacances A, B et C est définie de la façon suivante.

**Septembre 1995 - Janvier 2016** :
- Zone A : Académies de Caen, Clermont-Ferrand, Grenoble, Lyon, Montpellier, Nancy-Metz, Nantes, Rennes, Toulouse
- Zone B : Académies d'Aix-Marseille, Amiens, Besançon, Dijon, Lille, Limoges, Nice, Orléans-Tours, Poitiers, Reims, Rouen , Strasbourg,
- Zone C : Académies de Bordeaux, Créteil, Paris, Versailles

**Depuis janvier 2016** :
- Zone A : Académies de Besançon, Bordeaux, Clermont-Ferrand, Dijon, Grenoble, Limoges, Lyon, Poitiers
- Zone B : Académies d'Aix-Marseille, Amiens, Caen, Lille, Nantes, Nice, Nancy-Metz, Orléans-Tours, Reims, Rennes, Rouen, Strasbourg
- Zone C : Académies de Créteil, Montpellier, Paris, Versailles, Toulouse

## Installation
```
pip install vacances-scolaires-france
```

## Usage

```python
from vacances_scolaires_france import SchoolHolidayDates

import datetime

d = SchoolHolidayDates()
# Is it an holiday for zone A, B or C?
d.is_holiday(datetime.date(2017, 12, 25))
# Returns: True

# Is it an holiday for a given zone?
d.is_holiday_for_zone(datetime.date(2009, 2, 7), 'A')
# Returns: True

# Get holidays for any zone in a year
d.holidays_for_year(2018)
# Returns: {datetime.date(2018, 1, 1): OrderedDict([('date', datetime.date(2018, 01, 01)), ('vacances_zone_a', True), ('vacances_zone_b', True), ('vacances_zone_c', True), ('nom_vacances', 'Vacances de Noël')]), ...}

# Get holiday dates given a year and an holiday name
d.holiday_for_year_by_name(2017, 'Vacances de la Toussaint')
# Returns: {datetime.date(2017, 10, 21): OrderedDict([('date', datetime.date(2017, 10, 21)), ('vacances_zone_a', True), ('vacances_zone_b', True), ('vacances_zone_c', True), ...}

# Get holiday dates for a given year and zone
d.holidays_for_year_and_zone(2017, 'A')
# Returns: {datetime.date(2017, 1, 1): OrderedDict([('date', datetime.date(2017, 01, 01)), ('vacances_zone_a', True), ('vacances_zone_b', True), ('vacances_zone_c', True), ...}

# Get holiday dates for a given year, zone and holiday name
d.holidays_for_year_zone_and_name(2017, 'A', 'Vacances de Noël')
# Returns: {datetime.date(2017, 1, 1): OrderedDict([('date', datetime.date(2017, 1, 1)), ('vacances_zone_a', True), ('vacances_zone_b', True), ('vacances_zone_c', True), ('nom_vacances', 'Vacances de Noël')]), ...}
```

## Zone names
Use the capital letters A, B or C.

## Holiday names
You can use the following holiday names:
- Vacances de Noël
- Vacances d'hiver
- Vacances de printemps
- Vacances d'été
- Vacances de la Toussaint
- Pont de l'Ascension (only for some years)

## Data
School holiday dates are coming from the ["Vacances scolaires par zones" opendata dataset](https://www.data.gouv.fr/fr/datasets/vacances-scolaires-par-zones/) available on data.gouv.fr.

## Bank holidays
Interested in bank holidays as well (jours fériés in French)? There is another pip package for this! Check out https://github.com/AntoineAugusti/jours-feries-france

## Notice
This software is available under the MIT license and was developed as part of the [Entrepreneur d'Intérêt Général program](https://entrepreneur-interet-general.etalab.gouv.fr) by the French government.

Projet développé dans le cadre du programme « [Entrepreneur d’intérêt général](https://entrepreneur-interet-general.etalab.gouv.fr) ».
