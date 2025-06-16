from msal import ConfidentialClientApplication

CLIENT_ID = "9029fab8-1336-4460-920f-ecc3b2507a77"
CLIENT_SECRET = "V8W8Q~cNp30KZVGHHDqs3T1BI4zWRawucEovNbFo"
TENANT_ID = "fbcf15bd-a458-4753-9b69-8ac6cffa0a9e"

app = ConfidentialClientApplication(
    client_id=CLIENT_ID,
    authority=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_credential=CLIENT_SECRET
)

result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

if "access_token" in result:
    print("✅ Token acquired successfully.")
    print("Access Token:", result["access_token"][:40], "...")  # Shortened
else:
    print("❌ Failed to acquire token:")
    print(result)