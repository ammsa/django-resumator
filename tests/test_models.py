from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from datetime import datetime
from datetime import timedelta

from .models import TestBasicInformation as BasicInformation
from .models import TestExperience as Experience
from .models import TestEducation as Education
from .models import TestProject as Project
from .models import TestPublication as Publication
from .models import TestLanguage as Language


class BasicInformationTestCase(TestCase):

    def test_multiple_basic_information__raises_IntegrityError(self):
            with self.assertRaises(IntegrityError):
                BasicInformation.objects.create(name="James")
                BasicInformation.objects.create(name="John")


class EducationTestCase(TestCase):

    def test_start_date_after_end_date__raises_ValidationError(self):
            with self.assertRaises(ValidationError):
                today = datetime.today()
                yesterday = datetime.now() - timedelta(hours=24)
                Education.objects.create(name="blah",
                                         abbreviation="blah",
                                         start_date=today,
                                         end_date=yesterday,
                                         major="blah",
                                         gpa="4.0")


class ExperienceTestCase(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(company="blah",
                                                    description="blah")

    def test_start_date_after_end_date__raises_ValidationError(self):
        with self.assertRaises(ValidationError):
            today = datetime.today()
            yesterday = datetime.now() - timedelta(hours=24)
            Experience.objects.create(company="blah",
                                      role="blah",
                                      start_date=today,
                                      end_date=yesterday)

    def test_project_with_languages_assigned__returns_languages(self):
        python = Language.objects.create(name="Python")
        django = Language.objects.create(name="Django")
        python.experience.add(self.experience)
        django.experience.add(self.experience)
        expected = {self.experience: [python, django]}
        self.assertDictEqual(expected, self.experience.get_languages())


class ProjectTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name="blah",
                                              description="blah")

    def test_start_date_after_end_date__raises_ValidationError(self):
        with self.assertRaises(ValidationError):
            today = datetime.today()
            yesterday = datetime.now() - timedelta(hours=24)
            Project.objects.create(name="blah",
                                   description="blah",
                                   start_date=today,
                                   end_date=yesterday)

    def test_project_with_languages_assigned__returns_languages(self):
        python = Language.objects.create(name="Python")
        django = Language.objects.create(name="Django")
        python.projects.add(self.project)
        django.projects.add(self.project)
        expected = {self.project: [python, django]}
        self.assertDictEqual(expected, self.project.get_languages())


class PublicationTestCase(TestCase):
    pass


class LanguageTestCase(TestCase):
    pass
