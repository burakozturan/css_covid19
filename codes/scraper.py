import twint
from datetime import datetime, timedelta
from utils.queuing import RedisOperations
from utils.upload import FileOperations

QUEUE_NAME = "keywords"
BUCKET_NAME = "data-mining-tria"

redis = RedisOperations()
files = FileOperations()


class Scraper(object):
    def __init__(self):
        self.c = twint.Config()
        self.c.Custom["tweet"] = ['id', 'date', 'time', 'user_id', 'username',
                                  'tweet', 'hashtags', 'retweet', 'user_rt',
                                  'mentions']
        self.c.Lang = "tr"
        self.c.Store_csv = True

    def get(self):
        return redis.get(QUEUE_NAME)

    def scrape(self):
        option = self.get()
        keyword = option.get("keyword")
        day = option.get("day")
        nxt = datetime.strptime(day, "%Y-%m-%d") + timedelta(days=1)
        self.c.Search = keyword
        self.c.Since = day
        self.c.Until = nxt.strftime("%Y-%m-%d")
        self.c.Output = keyword.__add__(f"_{day}.csv")
        self.c.Count = True
        twint.run.Search(self.c)
        return keyword.__add__(f"_{day}.csv")

    def run(self):
        filename = self.scrape()
        files.upload_file(filename, BUCKET_NAME, filename)   


scraper = Scraper()
scraper.run()
