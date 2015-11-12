from django.apps import apps


def used_models(context_dict, ignore_models=None):
        """
        Checks if models other than whats in `context_dict` or `ignore_models`
        have atleast a single instance in db
        :return context_dict: dict containing already assigned objects.
                              sets models names as key and value set to True
                              if they have atleast a single instance in db.
                              Ignores models in `ignore_models`
        """
        app_models = apps.get_app_config('resumator').get_models()
        for model in app_models:
            if model._meta.db_table in context_dict or \
               ignore_models and model._meta.db_table in ignore_models:
                pass
            else:
                if model.objects.all():
                    context_dict[model._meta.db_table] = True
        return context_dict
