from django.shortcuts import render
from django.http import HttpResponse

import os
import requests
from django.shortcuts import render
from django.http import HttpResponse
from msal import ConfidentialClientApplication

# Azure AD App credentials
CLIENT_ID = '9029fab8-1336-4460-920f-ecc3b2507a77'
CLIENT_SECRET = 'V8W8Q~cNp30KZVGHHDqs3T1BI4zWRawucEovNbFo' '''a2fe5f35-d621-4a33-b86f-a95ec1b11d10'''
TENANT_ID = 'fbcf15bd-a458-4753-9b69-8ac6cffa0a9e'

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"

def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        # Get access token
        app = ConfidentialClientApplication(
            CLIENT_ID,
            authority=AUTHORITY,
            client_credential=CLIENT_SECRET,
        )
        result = app.acquire_token_for_client(scopes=SCOPE)

        print(result)

        if "access_token" in result:
            access_token = result["access_token"]

            # Upload to OneDrive root directory
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': uploaded_file.content_type,
            }
            upload_url = f"{GRAPH_API_ENDPOINT}/me/drive/root:/{uploaded_file.name}:/content"
            response = requests.put(upload_url, headers=headers, data=uploaded_file)

            if response.status_code in [200, 201]:
                return HttpResponse("File uploaded successfully to OneDrive.")
            else:
                return HttpResponse(f"Failed to upload. {response.status_code} - {response.text}")
        else:
            return HttpResponse(f"Failed to obtain access token. {result}")

    return render(request, 'upload.html')


'''https://test-instance-cbb9bbd7f0f2bgaz.canadacentral-01.azurewebsites.net/upload/'''