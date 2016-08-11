from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel
from colorful.fields import RGBColorField

class YearMonthField(models.CharField):
    "A model field for storing dates without days"
    default_error_messages = {
        'invalid': _('Enter a valid year and month.'),
    }

    def __init__(self, input_formats=None, *args, **kwargs):
        super(YearMonthField, self).__init__(*args, **kwargs)
        self.input_formats = input_formats

    def clean(self, value):
        if value in validators.EMPTY_VALUES:
            return None
        if isinstance(value, datetime.datetime):
            return format(value, '%b, %Y')
        if isinstance(value, datetime.date):
            return format(value, '%b, %Y')
        for fmt in self.input_formats or YEARMONTH_INPUT_FORMATS:
            try:
                date = datetime.date(*time.strptime(value, fmt)[:3])
                return format(date, '%b, %Y')
            except ValueError:
                continue
        raise ValidationError(self.error_messages['invalid'])

class BasicInformation(SingletonModel):
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
    image = models.ImageField(upload_to="images", blank=True)

    def __repr__(self):
        return '<BasicInformation: %s>' % self.name

    def __str__(self):
        return self.name.title()


class Education(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name=_("University name"))
    abbreviation = models.CharField(max_length=10,
                                    blank=True,
                                    default=None,
                                    verbose_name=_("Degree abbreviation"))
    start_date = YearMonthField(max_length=9, null=True, blank=True,
                                  verbose_name=_("start date"))
    end_date = YearMonthField(max_length=9, null=True,
                                blank=True,
                                verbose_name=_("end date"))
    major = models.CharField(max_length=50,
                             blank=True,
                             default=None)
    gpa = models.CharField(max_length=10,
                           blank=True,
                           default=None,
                           verbose_name=_("GPA"))

    def __repr__(self):
        return '<Education: %s>' % self.name

    def __str__(self):
        return '%s in %s' % (self.abbreviation, self.major)

    def save(self, *args, **kwargs):
        self.clean()
        return super(self.__class__, self).save(*args, **kwargs)

    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError({"start_date": _("Start date must be "
                                                       "before end date."),
                                       "end_date": _("Start date must be "
                                                     "before end date.")})

    class Meta:
        ordering = ['-end_date']


class Publication(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=200,
                               blank=True)
    conference = models.CharField(max_length=200,
                                  blank=True)
    abstract = models.TextField(blank=True)
    year = models.CharField(max_length=4,
                            blank=True)
    link = models.URLField(blank=True)

    def __repr__(self):
        return '<Publication: %s>' % self.name

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-year']


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default=None,
                                   blank=True,
                                   verbose_name=_("description"))
    start_date = YearMonthField(max_length=9, null=True,
                                  blank=True,
                                  verbose_name=_("start date"))
    end_date = YearMonthField(max_length=9, null=True,
                                blank=True,
                                verbose_name=_("end date"))
    link = models.URLField(blank=True)

    def __repr__(self):
        return '<Project: %s>' % self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.clean()
        return super(self.__class__, self).save(*args, **kwargs)

    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError({"start_date": _("Start date must be "
                                                       "before end date."),
                                       "end_date": _("Start date must be "
                                                     "before end date.")})

    def get_languages(self):
        languages = Language.objects.all()
        used_languages = []
        for language in languages:
            try:
                language.projects.get(pk=self.pk)
                used_languages.append(language)
            except ObjectDoesNotExist:
                pass
        return {self: used_languages}


class Experience(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=150)
    start_date = YearMonthField(max_length=9, null=True,
                                  blank=True,
                                  verbose_name=_("start date"))
    end_date = YearMonthField(max_length=9, null=True,
                                blank=True,
                                verbose_name=_("end date"))
    description = models.TextField(default=None,
                                   verbose_name=_("description"))
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to="images",
                              blank=True)

    def __repr__(self):
        return '<Experience: %s>' % self.company

    def __str__(self):
        return '%s at %s' % (self.role.capitalize(), self.company)

    class Meta:
        ordering = ['-end_date']

    def save(self, *args, **kwargs):
        self.clean()
        return super(self.__class__, self).save(*args, **kwargs)

    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError({"start_date": _("Start date must be "
                                                       "before end date."),
                                       "end_date": _("Start date must be "
                                                     "before end date.")})

    def get_languages(self):
        languages = Language.objects.all()
        used_languages = []
        for language in languages:
            try:
                language.experience.get(pk=self.pk)
                used_languages.append(language.name)
            except ObjectDoesNotExist:
                pass
        return {self: used_languages}


class Language(models.Model):
    name = models.CharField(max_length=50)
    experience = models.ManyToManyField(Experience,
                                        blank=True)
    projects = models.ManyToManyField(Project,
                                      blank=True)

    def __repr__(self):
        return '<Language: %s>' % self.name

    def __str__(self):
        return self.name


class Settings(SingletonModel):
    base_color = RGBColorField(blank=False,
                               verbose_name=_("Base color"),
                               default="bc0000")

    def __repr__(self):
        return '<Settings: %s>' % self.base_color

    def __str__(self):
        return 'Settings Singleton'
