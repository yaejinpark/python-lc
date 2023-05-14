import base64
from requests.auth import HTTPBasicAuth
api_key = base64.b64encode('343f1541-d006-47b5-86c3-1e7605f759e8:')
api_URL = "https://api.catalog.beer"
r = requests.post(api_URL, auth=HTTPBasicAuth("343f1541-d006-47b5-86c3-1e7605f759e8", ''), data=payload)

print(r.request.headers['Authorization'])