from rest_framework import viewsets
from .models import DonorDetails, PatientDetail, Request, Stock, Feedback
from .serializers import DonorDetailsSerializer, PatientDetailSerializer, RequestSerializer, StockSerializer, FeedbackSerializer

class DonorDetailsViewSet(viewsets.ModelViewSet):
    queryset = DonorDetails.objects.all()
    serializer_class = DonorDetailsSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in "create":
            permission_classes = [permissions.AllowAny]  
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAdminOrDonor]
        elif self.action == "destroy":
            permission_classes = [IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class PatientDetailViewSet(viewsets.ModelViewSet):
    queryset = PatientDetail.objects.all()
    serializer_class = PatientDetailSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminOrpatient]
        elif self.action in "create":
            permission_classes = [permissions.AllowAny]  
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAdminOrpatient]
        elif self.action == "destroy":
            permission_classes = [IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminOrpatient]
        elif self.action in "create":
            permission_classes = [IsPatient]  
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAdminOrpatient]
        elif self.action == "destroy":
            permission_classes = [IsAdminOrpatient]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminOrpatient]
        elif self.action in "create":
            permission_classes = [permissions.AllowAny]  
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAdmin]
        elif self.action == "destroy":
            permission_classes = [IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in "create":
            permission_classes = [IsPatient]  
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsPatient]
        elif self.action == "destroy":
            permission_classes = [IsPatient]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
