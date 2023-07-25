from typing import Any, Dict
from googleapiclient import discovery
from dotenv import load_dotenv
import os
from utils import import_json_to_dictionary

load_dotenv()

def main():
    # Load environment variables
    project_id = os.environ.get('PROJECT_ID')
    location = os.environ.get('LOCATION')
    dataset_id = os.environ.get('DATASET_ID')
    fhir_store_id = os.environ.get('FHIR_STORE_ID')

     # Import patient data from JSON file
    patient_to_create = import_json_to_dictionary('./data/patient_to_create.json')

     # Create the patient
    create_patient(project_id, location, dataset_id, fhir_store_id, patient_to_create)


def create_patient(
    project_id: str,
    location: str,
    dataset_id: str,
    fhir_store_id: str,
    patient_to_create: dict
) -> Dict[str, Any]:
    """Creates a new Patient resource in a FHIR store.
     Args:
        project_id: The project ID or project number of the Cloud project you want to use.
        location: The name of the parent dataset's location.
        dataset_id: The name of the parent dataset.
        fhir_store_id: The name of the FHIR store that holds the Patient resource.
        patient_to_create: The dictionary representing the patient to create.
     Returns:
        A dictionary representing the created Patient resource.
    """
    
    # Set up API client
    api_version = "v1"
    service_name = "healthcare"
    client = discovery.build(service_name, api_version)

    # Set up FHIR store information
    fhir_store_parent = f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
    fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"

    # Set up patient body
    patient_body = patient_to_create

    # Create the request to create the patient
    request = client.projects().locations().datasets().fhirStores().fhir().create(
        parent=fhir_store_name,
        type="Patient",
        body=patient_body
    )

    # Set required headers
    request.headers["content-type"] = "application/fhir+json;charset=utf-8"

    # Execute the request
    response = request.execute()

    # Print the ID of the created patient
    print(f"Created Patient resource with ID {response['id']}")
    return response

if __name__ == '__main__':
    main()