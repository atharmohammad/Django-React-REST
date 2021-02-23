from rest_framework import serializers
from user.models import NewUser

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser #To create seriaalizer 1st define models which will be used
        fields = ('email','user_name','first_name','password','about') #fields include in serializer
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data): #Function which will run to , Here a instance of models is createed and returnig
        password = validated_data.pop('password',None)#by checking if the it satisfies models fields standards
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
