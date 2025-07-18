from rest_framework import serializers


class WorkVolumeSerializer(serializers.Serializer):
    factory = serializers.IntegerField()
    start = serializers.DateField()
    finish = serializers.DateField()
    weight = serializers.IntegerField(min_value=1)

    def validate(self, data):
        if data['start'] > data['finish']:
            raise serializers.ValidationError('The start date cannot be later than the end date.')
        return data
