# from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
# from rest_framework.decorators import api_view, action
# from rest_framework.pagination import PageNumberPagination
# class IsSuperUserOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#
#         # safe_methods = getattr(settings, 'PATCH','GET','POST','PUT', ('GET', 'HEAD', 'OPTIONS'))
#         if request.user.is_superuser:
#             return True
#
#         if request.method in SAFE_METHODS:
#             return request.user and request.user.is_authenticated
#
#         return True
#
#
# class BasePagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'pageSize'
#
# class ImageUploadView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     pagination_class = BasePagination
#
#     def list(self, request, *args, **kwargs):
#         if 'query_all' in request.query_params:
#             queryset = self.filter_queryset(self.get_queryset())
#             serializer = self.get_serializer(queryset, many=True)
#             return Response(serializer.data)
#         else:
#             return super().list(request, *args, **kwargs)
#
#     # def get(self, request, format=None):
#     #     users = User.objects.all()
#     #     serializer = UserSerializerWithToken(users, many=True)
#     #     return Response(serializer.data)
#     # def get_extra_actions(self):
#     #     return self.serializer_class_by_actions[self.request.method]
#
#     @action(detail=True, methods=['get'])
#     def get(self, request, *args, **kwargs):
#         # Example: filter images uploaded by the current user
#         # user = self.get_object()
#         queryset = Image.objects.all().filter(pk = self.get_object().id)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     @action(detail=True, methods=['post'])
#     def update(self,request, *args, **kwargs):
#         img = self.get_object()
#         serializer = ImageSerializer(img, data=request.data, partial=True)  # Use `partial=True` for partial updates
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # @action(detail=True, methods=['get'])
#     # def get(self, request, pk=None):
#     #     user = self.get_object()
#     #     queryset = Image.objects.filter(username=user.username)
#     #     serializer = self.get_serializer(queryset, many=True, context={'request': request})
#     #     return Response(serializer.data)
#
#
#     #     user = self.get_object()
#     #     queryset = queryset = self.filter_queryset(self.get_queryset())
#     #     obj = queryset.get(pk=self.request.user.g)
#     #     serializer = self.get_serializer(queryset, many=True)
#     #     return Response(serializer.data)
#     #
#     # queryset = self.filter_queryset(self.get_queryset())
#     # # make sure to catch 404's below
#     # obj = queryset.get(pk=self.request.user.organisation_id)
#     # self.check_object_permissions(self.request, obj)
#     # return obj
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response
class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.method in SAFE_METHODS:
            return True

        if request.user == 'PUT' or request.method == 'PATCH':
            return request.user == view.get_object().user

        return True


class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'


class ImageUploadView(viewsets.ModelViewSet):
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = BasePagination
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    filterset_fields = ['username']
    search_fields = ['username', 'file']
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        if 'query_all' in request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)