from django.shortcuts import render
from django.apps import apps
from django.forms.models import model_to_dict
from django.http import HttpResponse
import json
from api.models import Bid, Competition, Seller
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from api.serializers import AllBuyersListViewSerialzer, AllSelllersListViewSerialzer, AllCompetitionsListViewSerialzer, AllBidsListViewSerialzer
from api.models import Buyer, Seller, Competition, Bid


class AllBuyersListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AllBuyersListViewSerialzer

    def get_queryset(self):
        try:
            return Buyer.objects.all()
        except Exception as e:
            return Response(e)


class AllSelllersListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AllSelllersListViewSerialzer

    def get_queryset(self):
        try:
            return Seller.objects.all()
        except Exception as e:
            return Response(e)


class AllCompetitionsListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AllCompetitionsListViewSerialzer

    def get_queryset(self):
        try:
            return Competition.objects.all()
        except Exception as e:
            return Response(e)


class AllBidsListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AllBidsListViewSerialzer

    def get_queryset(self):
        try:
            return Bid.objects.all()
        except Exception as e:
            return Response(e)


class LoadModeldata(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, file_name=None):
        try:
            with open('data/%ss.json' % file_name) as f:
                data = json.load(f)
            selected_model = apps.get_model("api.%s" % file_name)

            for details in data:
                selected_model.objects.create(**details)

            return Response("Data Created", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e)


class SellerBidsPerCompetition(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            valid_bid_counter = {}
            final_data = []
            all_bids = Bid.objects.select_related(
                "seller", "competition", "competition__buyer").all()

            all_competitions = {
                obj.id: obj for obj in Competition.objects.all()}

            # checking successful bids and counting bids per seller per competition
            for bid in all_bids:
                bid_competition_instance = all_competitions[bid.competition_id]
                if (bid.offered_capacity >= bid_competition_instance.minimum_capacity) and bid.accepted and bid.seller.verified and bid_competition_instance.open <= bid.created <= bid_competition_instance.closed:
                    unique_name = bid.competition.buyer.name + "_" + \
                        bid.competition.name + "_" + bid.seller.name
                    if valid_bid_counter.get(unique_name):
                        valid_bid_counter[unique_name] += 1
                    else:
                        valid_bid_counter[unique_name] = 1

            for valid_bids_names, total_bids in valid_bid_counter.items():
                all_names = valid_bids_names.split("_")
                final_data.append(
                    {"buyer_name": all_names[0], "competition_name": all_names[1], "seller_name": all_names[2], "bids": total_bids})

            return Response(final_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e)
