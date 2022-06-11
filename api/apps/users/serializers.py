from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        label='E-mail',
        max_length=64,
        min_length=6,
        allow_blank=False,
        allow_null=False
        )
    date_of_birth = serializers.DateField(label='Data de nascimento')
    username = serializers.CharField(
        label='Usuário',
        max_length=32,
        allow_blank=False,
        allow_null=False
        )
    password = serializers.CharField(
        label='Senha',
        max_length=64,
        min_length=6,
        allow_blank=False,
        allow_null=False
        )
    first_name = serializers.CharField(
        label='Nome',
        max_length=32
        )
    last_name = serializers.CharField(
        label='Sobrenome',
        max_length=32
        )

    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')
        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'E-mail já existe'})
        if UserModel.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': 'Username já existe'}
                )

        return super().validate(attrs)

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = UserModel
        fields = [
            'email',
            'date_of_birth',
            'username',
            'password',
            'first_name',
            'last_name'
            ]
