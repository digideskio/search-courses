import requests

from background_task import background
from search.models import CoursesModel
from search import settings

@background(schedule=60*5)
def TaskSearchCourses():
    start = 1
    key = settings.KEY
    cx = settings.CX
    url = "https://www.googleapis.com/customsearch/v1"
    q = "key={}&cx={}".format(key, cx)
    search = "q={}".format("courses")
    fmt = "filter=1&start={}&num=10&alt=json".format(start)
    url = "{}?{}?{}?{}".format(
        url,
        q,
        search,
        fmt
    )
    values = requests.get(url)
    import ipdb
    ipdb.set_trace()
