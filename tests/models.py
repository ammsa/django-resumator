from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from solo.models import SingletonModel


class TestBasicInformation(SingletonModel):
    name = models.CharField(max_length=25,
                            default="John Smith")
    short_bio = models.CharField(max_length=100,
                                 blank=True,
                                 verbose_name=_("short bio"),
                                 default="My short bio")
    long_bio = models.TextField(blank=True,
                                verbose_name=_("long bio"),
                                default="My long bio")
    email = models.EmailField(default="email@example.com")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    image = models.ImageField(upload_to="media/images", blank=True)


class TestEducation(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name=_("University name"))
    abbreviation = models.CharField(max_length=10,
                                    blank=True,
                                    default=None,
                                    verbose_name=_("Degree abbreviation"))
    start_date = models.DateField(null=True, blank=True,
                                  verbose_name=_("start date"))
    end_date = models.DateField(null=True,
                                blank=True,
                                verbose_name=_("end date"))
    major = models.CharField(max_length=50,
                             blank=True,
                             default=None)
    gpa = models.CharField(max_length=10,
                           blank=True,
                           default=None,
                           verbose_name=_("GPA"))

    def save(self, *args, **kwargs):
        self.clean()
        return super(self.__class__, self).save(*args, **kwargs)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError({"start_date": _("Start date must be before end date."),
                                   "end_date": _("Start date must be before end date.")})

    class Meta:
        ordering = ['-end_date']


class TestPublication(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=200,
                               blank=True)
    conference = models.CharField(max_length=200,
                                  blank=True)
    abstract = models.TextField(blank=True)
    year = models.CharField(max_length=4,
                            blank=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ['-year']


class TestProject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default=None,
                                   blank=True,
                                   verbose_name=_("description"))
    start_date = models.DateField(null=True,
                                  blank=True,
                                  verbose_name=_("start date"))
    end_date = models.DateField(null=True,
                                blank=True,
                                verbose_name=_("end date"))
    link = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        self.clean()
        return super(self.__class__, self).save(*args, **kwargs)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError({"start_date": _("Start date must be before end date."),
                                   "end_date": _("Start date must be before end date.")})

    def get_languages(self):
        languages = TestLanguage.objects.all()
        used_languages = []
        for language in languages:
            try:
                language.projects.get(pk=self.pk)
                used_languages.append(language)
            except ObjectDoesNotExist:
                pass
        return {self: used_languages}


class TestExperience(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=150)
    start_date = models.DateField(null=True,
                                  blank=True,
                                  verbose_name=_("start date"))
    end_date = models.DateField(null=True,
                                blank=True,
                                verbose_name=_("end date"))
    description = models.TextField(default=None,
                                   verbose_name=_("description"))
    link = models.URLField(blank=True)
    image = models.ImageField(blank=True)

    class Meta:
        ordering = ['-end_date']

    def save(self, *args, **kwargs):
        self.clean()
        return super(self.__class__, self).save(*args, **kwargs)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError({"start_date": _("Start date must be before end date."),
                                   "end_date": _("Start date must be before end date.")})

    def get_languages(self):
        languages = TestLanguage.objects.all()
        used_languages = []
        for language in languages:
            try:
                language.experience.get(pk=self.pk)
                used_languages.append(language)
            except ObjectDoesNotExist:
                pass
        return {self: used_languages}


class TestLanguage(models.Model):
    name = models.CharField(max_length=50)
    experience = models.ManyToManyField(TestExperience,
                                        blank=True)
    projects = models.ManyToManyField(TestProject,
                                      blank=True)
