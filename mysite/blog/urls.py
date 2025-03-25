from django.urls import path
from blog.views import post_list, post_detail, post_comment, post_search

urlpatterns = [
    path('', post_list, name='home'),
    path('<int:id>/', post_detail, name='post_detail' ),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('search/', post_search, name='post_search'),
]
