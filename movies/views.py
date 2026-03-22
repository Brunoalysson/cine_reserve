from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Movie, Session, Seat
from .serializers import MovieSerializer, SessionSerializer, SeatSerializer, RegisterSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['get'])
    def sessions(self, request, pk=None):
        movie = self.get_object()
        sessions = Session.objects.filter(movie=movie)
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    @action(detail=True, methods=['get'])
    def seats(self, request, pk=None):
        session = self.get_object()
        seats = session.seats.all().order_by('row', 'number')
        serializer = SeatSerializer(seats, many=True)
        return Response(serializer.data)


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    @action(detail=True, methods=['post'])
    def reserve(self, request, pk=None):
        seat = self.get_object()

        if seat.status != 'AVAILABLE':
            return Response(
                {"error": "Seat is not available"},
                status=status.HTTP_400_BAD_REQUEST
            )

        seat.status = 'RESERVED'
        seat.save()

        return Response({"message": "Seat reserved successfully"})


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)