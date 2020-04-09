#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:10:10 2020

@author: burak
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Those are revised code of [examples.py] written by Copyright (C) 2016 Pascal Jürgens and Andreas Jungherr (See License.txt).
# Revised by T.Kim.

# The code revision details:
# - Add time setting for Europe/Berlin
# - Add argument: print_user_archive(user)
# - Add argument and change file name setting: save_user_archive_to_file(user)
# - Add argument: save_user_archive_to_database(user)
# - Add argument: track_keywords(k_list)
# - Add argument: save_track_keywords(k_list)
# - change MST to LT var in all functions so that we can set arbitrary timezone
# - Add N argument for export_total functions. Originally, it only return top 50 total.
# - delete top_retweets(), export_retweet_text() due to error
# - Add new function export_retweets(), export_retweets_period(), export_top_retweets_daily()
# - Add two arguments indicating start date and stop date : export_user_counts(), export_mention_total(), export_url_total(),export_hashtag_total()
# - Add new function save_search_to_file(query,**kwargs)


"""
Examples for accessing the API
------------------------------
These are some examples demonstrating the use of provided functions for
gathering data from the Twitter API.

Requirements:
    - depends on API access modules rest.py and streaming.py
"""

import rest_for_seminar as rest
import streaming_for_seminar as streaming
import database_for_seminar as database
import logging
import json
import datetime
import peewee
from progress.bar import Bar
import csv
from pytz import timezone
from pytz import utc



# Time setting: put your timezone into LT var.
LT = timezone('Europe/Istanbul')
#LT = timezone("MST") # The Mountain Time Zone of North America keeps time by subtracting seven hours from Coordinated Universal Time (UTC).


#
# Setup
#


def hydrate(idlist_file="data/example_dataset_tweet_ids.txt"):
    """
    This function reads a file with tweet IDs and then loads them
    through the API into the database. Prepare to wait quite a bit,
    depending on the size of the dataset.
    """
    ids_to_fetch = set()
    for line in open(idlist_file, "r"):
        # Remove newline character through .strip()
        # Convert to int since that's what the database uses
        ids_to_fetch.add(int(line.strip()))
    # Find a list of Tweets that we already have
    ids_in_db = set(t.id for t in database.Tweet.select(database.Tweet.id))
    # Sets have an efficient .difference() method that returns IDs only present
    # in the first set, but not in the second.
    ids_to_fetch = ids_to_fetch.difference(ids_in_db)
    logging.warning(
        "\nLoaded a list of {0} tweet IDs to hydrate".format(len(ids_to_fetch)))

    # Set up a progressbar
    bar = Bar('Fetching tweets', max=len(ids_to_fetch), suffix='%(eta)ds')
    for page in rest.fetch_tweet_list(ids_to_fetch):
        bar.next(len(page))
        for tweet in page:
            database.create_tweet_from_dict(tweet)
    bar.finish()
    logging.warning("Done hydrating!")


def dehydrate(filename="data/dehydrated_tweet_ids.txt"):
    """
    This function writes the Tweet IDs contained in the current database to
    a file that allows re-hydration with the above method.
    """
    with open(filename, "w") as f:
        for tweet in database.Tweet.select(database.Tweet.id):
            f.write("{0}\n".format(tweet.id))


#
# Helper Functions
#


def print_tweet(tweet):
    """
    Print a tweet as one line:
    user: tweet
    """
    logging.warning(
        u"{0}: {1}".format(tweet["user"]["screen_name"], tweet["text"]))


def print_notice(notice):
    """
    This just prints the raw response, such as:
    {u'track': 1, u'timestamp_ms': u'1446089368786'}}
    """
    logging.error(u"{0}".format(notice))

#
# Examples for extracting Tweets
#


def import_json(fi):
    """
    Load json data from a file into the database.
    """
    logging.warning("Loading tweets from json file {0}".format(fi))
    for line in open(fi, "rb"):
        data = json.loads(line.decode('utf-8'))
        database.create_tweet_from_dict(data)


def print_user_archive(user):
    """
    Fetch all available tweets for one user and print them, line by line
    :param user: str indicating screen_name(without @) or user_id
    """
    archive_generator = rest.fetch_user_archive(user)
    for page in archive_generator:
        for tweet in page:
            print_tweet(tweet)


