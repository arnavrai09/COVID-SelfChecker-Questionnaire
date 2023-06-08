import joblib
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ViewSet):
    serializer_class = PatientSerializer

    def create(self, request):
        # Load the logistic regression model from file
        lr = joblib.load('patients\logistic_regression_model.joblib')

        # Create a new patient instance from the request data
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the result of the prediction using the loaded model
        patient_data = [serializer.validated_data[field] for field in serializer.validated_data]
        result = lr.predict([patient_data])

        # Return a response with the prediction result
        if result == 1:
            return Response({'message': 'You may be affected with COVID-19 virus! Please get RTPCR test ASAP and stay in Quarantine for 14 days!'})
        else:
            return Response({'message': 'You do not have any symptoms of COVID-19. Stay home! Stay safe!'})
