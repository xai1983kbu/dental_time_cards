from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

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
        # return 'api/user/{id}/'.format(id=obj.id)
        # api_reverse('<namespace>:<view_name>', kwargs={'username': obj.username})
        request = self.context.get('request')
        return api_reverse('api-user:detail', kwargs={'username': obj.username}, request=request)