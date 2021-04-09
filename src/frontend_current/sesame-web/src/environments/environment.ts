import { KeycloakConfig } from 'keycloak-angular';

// Add here your keycloak setup infos
let keycloakConfig: KeycloakConfig = {
  url: 'http://KEYCLOAK-IP:8088/auth',
  realm: 'your-realm-name',
  clientId: 'your-client-id',
  "credentials": {
    "secret": "your-client-secret"
  }  
};

export const environment = {
  keycloak: keycloakConfig,
};