from django.contrib import admin

# Register your models here.
from fakereview.models import RegistrationModel, ProductModel,CommentModel,SearchHistoryModel,LikeOrDisLikeModel

admin.site.register(RegistrationModel)
admin.site.register(ProductModel)
admin.site.register(CommentModel)
admin.site.register(SearchHistoryModel)
admin.site.register(LikeOrDisLikeModel)
