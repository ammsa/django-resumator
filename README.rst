=====
Resumator
=====

Resumator is a lightwight app to create web-based resumes.

Quick start
-----------

1. Add "resumator" to your INSTALLED_APPS setting like this::

       INSTALLED_APPS = (
               ...
               'resumator',
       )

2. Add the following to your setting.py::

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/'

2. Include the resumator URLconf in your project urls.py and add MEDIA URL to urlpatterns like this::

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        ...
        url(r'^', include('resumator.urls')),
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


3. Run `python manage.py migrate` to create the resumator models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to modify your basic information model and edit your resume (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/resume/ to see your resume.
