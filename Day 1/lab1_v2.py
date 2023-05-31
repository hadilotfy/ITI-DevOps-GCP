from google.oauth2 import service_account
creds = service_account.Credentials.from_service_account_file("my-service-account.json")

from google.cloud import resourcemanager_v3 as rm
# The Client
client = rm.ProjectsClient(credentials=creds)
# The Request
request = rm.GetProjectRequest(name="projects/96418353483",)
# Making the reques
responce = client.get_project(request=request)
print("Hello GCP")
print("================= Project Id    =================")
print( f"My Project Id is: {responce.project_id}" )
print("================= Full Responce =================")
print(responce)
print("=================    The End    =================")