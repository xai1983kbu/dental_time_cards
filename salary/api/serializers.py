from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from salary.models import DaysAtWork
from accounts.api.serializers import UserPublicSerializer


class DaysAtWorkSerializer(serializers.ModelSerializer):
    uri          = serializers.SerializerMethodField(read_only=True)
    owner        = UserPublicSerializer(read_only=True)
    employee     = serializers.SlugRelatedField(source='owner', slug_field='username', read_only=True)

    class Meta:
        model = DaysAtWork
        fields = [
            'id',
            'owner',
            'start_work',
            'end_work',
            'date_work',
            'sum_day',
            'employee',
            'uri'
        ]
        read_only_fileds = ['id', 'employee', 'uri'] # only GET method allowed

    def get_uri(self, obj):
        request = self.context.get("request", None)
        return api_reverse('api-salary:detail', kwargs={'id': obj.id}, request=request)

    def get_serializer_context(self):
        return {'request': self.request}

    def create(self, validated_data):
        request = self.context.get('request', None)
        if not request.user.is_anonymous:
            validated_data.pop("user") # removing unnecessary key-value
            instance = DaysAtWork.objects.create(**validated_data, owner=request.user)
            return instance
        else:
            raise serializers.ValidationError('Anonymous user can\'t submit data')