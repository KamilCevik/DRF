from rest_framework import serializers
from post.models import Post

"""class PostSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=200)
    content=serializers.CharField(max_length=120)"""


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'image',
            'url',
            'created',
            'modified_by',
        ]


class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]
