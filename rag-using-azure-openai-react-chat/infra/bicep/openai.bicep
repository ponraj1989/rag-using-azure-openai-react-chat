param openAiServiceName string
param location string = resourceGroup().location
param sku string = 'S0'

resource openAi 'Microsoft.CognitiveServices/accounts@2021-04-30' = {
  name: openAiServiceName
  location: location
  kind: 'OpenAI'
  sku: {
    name: sku
  }
  properties: {
    apiProperties: {
      openAiApiVersion: '2023-05-15'
    }
  }
}

output openAiEndpoint string = 'https://${openAi.name}.openai.azure.com/'