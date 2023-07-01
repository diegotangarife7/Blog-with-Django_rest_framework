import re

from rest_framework import serializers

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):

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
        
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('El nombre debe contener al menos 4 caracteres')
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('La contraseña debe tener al menos 8 catecteres')
        if not has_number(value):
            raise  serializers.ValidationError('La contraseña debe tener al menos un numero')
        return value
    
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


def has_number(string):
    pattern = r'\d' 

    if re.search(pattern, string):
        return True
    else:
        return False
    


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'last_name',
            'gender',
            'twitter',
            'avatar',
            'is_active'
        ]



   
        
    
        
