# C:\Python312\Lib\site-packages\requests\__init__.py


# import requests
import sys

sys.path.append("C:\Python312\Lib\site-packages")
# print(sys.path)


import requests

# Make the API request
response = requests.get('https://c60d32ofo0.execute-api.eu-central-1.amazonaws.com')  # Replace with your actual API endpoint

# Assert the status code is 200
assert response.status_code == 200, f"Status code is not 200, it's {response.status_code}"

print("Status code is 200")