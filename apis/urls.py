from django.urls import path
from .views import UserList, UserCreate, UserDetail, UserDelete, HomePageView

urlpatterns = [
    # path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", HomePageView.as_view(), name="user_home"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path("users/create/", UserCreate.as_view(), name="user_create"),
    path("users/delete/<int:pk>/", UserDelete.as_view(), name="user_delete"),
]