def save_user_archive_to_file(user):
    """
    Fetch all available tweets for one user and save them to a text file, one tweet per line.
    :param user: str indicating screen_name(without @) or user_id
    :return: a json file, named user-tweets.json, contains recent 3200 tweets published from the user.
    """
    filename = str(user).__add__('-tweets.json')
    with open(filename, "w") as f:
        archive_generator = rest.fetch_user_archive(user)
        for page in archive_generator:
            for tweet in page:
                f.write(json.dumps(tweet) + "\n")
    logging.warning(u"Wrote tweets from the user")


def save_user_archive_to_database(user):
    """
    Fetch all available tweets for one user and save them to the database.
    :param user: str indicating screen_name(without @) or user_id
    """
    archive_generator = rest.fetch_user_archive(user)
    for page in archive_generator:
        for tweet in page:
            database.create_tweet_from_dict(tweet)
    logging.warning(u"Wrote tweets from the user to database")


def print_list_of_tweets():
    """
    Fetch a list of three tweets by ID, then print them line by line
    This example can be easily adapted to write the tweets to a file, see above.
    """
    list_generator = rest.fetch_tweet_list(
        [62154131600224256, 662025716746354688, 661931648171302912, ])
    for page in list_generator:
        for tweet in page:
            print_tweet(tweet)


def track_keywords(k_list):
    """
    Track two keywords with a tracking stream and print machting tweets and notices.
    To stop the stream, press ctrl-c or kill the python process.
    :param: k_list: list of keywords
    """
    keywords = k_list
    stream = streaming.stream(
        on_tweet=print_tweet, on_notification=print_notice, track=keywords)


def save_track_keywords(k_list):
    """
    Track two keywords with a tracking stream and save machting tweets.
    To stop the stream, press ctrl-c or kill the python process.
    :param: k_list : list of keywords.
    """
    # Set up file to write to
    outfile = open("keywords_example.json", "w")

    def save_tweet(tweet):
        json.dump(tweet, outfile)
        # Insert a newline after one tweet
        outfile.write("\n")
    keywords = k_list
    try:
        stream = streaming.stream(
            on_tweet=save_tweet, on_notification=print_notice, track=keywords)
    except (KeyboardInterrupt, SystemExit):
        logging.error("User stopped program, exiting!")
        outfile.flush()
        outfile.close()


def follow_users():
    """
    Follow several users, printing their tweets (and retweets) as they arrive.
    To stop the stream, press ctrl-c or kill the python process.
    """
    # user IDs are: nytimes: 807095, washingtonpost: 2467791
    # they can be obtained through:
    # users = ["nytimes", "washingtonpost"]
    # users_json = rest.fetch_user_list_by_screen_name(screen_names=users)
    # for u in users_json:
    #   print("{0}: {1}".format(u["screen_name"], u["id"]))
    users = ["807095", "2467791"]
    stream = streaming.stream(
        on_tweet=print_tweet, on_notification=print_notice, follow=users)


def save_follow_users():
    """
    Follow several users, saving their tweets (and retweets) as they arrive.
    To stop the stream, press ctrl-c or kill the python process.
    """
    outfile = open("user_example.json", "w")

    def save_tweet(tweet):
        json.dump(tweet, outfile)
        # Insert a newline after one tweet
        outfile.write("\n")
    users = ["807095", "2467791"]
    stream = streaming.stream(
        on_tweet=save_tweet, on_notification=print_notice, follow=users)



def save_search_to_file(query,**kwargs):
    """
    Save search results using keywords (max period: last 7 days)
    :param query: query for search
    :param kwargs: parameter including 'since' and 'until', which indicate the period (utc)

    example:
    q = {'since': '2018-11-24','until':'2018-11-25', 'result_type': 'recent', 'lang':'de'}
    save_search_to_file('CDU', **q)

    if you want to use local time,

    start_date = LT.localize(datetime.datetime(2018,11,1))
    start_date = str(utc.normalize(start_date).date())

    set start_date as 'since' value and do the same for 'until'

    """
    with open("search.json","w") as f:
        generator = rest.search_tweets_period(query,**kwargs)
        for page in generator:
            for tweet in page:
                f.write(json.dumps(tweet)+"\n")
    logging.warning(u"Wrote tweets from search keyword to json file.")



