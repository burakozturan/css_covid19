import itertools
from datetime import date, timedelta
from utils.queuing import RedisOperations


QUEUE_NAME = "keywords"

KEYWORDS = ['işsizlik', 'ekonomi', 'destek']

START_DATE = date(2020, 2, 25)
END_DATE = date(2020, 5, 15)

redis = RedisOperations()


def get_dates(sdate, edate):
    days = []
    delta = edate - sdate
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        day = day.strftime("%Y-%m-%d")
        days.append(day)
    return days


def run():
    dates = get_dates(START_DATE, END_DATE)
    search_matrix = itertools.product(KEYWORDS, dates)
    for keyword, day in search_matrix:
        option = {
            "day": day,
            "keyword": keyword
        }
        redis.put(QUEUE_NAME, option)
    print('Keyword and date matrices loaded.')


if __name__ == "__main__":
    run()
