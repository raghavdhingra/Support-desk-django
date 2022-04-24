from django.urls import path
from . import views

urlpatterns = [
    path("redirect/", views.redirectUser, name="redirect_user"),
    path("all-request/", views.allRequest, name="supportdesk_all_request"),
    path("view-request/<int:num>", views.viewRequest),
    path("my-request/", views.myRequest, name="supportdesk_my_request"),
    path("create-request/", views.createRequest, name="supportdesk_create_request"),
    path("assign/<int:id>", views.assignRequest),
    path("complete/<int:id>", views.completeRequest),
]
