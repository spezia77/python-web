from django.urls import path

from steamfake import views


urlpatterns = [
    path("", views.home),
    path("categoria", views.categoria_index, name="categorias"),
    path("categoria/cadastro", views.categoria_cadastro),
    path("categoria/cadastrar", views.categoria_cadastrar),
    path("categoria/apagar/<int:id>", views.categoria_apagar),
    path("categoria/editar/<int:id>", views.categoria_editar),
    path("categoria/editado/<int:id>", views.categoria_editado),
    path("tags", views.tag_index, name="tags"),
    path("tags/cadastro", views.tag_cadastro),
    path("tags/cadastrar", views.tag_cadastrar),
    path("tags/apagar/<int:id>", views.tag_apagar),
    path("tags/editar/<int:id>", views.tag_editar),
    path("tags/editado/<int:id>", views.tag_editado),

]