from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="admin_index"),
    path("nivel/save", views.nivel_save, name="nivel_save"),



    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
    # path("register", views.register, name="admin_register"),
    # path("forgot-password", views.forgot, name="forgot"),
    # path("user/exist", views.user_exist, name="user_exist"),
    # path("users", views.users, name="users"),
    # path("users/new", views.new_user_view, name="new_user_view"),
    # path("mi-empresa", views.empresa_view, name="empresa"),
    # path("mi-empresa/save", views.empresa_save_chages, name="empresa_save_chages"),
    # path("clientes", views.clientes_view, name="clientes_view"),
    # path("clientes/new", views.cliente_new, name="cliente_new"),
    # path("clientes/edit/<int:client_id>", views.cliente_edit, name="cliente_edit"),
    # path("clientes/edit/save", views.cliente_edit_save, name="cliente_edit_save"),
    # path("clientes/delete", views.cliente_delete, name="cliente_delete"),
    # path("folios/new", views.new_folio_view, name="new_folio_view"),
]
