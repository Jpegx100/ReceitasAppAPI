from django.conf.urls import url
from django.contrib import admin
from core.views.recipe import *
from core.views.user import *
from core.views.comment import *
from core.views.feel import *
from core.views.ingredient_type import *
from core.views.ingredient import *
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='ReceitasAPP API')

urlpatterns = [
    # url(r'^comments/$', CommentList.as_view()),
    # url(r'^comments/(?P<pk>[0-9]+)/$', CommentDetail.as_view()),
    url(r'^recipes/$', RecipeList.as_view()),
    url(r'^recipes/create/$', RecipeCreate.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)/$', RecipeDetail.as_view()),
    url(r'^ingredient_types/$', IngredientTypeList.as_view()),
    url(r'^ingredient_types/(?P<pk>[0-9]+)/$', IngredientTypeDetail.as_view()),
    url(r'^ingredients/$', IngredientList.as_view()),
    url(r'^ingredients/(?P<pk>[0-9]+)/$', IngredientDetail.as_view()),
    url(r'^feels/$', FeelList.as_view()),
    url(r'^feels/(?P<pk>[0-9]+)/$', FeelDetail.as_view()),
    url(r'^users/create/$', UserCreate.as_view()),
    url(r'^users/login/$', UserLogin.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
]
