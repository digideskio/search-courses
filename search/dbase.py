import json
from search.models import CoursesModel

class DataBase():
    def save(self, name, address):
        if not CoursesModel.objects.filter(key=str(name)).exists():
            objects = CoursesModel.objects.create(
                key = str(name),
                address = str(address)
            )
            objects.save()

    def get(self, key):
        if not CoursesModel.objects.filter(key=str(key)).exists():
            raise KeyError('invalid')
        value = CoursesModel.objects.get(name=str(key)).__str__()
        return json.loads(value)
