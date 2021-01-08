from rest_framework import serializers
class usersSerializer(serializers.Serializer):
    username = serializers.CharField()
    amout_task = serializers.IntegerField()
    amout_task_end = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    

