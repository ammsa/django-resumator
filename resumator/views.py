from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import BasicInformation
from .models import Project
from .models import Experience
from .models import Publication
from .models import Education

from resumator import utils


def about(request):
    template = loader.get_template('resumator/index.html')
    basic_information = BasicInformation.objects.get()
    context_dict = {"resumator_basicinformation": basic_information}
    context = RequestContext(request,
                             utils.used_models(context_dict))
    return HttpResponse(template.render(context))


def projects(request):
    basic_information = BasicInformation.objects.latest('pk')
    projects_list = Project.objects.all()
    used_languages = {}
    for project in projects_list:
        used_languages.update(project.get_languages())
    template = loader.get_template('resumator/projects.html')
    context_dict = {'resumator_basicinformation': basic_information,
                    'resumator_project': projects_list,
                    'used_languages': used_languages,
                    }
    print context_dict
    context = RequestContext(request,
                             utils.used_models(context_dict,
                                               ignore_models=["resumator_language"]))
    return HttpResponse(template.render(context))


def experience(request):
    basic_information = BasicInformation.objects.latest('pk')
    experience_list = Experience.objects.all()
    used_languages = {}
    for experience in experience_list:
        used_languages.update(experience.get_languages())
    template = loader.get_template('resumator/experience.html')
    context_dict = {'resumator_basicinformation': basic_information,
                    'resumator_experience': experience_list,
                    'used_languages': used_languages,
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    return HttpResponse(template.render(context))


def publications(request):
    basic_information = BasicInformation.objects.latest('pk')
    publication_list = Publication.objects.all()
    template = loader.get_template('resumator/publications.html')
    context_dict = {'resumator_basicinformation': basic_information,
                    'resumator_publication': publication_list,
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    return HttpResponse(template.render(context))


def education(request):
    basic_information = BasicInformation.objects.latest('pk')
    education_list = Education.objects.all()
    template = loader.get_template('resumator/education.html')
    context_dict = {'resumator_basicinformation': basic_information,
                    'resumator_education': education_list,
                    }
    context = RequestContext(request,
                             utils.used_models(context_dict))
    return HttpResponse(template.render(context))
