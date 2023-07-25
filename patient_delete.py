from typing import Any, Dict
from googleapiclient import discovery
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # Load environment variables
    project_id = os.environ.get('PROJECT_ID')
    location = os.environ.get('LOCATION')
    dataset_id = os.environ.get('DATASET_ID')
    fhir_store_id = os.environ.get('FHIR_STORE_ID')
    
    resource_type = 'Patient' #TODO:move to parameter
    resource_id = '02594d88-f264-42a9-9258-527486a98775' #TODO:move to parameter

    # Delete the resource
    delete_resource(
        project_id,
        location,
        dataset_id,
        fhir_store_id,
        resource_type, 
        resource_id 
    )


def delete_resource(
    project_id: str,
    location: str,
    dataset_id: str,
    fhir_store_id: str,
    resource_type: str,
    resource_id: str,
) -> dict:
    """Deletes a FHIR resource.

    Regardless of whether the operation succeeds or
    fails, the server returns a 200 OK HTTP status code. To check that the
    resource was successfully deleted, search for or get the resource and
    see if it exists.

    Args:
        project_id: The project ID or project number of the Cloud project you want to use.
        location: The name of the parent dataset's location.
        dataset_id: The name of the parent dataset.
        fhir_store_id: The name of the FHIR store.
        resource_type: The type of FHIR resource.
        resource_id: The "logical id" of the resource you want to get the contents of. The ID is assigned by the server.

    Returns:
        An empty dict.
    """

    # Set up API client
    api_version = "v1"
    service_name = "healthcare"
    client = discovery.build(service_name, api_version)

    # Set up FHIR store information
    fhir_store_parent = (
        f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
    )
    fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"

    # Create the request to read the patient
    request = (
        client.projects()
        .locations()
        .datasets()
        .fhirStores()
        .fhir()
        .delete(name=fhir_resource_path)
    )

    # Execute the request
    response = request.execute()

    # Print the ID of the deleted patient
    print(f"Deleted {resource_type} resource with ID {resource_id}.")

    return response

if __name__ == '__main__':
    main()