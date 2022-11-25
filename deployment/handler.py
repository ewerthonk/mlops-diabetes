try:
  import unzip_requirements
except ImportError:
  pass

from joblib import load
import json

model = load('./models/model.joblib')

def predict(event, context):
    body = {"message": "OK",}
    if 'queryStringParameters' in event.keys():
        params = event['queryStringParameters']
        predict_proba = model.predict_proba(
            [
                [
                    int(params['pregnancies']),
                    int(params['glucose']),
                    int(params['blood_pressure']),
                    int(params['skin_thickness']),
                    int(params['insulin']),
                    float(params['bmi']),
                    float(params['diabetes_pedigree_function']),
                    int(params['age']),
                ]
            ]
        )[0]
        if predict_proba[0] > 0.5:
            predicted_class = "does not have diabetes"
            predicted_proba = predict_proba[0]
        else:
            predicted_class = "has diabetes"
            predicted_proba = predict_proba[1]

        body['predicted_class'] = predicted_class
        body['predicted_proba'] = round(predicted_proba, 3)
		
    else:
        body['message'] = 'queryStringParameters not in event.'

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": 'application/json',
            "Access-Control-Allow-Origin": "*"
        }
    }
	
    return response