from rest_framework import serializers
from countries.models import Countries

class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model= Countries
        field=('id','name','capital')
        fields = '__all__'