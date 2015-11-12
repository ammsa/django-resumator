from django.contrib import admin
from django.db.utils import OperationalError
from solo.admin import SingletonModelAdmin

from models import BasicInformation
from models import Project
from models import Experience
from models import Language
from models import Publication
from models import Education


admin.site.register(BasicInformation, SingletonModelAdmin)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Language)
admin.site.register(Publication)
admin.site.register(Education)


# make BasicInformation singleton if it does not already exist
try:
    basic_information = BasicInformation.get_solo()
except OperationalError:
    pass

