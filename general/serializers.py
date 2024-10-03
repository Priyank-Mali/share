from rest_framework import serializers
from .models import globalNote

class globalNoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = globalNote
        fields = "__all__"