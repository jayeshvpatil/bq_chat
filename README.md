
### Create a virtual environment for the app:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install the dependencies:
```bash
pip install -r requirements.txt
```

### Add gcp service account to .streamlit/secret.toml
[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"