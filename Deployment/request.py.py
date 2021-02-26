



import requests

# url = 'http://localhost:5000/predict_api'
url = 'http://127.0.0.1:5000/api_request'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
