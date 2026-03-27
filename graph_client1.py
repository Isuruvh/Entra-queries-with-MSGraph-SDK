from msgraph import GraphServiceClient
from utils.auth import get_graph_credential

def get_graph_client():
    credential = get_graph_credential()
    client = GraphServiceClient(credential)
    return client
