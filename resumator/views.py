from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import BasicInformation
from .models import Project
from .models import Experience
from .models import Publication
from .models import Education
from .models import Settings
from resumator import utils


def about(request):
    settings = Settings.objects.get()
    basic_information = BasicInformation.objects.get()
    context_dict = {"resumator_basicinformation": basic_information,
                    "resumator_settings": settings}
    context = RequestContext(request,
                             utils.used_models(context_dict))
    template = loader.get_template('resumator/index.html')
    return HttpResponse(template.render(context))


def projects(request):
    settings = Settings.objects.get()
    basic_information = BasicInformation.objects.latest('pk')
    projects_list = Project.objects.all()
    used_languages = {}
    for project in projects_list:
        used_languages.update(project.get_languages())
    context_dict = {'resumator_basicinformation': basic_information,
                    'resumator_project': projects_list,
                    'used_languages': used_languages,
                    "resumator_settings": settings
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict,
                                               ignore_models=["resumator_language"]))
    template = loader.get_template('resumator/projects.html')
    return HttpResponse(template.render(context))


def experience(request):
    settings = Settings.objects.get()
    basic_information = BasicInformation.objects.latest('pk')
    experience_list = Experience.objects.all()
    used_languages = {}
    for experience in experience_list:
        used_languages.update(experience.get_languages())
    context_dict = {'resumator_basicinformation': basic_information,
                    'resumator_experience': experience_list,
                    'used_languages': used_languages,
                    "resumator_settings": settings
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    template = loader.get_template('resumator/experience.html')
    return HttpResponse(template.render(context))


def publications(request):
    settings = Settings.objects.get()
    basic_information = BasicInformation.objects.latest('pk')
    publication_list = Publication.objects.all()
    context_dict = {'resumator_basicinformation': basic_information,
                    'resumator_publication': publication_list,
                    "resumator_settings": settings
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    template = loader.get_template('resumator/publications.html')
    return HttpResponse(template.render(context))


def education(request):
    settings = Settings.objects.get()
    basic_information = BasicInformation.objects.latest('pk')
    education_list = Education.objects.all()
    context_dict = {'resumator_basicinformation': basic_information,
                    'resumator_education': education_list,
                    "resumator_settings": settings
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    template = loader.get_template('resumator/education.html')
    return HttpResponse(template.render(context))
