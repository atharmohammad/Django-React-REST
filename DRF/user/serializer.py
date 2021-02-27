from rest_framework import serializers
from user.models import NewUser


class RegisterUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = NewUser #To create seriaalizer 1st define models which will be used
        fields = ('email','username','first_name','password','about') #fields include in serializer
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data): #Function which will run to , Here a instance of models is createed and returnig
        password = validated_data.pop('password',None)#by checking if the it satisfies models fields standards
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
#
# class UserLoginSerializer(serializers.Serializer):
#
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         email = data.get("email", None)
#         password = data.get("password", None)
#         user = authenticate(email=email, password=password)
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password is not found.'
#             )
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)
#             update_last_login(None, user)
#         except NewUser.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given email and password does not exists'
#             )
#         return {
#             'email':user.email,
#             'token': jwt_token
#         }
