import os
import pytest
from azure.cosmos import CosmosClient, PartitionKey
from control_operations import create_control, read_control, Control

@pytest.fixture(scope="module")
def cosmos_container():
    connection_string = os.getenv("COSMOSDB_CONNECTION_STRING")
    database_id = os.getenv("COSMOSDB_DATABASE_NAME")
    container_id = os.getenv("COSMOSDB_CONTAINER_NAME")

    if not connection_string:
        raise ValueError("Please set COSMOSDB_CONNECTION_STRING environment variable.")

    client = CosmosClient.from_connection_string(connection_string)
    database = client.create_database_if_not_exists(id=database_id)
    container = database.create_container_if_not_exists(
        id=container_id,
        partition_key=PartitionKey(path="/id")
    )

    yield container

    client.delete_database(database.id)
    print("Database deleted")

def test_create_control(cosmos_container):
    test_control = Control(id="A.5.1.1", title="Policies for information security", active=True)
    
    # Verify that create_control does not raise an exception
    try:
        create_control(cosmos_container, test_control)
        print("Control creation test complete")
    except Exception as e:
        pytest.fail(f"create_control raised an exception: {e}")

def test_read_control(cosmos_container):

    test_control_id = "A.5.1.2"
    test_control = Control(id=test_control_id, title="Information security roles and responsibilities", active=True)
    
    try:
        create_control(cosmos_container, test_control)
        print("Control creation test complete")
    except Exception as e:
        pytest.fail(f"create_control raised an exception: {e}")

    control = read_control(cosmos_container, test_control_id)
    
    assert test_control_id == control.id
    assert "Information security roles and responsibilities" == control.title
    assert control.active
    
    print(control read test complete")
