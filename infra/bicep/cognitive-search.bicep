param cognitiveSearchName string
param location string = resourceGroup().location
param sku string = 'standard'
param replicaCount int = 1
param partitionCount int = 1

resource cognitiveSearch 'Microsoft.Search/searchServices@2020-08-01' = {
  name: cognitiveSearchName
  location: location
  sku: {
    name: sku
    capacity: replicaCount
  }
  properties: {
    partitionCount: partitionCount
    hostingMode: 'Default'
  }
}

output cognitiveSearchEndpoint string = 'https://${cognitiveSearch.name}.search.windows.net'