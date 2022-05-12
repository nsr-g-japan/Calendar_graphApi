from msal import PublicClientApplication
import sys
client_id = '<client-id>'
tenant_id = '<refresh-token'
refresh_token = '<refresh-token>'

scope = [ '2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default' ]
# Check for too few or too many command-line arguments.
if (len(sys.argv) > 1) and (len(sys.argv) != 4):
  print("Usage: refresh-tokens.py <client ID> <tenant ID> <refresh token>")
  exit(1)

if len(sys.argv) > 1:
  client_id = sys.argv[1]
  tenant_id = sys.argv[2]
  refresh_token = sys.argv[3]

app = PublicClientApplication(
  client_id = client_id,
  authority = "https://login.microsoftonline.com/" + tenant_id
)

acquire_tokens_result = app.acquire_token_by_refresh_token(
  refresh_token = refresh_token,
  scopes = scope
)

if 'error' in acquire_tokens_result:
  print("Error: " + acquire_tokens_result['error'])
  print("Description: " + acquire_tokens_result['error_description'])
else:
  print("\nNew access token:\n")
  print(acquire_tokens_result['access_token'])
  print("\nNew refresh token:\n")
  print(acquire_tokens_result['refresh_token'])