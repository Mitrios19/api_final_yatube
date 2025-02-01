from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')

    def validate(self, data):
        user = data['user']
        following = data['following']
        if user == following:
            raise serializers.ValidationError("You cannot follow yourself.")
        return data
