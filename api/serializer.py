from rest_framework import serializers
from student.models import User

class UserSerializer(serializers.Serializer):
  
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    hobby = serializers.CharField()
    Location = serializers.CharField()
   
    def validate(self, data):
        username = data.get('username')

        if len(username)<=4:
            result = {
                "status":False,
                "message": "username len is less than 4"
            }

            raise serializers.ValidationError(result)

        phone_number = data['phone_number']

        if not phone_number.startswith('+998'):
            result = {
                "status": False,
                "message": "Telefon raqam faqat Uzb vo'lishi lozim "
            }

            raise serializers.ValidationError(result)

        return data


    def create(self, validated_data):
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        phone_number = validated_data.get('phone_number')
        Location = validated_data.get('Location')
        hobby = validated_data.get('hobby')
    
        User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            Location=Location,
            hobby=hobby
        )

        return validated_data
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.Location = validated_data.get('Location', instance.Location)
        instance.hobby = validated_data.get('hobby', instance.hobby)
        return instance  
    

    def delete(self, instance):
     
      instance.delete()

      
        