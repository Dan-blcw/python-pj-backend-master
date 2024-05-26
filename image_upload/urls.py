# # from django.urls import path
# from .views import ImageUploadView
# # from .views import ImageListView
# from django.urls import path
# # from rest_framework.routers import DefaultRouter
# # from .views import ImageViewSet
# # from . import views
# # router = DefaultRouter()
# # router.register(r'api/image-upload', ImageUploadView, basename='image')
# urlpatterns = [
#     # path('api/image-upload/', ImageUploadView.as_view(), name='image-upload'),
#     # path('api/image-upload-detail/', ImageListView.as_view(), name='image-upload'),
#     # path('', include(router.urls)),
#     path('api/image-detail/<int:pk>/',  ImageUploadView.as_view(), name='image-detail'),
#     # path('api/image-upload/<int:ok>/', ImageUploadView.as_view(), name='image-detail'),
#     path('api/image-upload/<int:pk>/',  ImageUploadView.as_view(), name='image-change-img'),
#  ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ImageUploadView
#
# router = DefaultRouter()
# router.register(r'api/image-upload', ImageUploadView, basename='image')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageUploadView


router = DefaultRouter()
router.register(r'image-upload', ImageUploadView)

urlpatterns = [
    path('api/', include(router.urls))
]
