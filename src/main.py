import json
from data.names.convert import names_convert as names
from data.club.convert import club_convert as club

import os

club("./data/club/csv/club_teatchers.csv", "club_teatchers")
names("./data/names/csv/all_teatchers.csv", "all_teatchers")
