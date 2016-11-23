import requests

from background_task import background
from search.models import CoursesModel
from search import settings

def TaskSearchCourses():
    import ipdb
    ipdb.set_trace()
    print "aaaaa"
    start = 1
    key = settings.KEY
    cx = settings.CX
    url = "https://www.googleapis.com/customsearch/v1"
    q = "key={}&cx={}".format(key, cx)
    search = "q={}".format("english%20online%20course")
    fmt = "filter=1&start={}&num=10&alt=json".format(start)
    url = "{}?{}&{}&{}".format(
        url,
        q,
        search,
        fmt
    )
    values = requests.get(url)
    items = values.json().get('items')
    for item in items:
        print "save"
        CoursesModel().save(
            item.get('title'),
            item.get('formattedUrl')
        )
