from django.urls import path
from .views import UserSerializerView, UserDetailApiView, CreateUserSerializerView, DeleteUserSerializerView, UpdateUserSerializerView

urlpatterns=[
    path('users-list/', UserSerializerView.as_view(), name='users_list'),
    path('users-deteil/<int:id>', UserDetailApiView.as_view(), name='users_deteil'),
    path('users-create/', CreateUserSerializerView.as_view(), name='users_create'),
    path('users-update/<int:id>', UpdateUserSerializerView.as_view(), name='users_update'),
    path('users-delete/<int:id>', DeleteUserSerializerView.as_view(), name='users_delete'),

]
