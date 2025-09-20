import ibm_boto3
from ibm_botocore.client import Config


API_KEY = "0CbZ_LLjfcBgRnSXaQqSbmhndghdpQe7uMWUP3eg8f-l"
RESOURCE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/7e8ca22515014b44bf3ec732a7bb3fc8:46ab1d34-73b7-4e39-b85d-939ed7d35345::"
AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
ENDPOINT_URL = "https://s3.au-syd.cloud-object-storage.appdomain.cloud"

cos = ibm_boto3.client("s3",
    ibm_api_key_id=API_KEY,
    ibm_service_instance_id=RESOURCE_INSTANCE_ID,
    ibm_auth_endpoint=AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=ENDPOINT_URL
)

try:
    response = cos.list_buckets()
    print("✅ COS authentication successful.")
    for bucket in response["Buckets"]:
        print(f" - {bucket['Name']}")
except Exception as e:
    print("❌ COS authentication failed.")
    print("Error:", e)