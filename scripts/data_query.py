import os
import json
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

# https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
load_dotenv()

endpoint = os.environ["COSMOS_ENDPOINT"]
database_id = os.environ["DATABASE_ID"]
container_id = os.environ["CONTAINER_ID"]
account_key = os.environ["COSMOS_KEY"]

credential = DefaultAzureCredential()
client = CosmosClient(url=endpoint, credential=account_key)

def query_values_with_vin(container, vin):
    # https://azuresdkdocs.blob.core.windows.net/$web/python/azure-cosmos/4.0.0/index.html#query-the-database
    for item in container.query_items(
            query=f'SELECT * FROM mycontainer r WHERE r.VIN="{vin}"',
            enable_cross_partition_query=True):
        print(json.dumps(item, indent=True))

def query_values_with_city(container, city):
    # https://azuresdkdocs.blob.core.windows.net/$web/python/azure-cosmos/4.0.0/index.html#query-the-database
    for item in container.query_items(
            query=f'SELECT * FROM mycontainer r WHERE r.City="{city}"',
            enable_cross_partition_query=True):
        print(json.dumps(item, indent=True))    

if __name__ == "__main__":
    # database
    db = client.get_database_client(database_id)
    # container
    container = db.get_container_client(container_id)

    print("query values based on a vin first \n")

    # query based on a vin value
    QUERY_VIN = "7SAYGDEE5P"
    query_values_with_vin(container, QUERY_VIN)

    print("query values based on a city second \n")

    # query based on a city value
    QUERY_CITY= "Seattle"    
    query_values_with_city(container, QUERY_CITY)