
from rest_framework import serializers

from api.models import Problem,User

class AdminSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","phone","password"]

        read_only_fields = ["id"]

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)



class ProblemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Problem

        fields = "__all__"

        read_only_fields = ["id","posted_by","created_at","updated_at","is_active"]


