from rest_framework import serializers
from .models import AirbnbData

class AirbnbSeralizer(serializers.ModelSerializer):
    

    class Meta:
        model = AirbnbData

        
        fields = ('Categories',
                'Price',
                'Reviews',
                'Rating',
                'Description',
                'URL',
                'Amenities',
                'Location',
                'SafetyProperty',
                'Image',
        )

    

    def create(self, validated_data):
        data = AirbnbData.objects.create(**validated_data)
        return data

    def update(self, instance, validated_data):
        instance.Categories = validated_data.get('Categories', instance.Categories)
        instance.Price = validated_data.get('Price', instance.Price)
        instance.Reviews = validated_data.get('Reviews', instance.Reviews)
        instance.Rating = validated_data.get('Rating', instance.Rating)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.URL = validated_data.get('URL', instance.URL)
        instance.Amenities = validated_data.get('Amenities', instance.Amenities)
        instance.Location = validated_data.get('Location', instance.Location)
        instance.SafetyProperty = validated_data.get('SafetyProperty', instance.SafetyProperty)
        instance.Image = validated_data.get('Image', instance.Image)
        
        
        instance.save()
        return instance




