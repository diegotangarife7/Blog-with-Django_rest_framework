import re

from django.contrib.auth.hashers import check_password

from rest_framework import serializers

from .models import User




def has_number(string):
    pattern = r'\d' 

    if re.search(pattern, string):
        return True
    else:
        return False
    

class UserValidateName:

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('El nombre debe contener al menos 4 caracteres')
        return value
    

class UserValidatePassword:

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('La contraseña debe tener al menos 8 catecteres')
        if not has_number(value):
            raise  serializers.ValidationError('La contraseña debe tener al menos un numero')
        return value


class UserRegisterSerializer(serializers.ModelSerializer, UserValidateName, UserValidatePassword):

    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'password',
            'password_confirm'
        ]
        
        extra_kwargs = {
                'password': {'write_only': True},
                'password_confirm': {'write_only': True}
            }
    
    def validate(self, data):
        password = data["password"]
        password_confirm = data["password_confirm"]
    
        if password != password_confirm:
            raise serializers.ValidationError({'password':'Las contraseñas no coinciden'})
        elif password == password_confirm:
            data.pop('password_confirm')
        return super().validate(data)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'last_name',
            'gender',
            'twitter',
            'avatar',
            'is_active'
        ]


class UserUpdateSerializer(serializers.ModelSerializer, UserValidateName):

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'last_name',
            'gender',
            'twitter'
        ]


class UserDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'is_active'
        ]


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'last_name',
            'gender',
            'twitter',
            'avatar',
        ]


class UserUpdatePasswordSerializer(serializers.ModelSerializer):

    new_password = serializers.CharField(write_only=True)
    new_password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'password',
            'new_password',
            'new_password_confirm'
        ]

    def validate_password(self, value):
        user = self.instance
        if not check_password(value, user.password):
            raise serializers.ValidationError('El password actual es incorrecto. //')
        return value
    
    def validate_new_password(self, value):
        new_password = UserValidatePassword()
        new_password.validate_password(value)
        return value

    def validate(self, data):
        new_password = data['new_password']
        new_password_confirm = data['new_password_confirm']
        password = data['password']

        if new_password == password:
            raise serializers.ValidationError({'nueva contraseña': 'asegurate de que la nueva contraseña sea diferente a la actual'})
        if new_password != new_password_confirm:
            raise serializers.ValidationError({'new_password_confirm': 'Las contraseñas no coinciden'})
        
        user = self.instance
        user.set_password(new_password)
        data['password'] = user.password

        return super().validate(data)
            
