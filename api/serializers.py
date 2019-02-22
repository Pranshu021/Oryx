from rest_framework import serializers
from productapi.models import Smartphone, Rated

class SmartphoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Smartphone

        fields = ['name', 'image', 'performance_ratings','design_ratings', 'camera_ratings', 'sound_ratings', 'features_ratings', 'no_of_users', 'commented', 'total_ratings', 'recommend', 'not_recommend', 'overpriced', 'issues_with_the_product', 'budget', 'smooth',]










