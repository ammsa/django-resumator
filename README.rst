=====
django-resumator
=====
|pypi| |travis|


django-resumator is a lightwight app to create web-based resumes. Please visit `theresumator`_ for a django project that uses it. 



installation
-----------
    
       pip install django-resumator

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
            url(r'^resume/', include('resumator.urls')),
            ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


3. Run `python manage.py migrate` to create the resumator models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to modify your basic information model and edit your resume (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/resume/ to see your resume.


Contributing
-----------

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

License
-----------

All parts of theresumator are free to use and abuse under the `open-source MIT license`_.

.. |pypi| image:: https://badge.fury.io/py/django-resumator.svg
   :target: https://badge.fury.io/py/django-resumator
.. |travis| image:: https://travis-ci.org/AmmsA/django-resumator.svg?branch=master
   :alt: Build Status - master branch
   :target: https://travis-ci.org/AmmsA/django-resumator
.. _`theresumator`: https://github.com/AmmsA/theresumator
.. _`open-source MIT license`: https://github.com/AmmsA/django-resumator/blob/master/LICENSE

