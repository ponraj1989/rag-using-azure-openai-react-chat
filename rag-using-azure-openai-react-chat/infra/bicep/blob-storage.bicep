param storageAccountName string
param location string = resourceGroup().location

resource blobStorage 'Microsoft.Storage/storageAccounts@2021-04-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    supportsHttpsTrafficOnly: true
  }
}

output blobStorageEndpoint string = 'https://${blobStorage.name}.blob.core.windows.net/'