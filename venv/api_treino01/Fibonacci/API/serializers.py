from rest_framework.serializers import ModelSerializer
from Fibonacci.models import Major

class Major_Serializer(ModelSerializer):
    class Meta:
        model = Major
        fields = ('id','numero','calc')