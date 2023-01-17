#!/bin/bash
pkcs7=$(curl -s "http://169.254.169.254/latest/dynamic/instance-identity/pkcs7" | tr -d '\n')
echo $pkcs7
data=$(cat <<EOF
{
  "role": "wall-role",
  "pkcs7": "$pkcs7"
}
EOF
)
echo $data
curl -k --request POST --data "$data" "https://34.220.46.200:8200/v1/auth/aws/login" > /tmp/response.json
token=$(cat /tmp/response.json | jq -r '.auth.client_token')
curl -k -H "X-Vault-Token: $token" -X GET "https://34.220.46.200:8200/v1/kv/data/creds" > /tmp/response.txt