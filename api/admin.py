from django.contrib import admin
#
# from api.models.actividade import Actividade
# from api.models.assinante import Assinante
from django.contrib import admin
from django.apps import apps

# Get all models from the 'api' app
api_models = apps.get_app_config('api').get_models()

# Register all models from the 'api' app
for model in api_models:
    admin.site.register(model)


# Register your models here.
# admin.site.register(Actividade, Assinante)


