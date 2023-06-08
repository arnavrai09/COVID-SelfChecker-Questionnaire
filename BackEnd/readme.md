pip install django
pip install djangorestframework
pip install scikit-learn
pip install joblib

change path for ML Model

python .\manage.py runserver

curl --location --request POST 'http://localhost:8000/patients/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "breathing_problem": 1,
    "fever": 1,
    "dry_cough": 0,
    "sore_throat": 0,
    "running_nose": 0,
    "asthma": 0,
    "chronic_lung_disease": 0,
    "headache": 1,
    "heart_disease": 0,
    "diabetes": 0,
    "hyper_tension": 1,
    "fatigue": 1,
    "gastrointestinal": 0,
    "abroad_travel": 0,
    "contact_with_covid_patient": 0,
    "attended_large_gathering": 0,
    "visited_public_exposed_places": 1,
    "family_working_in_public_exposed_places": 0
}'