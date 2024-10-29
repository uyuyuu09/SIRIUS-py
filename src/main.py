from data.names.convert import names_convert as names
from data.club.convert import club_names, names_club
from data.mix import set_full_names

try:
    names("./data/names/csv/all_teatchers.csv", "all_teatchers")
    names_club("./data/club/csv/club_teatchers.csv", "names_club")
    club_names("./data/club/csv/club_teatchers.csv", "club_names")
    set_full_names("all_teatchers", "names_club")
    print("success", "処理成功")
except:
    print("error", "処理失敗")