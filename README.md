
# Sobre

Esse projeto tem o objetivo de demonstrar a integração com os servições fornecidos pela CLOUD HEALTHCARE SMS.


# Passo a passo

Altere as seguintes variáveis no arquivo .env.sample

PROJECT_ID = 'Nome do projeto na GCP'
LOCATION = 'Localização do projeto'
DATASET_ID = 'Nome do dataset' 
FHIR_STORE_ID = 'Nome do FHIR Store'
GOOGLE_APPLICATION_CREDENTIALS = 'Caminho para o arquivo de chave de acesso'

Na pasta data você encontra um modelo em json descrevendo os valores para o resource paciente.

O projeto faz o envio de um resource por vez, será necessário criar um meio de criar e enviar N resources.

# Referências
- Authentication:
https://cloud.google.com/healthcare-api/docs/authentication

- CRUD Instructions:
https://cloud.google.com/healthcare-api/docs/how-tos/fhir-resources#healthcare-create-patient-drest