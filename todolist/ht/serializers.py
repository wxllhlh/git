from rest_framework import serializers
from ht.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'username', 'title',  'description', 'status')
