# Cosmos DB Python Scripting

This project includes several python scripts that can be used to interact with an [Azure Cosmos DB Database Container](https://azure.microsoft.com/en-us/products/cosmos-db).

This project was started from the [azure python quickstart tutorial](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python).

The python scripts use the [Azure Python Cosmos SDK](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-cosmos/4.0.0/index.html).

Working with Cosmos DB python function calls are based on examples in [the Azure python SDK repo](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/cosmos/azure-cosmos/samples/document_management.py#L106-L111).

In the `data` folder there is a CSV file of electronic vehicle information retrieved freely from [catalog.data.gov](https://catalog.data.gov/dataset/electric-vehicle-population-data).

If you want to play with the scripts in this project, first you must create an Azure Cosmos DB account and database with a container. I recommend following the steps in the "setting up" step of the [Azure Cosmos DB Quickstart Tutorial](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python?tabs=azure-portal%2Cpasswordless%2Clinux%2Csign-in-azure-cli%2Csync#setting-up).

Before working with the scripts in this project, please also create a `.env` file in the project root with the following values:

```bash
COSMOS_ENDPOINT=""
COSMOS_KEY=""
DATABASE_ID=""
CONTAINER_ID=""
```

In the "scripts" folder there are the following scripts that work with a Cosmos DB container:
- `data_load.py` loads values from the `ELECTRONIC_VEHICLE_POPULATION_DATA.csv` file
- `data_query.py` queries values from the Electronic Vehicles data with a specific VIN (first 10 digits only)
- `data_delete.py` deletes values from the Electronic Vehicles data with a specific VIN (first 10 digits only)
- `data_update.py` updates values from the Electronic Vehicles data for a specicifc VIN (first 10 digits only)

When fininished working with the data, I recommend deleting the database and container unless you wanted to do more with the sample values.