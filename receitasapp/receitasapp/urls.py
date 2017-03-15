from django.conf.urls import url
from django.contrib import admin
from core import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='ReceitasAPP API')

urlpatterns = [
    # url(r'^comments/$', views.CommentList.as_view()),
    # url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    url(r'^recipes/$', views.RecipeList.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view()),
    url(r'^ingredient_types/$', views.IngredientTypeList.as_view()),
    url(r'^ingredient_types/(?P<pk>[0-9]+)/$', views.IngredientTypeDetail.as_view()),
    url(r'^ingredients/$', views.IngredientList.as_view()),
    url(r'^ingredients/(?P<pk>[0-9]+)/$', views.IngredientDetail.as_view()),
    url(r'^feels/$', views.FeelList.as_view()),
    url(r'^feels/(?P<pk>[0-9]+)/$', views.FeelDetail.as_view()),
    url(r'^users/$', views.UserCreate.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
]
