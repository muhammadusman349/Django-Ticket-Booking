from rest_framework import serializers
from .models import Bus, Seat, Booking
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password']
                                        )
        return user


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'is_booked']


class BusSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Bus
        fields = '__all__'


class BusSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['bus_name', 'number', 'origin', 'destination']


class BookingSerializer(serializers.ModelSerializer):
    bus = BusSummarySerializer(read_only=True)
    seat = SeatSerializer(read_only=True)
    user = serializers.StringRelatedField()
    price = serializers.StringRelatedField()
    origin = serializers.StringRelatedField()
    destination = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'booking_time', 'bus', 'seat', 'price', 'origin', 'destination']
