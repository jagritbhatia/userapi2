from django.urls import path
from .views import UserList, UserCreate, UserDetail, UserDelete

urlpatterns = [
    # path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", UserList.as_view(), name="user_list"),
    path("<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path("create/", UserCreate.as_view(), name="user_create"),
    path("delete/<int:pk>/", UserDelete.as_view(), name="user_delete"),
]
