from rest_framework import serializers
from api.models import Buyer, Seller, Competition, Bid


class AllBuyersListViewSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        fields = ["id", "name"]


class AllSelllersListViewSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ["id", "name", "verified"]


class AllCompetitionsListViewSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = '__all__'


class AllBidsListViewSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = '__all__'
