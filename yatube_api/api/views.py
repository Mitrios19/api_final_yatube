from posts.models import Post, Group, Comment, User, Follow
from .serializers import (PostSerializer, UserSerializer,
                          GroupSerializer, CommentSerializer,
                          FollowSerializer)
from .permissions import AuthorOrReadOnly, CanSubscribe
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (CanSubscribe,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['following__username']  # Поиск по имени пользователя, на которого подписан

    def get_queryset(self):
        # Возвращаем только подписки текущего пользователя
        return Follow.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Устанавливаем текущего пользователя как подписчика
        serializer = self.get_serializer(data={
            'user': request.user.id,
            'following': request.data.get('following')
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