#
# Examples for extracting results from database
#

def export_total_counts(interval="day",start_date = None, stop_date = None):
    """
    Create hourly counts for Tweets
    """
    # Create output file
    with open("total_counts.csv", "w") as f:
        # Write header line
        f.write("{0},".format(interval))
        f.write("total,")
        f.write("\n")
        # Prepare interator over intervals
        intervals = database.objects_by_interval(
            database.Tweet, interval=interval, start_date=start_date, stop_date=stop_date)
        for (interval_start, interval_stop), query in intervals:
            # Convert the timestamp to Mountain Standard Time which is
            # the local timezone for the example data
            timestamp = LT.normalize(interval_start).strftime(
                "%Y-%m-%d %H:%M:%S %z")
            f.write("{0},".format(timestamp))
            f.write("{0},".format(query.count()))
            f.write("\n")


def export_featureless_counts(interval="day"):
    """
    Create hourly counts for Tweets without mentions or URLs.
    Complex queries on many-to-many-relationships are very
    contrived with peewee. For the sake of simplicity, this
    function instead
    """
    # Create output file
    with open("featureless_counts.csv", "w") as f:
        # Write header line
        f.write("{0},".format(interval))
        f.write("featureless,")
        f.write("\n")
        # Prepare interator over intervals
        intervals = database.objects_by_interval(
            database.Tweet, interval=interval, start_date=None, stop_date=None)
        for (interval_start, interval_stop), query in intervals:
            # Convert the timestamp to Mountain Standard Time which is
            # the local timezone for the example data
            timestamp = LT.normalize(interval_start).strftime(
                "%Y-%m-%d %H:%M:%S %z")
            f.write("{0},".format(timestamp))
            featureless_count = 0
            for t in query:
                if bool(t.mentions.is_null() and t.urls.is_null() and t.reply_to_tweet is None):
                    featureless_count += 1
            f.write("{0},".format(featureless_count))
            f.write("\n")


def export_mention_totals(n=50,
                          start_date = LT.localize(datetime.datetime(2018, 11, 1, 0)),
                          stop_date = LT.localize(datetime.datetime(2018, 11, 13, 23, 59))):
    """
    Export the N most mentioned users and their respective counts to
    a CSV file.
    :param: n: int
    """
    start_date = start_date
    stop_date = stop_date
    with open("mention_totals.csv", "w") as f:
        f.write("user, mentions\n")
        for user in database.mention_counts(start_date, stop_date)[:n]:
            f.write("{0}, {1}\n".format(user.username, user.count))


def export_url_totals(n=50,
                      start_date=LT.localize(datetime.datetime(2018, 11, 1, 0)),
                      stop_date=LT.localize(datetime.datetime(2018, 11, 13, 23, 59))):
    """
    Export the N most mentioned URLs and their respective counts to
    a CSV file.
    :param: n: int
    """
    start_date = start_date
    stop_date = stop_date
    with open("url_totals.csv", "w") as f:
        f.write("url, mentions\n")
        for url in database.url_counts(start_date, stop_date)[:n]:
            f.write("{0}, {1}\n".format(url.url, url.count))


def export_hashtag_totals(n=50,
                          start_date=LT.localize(datetime.datetime(2018, 11, 1, 0)),
                          stop_date=LT.localize(datetime.datetime(2018, 11, 13, 23, 59))):
    """
    Export the N most mentioned hashtags and their respective counts to
    a CSV file.
    :param: n: int
    """
    start_date = start_date
    stop_date = stop_date
    with open("hashtag_totals.csv", "w") as f:
        f.write("hashtag, mentions\n")
        for hashtag in database.hashtag_counts(start_date, stop_date)[:n]:
            f.write("{0}, {1}\n".format(hashtag.tag, hashtag.count))


def export_retweet_totals(n=50,
                          start_date=LT.localize(datetime.datetime(2018, 11, 1, 0)),
                          stop_date=LT.localize(datetime.datetime(2018, 11, 13, 23, 59))):
    """
    Export the N most retweeted users and their respective counts to
    a CSV file.
    :param: n: int
    """
    start_date = start_date
    stop_date = stop_date
    with open("retweet_totals.csv", "w") as f:
        f.write("user, retweets\n")
        retweetcounts = database.retweet_counts(
            start_date, stop_date, n).items()
        for username, count in retweetcounts:
            f.write("{0}, {1}\n".format(username, count))


