
from rest_framework import serializers

from api.models import User

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password","phone"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



