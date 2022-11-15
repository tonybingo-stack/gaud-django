from rest_framework import serializers 
from dwitter.models import ImageProcess
 
 
class ImageSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ImageProcess
        fields = ('imageUrl')