def export_hashtag_counts(interval="day", hashtags=["Bush"], start_date= None, stop_date=None):
    """
    Create daily counts for given Hashtags. A bit slow. An easy speedup is to convert the list of hashtags to Hashtag database objects and query for them.
    :param: keywords: list of keywords
    :param: start_date
    :param: stop_date
    """
    # Create output file
    with open("hashtag_counts.csv", "w") as f:
        # Write header line
        f.write("{0},".format(interval))
        f.write(",".join(hashtags))
        f.write(",\n")
        # Prepare interator over intervals
        # htm is an intermediary model for many-to-many-relationships
        # In this case Tweet -> htm -> Hashtag
        htm = database.Tweet.tags.get_through_model()
        intervals = database.objects_by_interval(
            database.Tweet, interval=interval, start_date=start_date, stop_date=stop_date)
        for (interval_start, interval_stop), query in intervals:
            # Convert the timestamp to Mountain Standard Time which is
            # the local timezone for the example data
            timestamp = LT.normalize(interval_start).strftime(
                "%Y-%m-%d %H:%M:%S %z")
            f.write("{0},".format(timestamp))
            for tag in hashtags:
                # Match ignoring case
                count = query.join(htm).join(database.Hashtag).where(
                    peewee.fn.Lower(database.Hashtag.tag) == tag.lower()).count()
                f.write("{0},".format(count))
            f.write("\n")


def export_mention_counts(interval="day", usernames=["jebbush"], start_date=None, stop_date=None):
    """
    Create daily counts for mentions of given Users.
    :param: keywords: list of keywords
    :param: start_date
    :param: stop_date
    """
    # Create output file
    with open("mention_counts.csv", "w") as f:
        # Write header line
        f.write("{0},".format(interval))
        f.write(",".join(usernames))
        f.write(",\n")
        # Prepare interator over intervals
        # htm is an intermediary model for many-to-many-relationships
        # In this case Tweet -> htm -> Hashtag
        mtm = database.Tweet.mentions.get_through_model()
        intervals = database.objects_by_interval(
            database.Tweet, interval=interval, start_date=start_date, stop_date=stop_date)
        for (interval_start, interval_stop), query in intervals:
            # Convert the timestamp to Mountain Standard Time which is
            # the local timezone for the example data
            timestamp = LT.normalize(interval_start).strftime(
                "%Y-%m-%d %H:%M:%S %z")
            f.write("{0},".format(timestamp))
            for user in usernames:
                # Match ignoring case
                count = query.join(mtm).join(database.User).where(
                    peewee.fn.Lower(database.User.username) == user.lower()).count()
                f.write("{0},".format(count))
            f.write("\n")


def export_keyword_counts(interval="day", keywords=["Bush"], start_date=None, stop_date=None):
    """
    Create daily counts for given Keywords.
    :param: keywords: list of keywords
    :param: start_date
    :param: stop_date
    """
    # Create output file
    with open("keyword_counts.csv", "w") as f:
        # Write header line
        f.write("{0},".format(interval))
        f.write(",".join(keywords))
        f.write(",\n")
        # Prepare interator over intervals
        intervals = database.objects_by_interval(
            database.Tweet, interval=interval, start_date=start_date, stop_date=stop_date)
        for (interval_start, interval_stop), query in intervals:
            # Convert the timestamp to Mountain Standard Time which is
            # the local timezone for the example data
            timestamp = LT.normalize(interval_start).strftime(
                "%Y-%m-%d %H:%M:%S %z")
            f.write("{0},".format(timestamp))
            for word in keywords:
                # Match ignoring case
                kwcount = query.where(
                    peewee.fn.Lower(database.Tweet.text).contains(word.lower())).count()
                f.write("{0},".format(kwcount))
            f.write("\n")


