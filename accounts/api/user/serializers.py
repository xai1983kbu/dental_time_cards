from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri        = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]

    def get_uri(self, obj):
        return 'api/user/{id}/'.format(id=obj.id)
