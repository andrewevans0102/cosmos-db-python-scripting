import os
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import pandas as pd
import uuid

# https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
load_dotenv()

endpoint = os.environ["COSMOS_ENDPOINT"]
database_id = os.environ["DATABASE_ID"]
container_id = os.environ["CONTAINER_ID"]
account_key = os.environ["COSMOS_KEY"]

credential = DefaultAzureCredential()
client = CosmosClient(url=endpoint, credential=account_key)


if __name__ == "__main__":
    # database
    db = client.get_database_client(database_id)
    # container
    container = db.get_container_client(container_id)

    # read in original data file
    df = pd.read_csv("../data/ELECTRIC_VEHICLE_POPULATION_DATA.csv")

    # loop through file and save each value to the Cosmos DB container
    for index, row in df.iterrows():
        # capping at 10000 values but if you wanted more change the value here
        if(index < 10000):
            try:
                new_item = {
                    "id": str(uuid.uuid4()),
                    "VIN": row["VIN"],
                    "County": row["County"],
                    "City": row["City"],
                    "State": row["State"],
                    "PostalCode": row["Postal Code"],
                    "ModelYear": row["Model Year"],
                    "Make": row["Make"],
                    "Model": row["Model"],
                    "ElectricVehicleType": row["Electric Vehicle Type"],
                    "CAFVEligability": row["Clean Alternative Fuel Vehicle (CAFV) Eligibility"],
                    "ElectricRange": row["Electric Range"],
                    "BaseMSRP": row["Base MSRP"],
                    "LegislativeDistrict": row["Legislative District"],
                    "DOLVehicleId": row["DOL Vehicle ID"],
                    "VehicleLocation": row["Vehicle Location"],
                    "ElectricUtility": row["Electric Utility"],
                    "2020CensusTract": row["2020 Census Tract"]
                }

                container.create_item(new_item)
                print(f"value loaded with ${new_item} \n")
            except Exception:
                print(Exception)
        else:
            break