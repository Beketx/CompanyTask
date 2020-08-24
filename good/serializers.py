from rest_framework import serializers
from good.models import Good


class GoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Good
        fields = ['title', 'photo', 'price', 'size', 'subcategory', 'brand']
