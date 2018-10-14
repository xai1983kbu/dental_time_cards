import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    uri      = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-user:detail', kwargs={'username': obj.username}, request=request)


class UserRegisterSerializer(serializers.ModelSerializer):
    password2      = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token          = serializers.SerializerMethodField(read_only=True)
    expires        = serializers.SerializerMethodField(read_only=True)
    message        = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            'message'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_message(self, obj):
        return 'Thank yo for registering. Please verify your email before continuing'

    def get_expires(self, oobj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with that e-mail already exists')
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with that username already exists')
        return value

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError('Password must match password2')
        return data

    def create(self, validated_data):
        user_obj = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = False
        user_obj.save()
        return user_obj

