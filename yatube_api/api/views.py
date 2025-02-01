from posts.models import Post, Group, Comment, Follow
from .serializers import (PostSerializer,
                          GroupSerializer, CommentSerializer,
                          FollowSerializer)
from .permissions import AuthorOrReadOnly, CanSubscribe
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response


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
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)
