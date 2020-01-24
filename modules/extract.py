from datetime import datetime


def get_arrest_date(arrest_date):
    if len(arrest_date) == 3:
        arrest_date = datetime.strptime(" ".join(arrest_date), "%B %d %Y").strftime("%m/%d/%Y")
    elif len(arrest_date[1]) <= 2:
        arrest_date = datetime.strptime(" ".join(arrest_date), "%B %d").strftime("%m/%d")
    else:
        arrest_date = datetime.strptime(" ".join(arrest_date), "%B %Y").strftime("%m/%Y")
    return arrest_date
