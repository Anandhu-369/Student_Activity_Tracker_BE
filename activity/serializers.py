from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Activity
        fields=["id","name","activity","hours","created_at"]
        read_only_fields=["id","created_at"]

    def validate_name(self,value):
        value=value.strip()
        if not value:
            raise serializers.ValidationError("Student Name Can't be Empty")
        return value

    def validate_activity(self,value):
        value=value.strip()
        if not value:
            raise serializers.ValidationError("Activity Can't be Empty")
        return value

    def validate_hours(self,value):
        if value<1:
            raise serializers.ValidationError("Hours Must be More Than One")
        return value
        
