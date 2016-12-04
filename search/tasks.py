import requests
import logging

from background_task import background
from search.dbase import DataBase
from search import settings

#  @background(schedule=60*20)
def TaskSearchCourses():
    querys = ["english%20online%20course", "curso%20ingles%20online", "curso%20online%20interativo"]
    key = settings.KEY
    cx = settings.CX
    url_base = "https://www.googleapis.com/customsearch/v1"
    q = "key={}&cx={}".format(key, cx)
    for query in querys:
        print "search for query: %s" % query
        search = "q={}".format(query)
        for start in range(0, 5):
            print "search page: %s" % start
            logging.debug("search page: %s" % start)
            fmt = "filter=1&start={}&num=10&alt=json".format(start*10 + 1)
            url = "{}?{}&{}&{}".format(
                url_base,
                q,
                search,
                fmt
            )
            print "URL: %s" % url
            response = requests.get(url)
            if response.status_code == 200:
                items = response.json().get('items')
                DataBase().save(items)
                logging.debug("page done: %s" % start)
                print "page done: %s" % start
            else:
                logging.debug("Error in page: {}, status: {}".format(
                    start,
                    response.status_code)
                )
                print "Error in page: {}, status: {}".format(
                    start,
                    response.status_code
                )
    #  TaskSearchCourses()
