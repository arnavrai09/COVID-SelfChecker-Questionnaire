from rest_framework import serializers

class PatientSerializer(serializers.Serializer):
    breathing_problem = serializers.IntegerField()
    fever = serializers.IntegerField()
    dry_cough = serializers.IntegerField()
    sore_throat = serializers.IntegerField()
    running_nose = serializers.IntegerField()
    asthma = serializers.IntegerField()
    chronic_lung_disease = serializers.IntegerField()
    headache = serializers.IntegerField()
    heart_disease = serializers.IntegerField()
    diabetes = serializers.IntegerField()
    hyper_tension = serializers.IntegerField()
    fatigue = serializers.IntegerField()
    gastrointestinal = serializers.IntegerField()
    abroad_travel = serializers.IntegerField()
    contact_with_covid_patient = serializers.IntegerField()
    attended_large_gathering = serializers.IntegerField()
    visited_public_exposed_places = serializers.IntegerField()
    family_working_in_public_exposed_places = serializers.IntegerField()