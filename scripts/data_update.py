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
    response = []
    # https://azuresdkdocs.blob.core.windows.net/$web/python/azure-cosmos/4.0.0/index.html#query-the-database
    for item in container.query_items(
            query=f'SELECT * FROM mycontainer r WHERE r.VIN="{vin}"',
            enable_cross_partition_query=True):
        print(json.dumps(item, indent=True))
        response.append(item)
    return response

# in Azure updating and inserting is considered an Upsert
# modified from the upsert_item function at https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/cosmos/azure-cosmos/samples/document_management.py#L106-L111
def update_value(container, updated_value):
    container.upsert_item(body=updated_value)

if __name__ == "__main__":
    # database
    db = client.get_database_client(database_id)
    # container
    container = db.get_container_client(container_id)

    # query based on a vin value
    QUERY_VIN = "5YJXCAE23J"
    print("query values based on a vin first \n")
    queried_values = query_values_with_vin(container, QUERY_VIN)

    # change the value of the ElectronicVehicleType to something else
    for item in queried_values:
        item["ElectricVehicleType"] = "hey this is an update of the electronic vehicle type"
        update_value(container, item)

    # query again to show the change has saved
    print("query values again and show update second \n")
    queried_values = query_values_with_vin(container, QUERY_VIN)