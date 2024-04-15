from rest_framework import serializers
from .models import Host, RentRequest, Rents, Transaction, Vehicle, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        
# Serializer for RentRequest model
class RentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentRequest
        fields = '__all__'

# Serializer for Rents model
class RentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rents
        fields = '__all__'

# Serializer for Host model
class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

# Serializer for Transaction model
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
