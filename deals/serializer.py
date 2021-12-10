from rest_framework import serializers

class DealSerializer(serializers.Serializer):
    # initialize fields
    dealname = serializers.CharField()
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField() 