param redisName string = 'myRedisCache'
param location string = resourceGroup().location
param skuName string = 'Basic'
param skuCapacity int = 0

resource redisCache 'Microsoft.Cache/Redis@2021-06-01' = {
  name: redisName
  location: location
  sku: {
    name: skuName
    capacity: skuCapacity
    family: 'C'
  }
  enableNonSslPort: true
  minimumTlsVersion: '1.2'
}

output redisHost string = redisCache.hostName
output redisPort int = redisCache.port
output redisSslPort int = redisCache.sslPort