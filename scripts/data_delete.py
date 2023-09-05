import os
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
        response.append(item)
    return response

def delete_values(container, queried_values):
    for item in queried_values:
        # when deleting in a cosmos DB instance make sure to specify the right partition key
        # in the sample table I am using id but it could be anything you specifiy
        container.delete_item(item=item["id"], partition_key=item["id"])

if __name__ == "__main__":
    # database
    db = client.get_database_client(database_id)
    # container
    container = db.get_container_client(container_id)

    # vin value that will be selected and deleted    
    QUERY_VIN = "YV4BR0CK2K"

    # query based on a vin value
    print("query values based on a vin first to show they exist \n")
    queried_values = query_values_with_vin(container, QUERY_VIN)
    print(f"initially there are {len(queried_values)} with the selected vin \n")

    # attempt delete
    delete_values(container, queried_values)

    # query again based on the vin you selected
    print("query values based on a vin again to show they no longer exist \n")
    queried_values = query_values_with_vin(container, QUERY_VIN)
    print(f"after delete there are {len(queried_values)} with the selected vin \n")