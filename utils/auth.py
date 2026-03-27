from azure.identity import ClientSecretCredential
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from root or msgraph/ subfolder
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")
load_dotenv(dotenv_path=Path(__file__).parent.parent / "msgraph" / ".env")

def get_graph_credential():
    tenant_id = os.getenv("TENANT_ID")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    return ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret
    )
