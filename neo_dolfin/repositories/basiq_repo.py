from services.s3_service import S3Service

url = f"{BASE_URL}users/{BASIC_ID}/transactions"

class BasiqRepo(IBasiqRepo):
    def __init__(self):
        self._data_source = []

def get_access_token(self):
        url = BASE_URL + "token"
        payload = "scope=SERVER_ACCESS"
        headers = {
            "accept": "application/json",
            "basiq-version": "3.0",
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {KEY}"
        }

        response = requests.post(url, data=payload, headers=headers)
        json_response = response.json()
        access_token = "Bearer " + json_response["access_token"]
        return access_token

def get_all_transaction_data_for_user(access_token):
    get_headers(access_token)
        
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

def create_user_transaction_data_object(data, username, bucket_name, file_extension):
    #Add exception handling
    return S3Service.set_object(data, bucket_name, username, file_extension)

def get_headers(access_token):
    headers = {
            "accept": "application/json",
            "authorization": access_token,
    }
    
    return headers
