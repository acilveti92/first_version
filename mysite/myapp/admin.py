from django.contrib import admin

import mysite.myapp.models as myapp_models


admin.site.register(myapp_models.Word)
admin.site.register(myapp_models.WordsUse)
admin.site.register(myapp_models.WordAjaxModel)