def export_user_counts(interval="day", usernames=["JebBush"], start_date = None, stop_date= None):
    """
    Create daily counts for given Users.
    :param: interval
    :param: usernames: list of usernames
    :param: start_date
    :param: stop_date
    """
    # Create output file
    with open("user_counts.csv", "w") as f:
        # Write header line
        f.write("{0},".format(interval))
        f.write(",".join(usernames))
        f.write(",\n")
        # Prepare interator over intervals
        intervals = database.objects_by_interval(
            database.Tweet, interval=interval, start_date=start_date, stop_date=stop_date)
        for (interval_start, interval_stop), query in intervals:
            # Convert the timestamp to local Time
            timestamp = LT.normalize(interval_start).strftime(
                "%Y-%m-%d %H:%M:%S %z")
            f.write("{0},".format(timestamp))
            for username in usernames:
                # Match precise username
                ucount = query.join(database.User).where(
                    database.User.username == username).count()
                f.write("{0},".format(ucount))
            f.write("\n")



"""
Retweets
"""


def top_retweets_straight(n=50):
    """
    Get N most retweeted Tweets directly via the database.
    The query logic is a bit contrived.

    Returns tweet objects which are actually retweets but contain
    the retweet count as attribute "rt_count". To get the original (retweeted) Tweet,
    refer to the "retweet_id" and "retweet" fields.

    Example:
    for tweet in top_retweets_straight():
        print(tweet.rt_count, tweet.retweet.id, tweet.retweet.text)

    """
    # Alias for RT count
    rt_count = peewee.fn.Count(database.Tweet.retweet_id)
    # Directly aggregate in DB by counting retweet_id field and then grouping
    # by current tweet id.
    retweets = (
        database.Tweet
        .select(database.Tweet, rt_count.alias("rt_count"))
        .where(database.Tweet.retweet_id > 0)
        .group_by(database.Tweet.retweet_id)
        .order_by(rt_count.desc())
    )
    return retweets.limit(n)



def export_retweets(n=50):
    """
    Export csv file contains top N top retweeted tweets in the whole period.
    It exports count, username, text.
    :param n: number of top retweets to be exported
    """
    rt_count = peewee.fn.COUNT(database.Tweet.retweet_id)
    retweets = (
        database.Tweet
        .select(database.Tweet, rt_count.alias("rt_count"))
        .where(database.Tweet.retweet_id > 0)
        .group_by(database.Tweet.retweet_id)
        .order_by(rt_count.desc())
    )
    with open('retweet_top_text.csv', "w", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["count", "user","text"])
        for tweet in retweets.limit(n):
            tweet_list = [tweet.rt_count,tweet.retweet.user.username,tweet.retweet.text]
            writer.writerow(tweet_list)




def export_retweets_period(n=50,
                           start_date=LT.localize(datetime.datetime(2018, 11, 1, 0)),
                           stop_date=LT.localize(datetime.datetime(2018, 11, 13, 23)),
                           filename="retweet_top_text_period.csv"):
    """
    Export csv file contains top N retweets during indicated periods.
    :param n: number of top retweets to be export
    :param start_date:
    :param stop_date:
    :param filename: name of csv file (str)
    """
    retweets = (
        database.Tweet
        .select(database.Tweet, peewee.fn.COUNT(database.Tweet.retweet_id).alias("rt_count"))
        .where((database.Tweet.retweet_id > 0)
               & (database.Tweet.date>= database.to_utc(start_date))
               & (database.Tweet.date < database.to_utc(stop_date)))
        .group_by(database.Tweet.retweet_id)
        .order_by(peewee.fn.COUNT(database.Tweet.retweet_id).desc())
    )
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["count", "user","text"])
        for tweet in retweets.limit(n):
            tweet_list = [tweet.rt_count,tweet.retweet.user.username,tweet.retweet.text]
            writer.writerow(tweet_list)



def export_top_retweets_daily(start_date, stop_date, day = 1):
    """
    Export top 50 retweets daily.
    :param start_date:
    :param stop_date:
    :param day: step of days
    """
    kara = start_date
    made = start_date + datetime.timedelta(days=day)
    while made <= stop_date:
        print("now exporting", kara.date(), 'to', made.date())
        filename= str(kara.date()).__add__('_').__add__(str(made.date()).__add__('.csv'))
        export_retweets_period(start_date=kara, stop_date=made, filename=filename)
        kara = made
        made = made + datetime.timedelta(days=day)
