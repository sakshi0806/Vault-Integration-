'''Vault takes the security burden away from developers by providing a secure, 
centralized secret store for an application’s sensitive data: 
credentials, certificates, encryption keys, and more.'''

# After successful installtion of Hashicorp vault 
# Run this command on command prompt: vault server -dev -dev-root-token-id="dev-only-token"
# "pip install hvac" run this command on terminal to install library

import hvac     # Hashicorp Vault library is imported

# Authenticate to vault
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='dev-only-token',
)

# Store a secret
create_response = client.secrets.kv.v2.create_or_update_secret(
    path='my-secret-password',
    secret=dict(password='Sakshi123'),
)

print('Secret written successfully.')

# Retrieve a secret
read_response = client.secrets.kv.read_secret_version(path='my-secret-password')

password = read_response['data']['data']['password']
if password != 'Sakshi123':
    sys.exit('unexpected password')

print('Access granted!')



