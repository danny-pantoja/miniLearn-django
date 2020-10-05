#!/bin/bash

curl "http://localhost:8000/videos/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "videos": {
      "name": "'"${NAME}"'",
      "url": "'"${URL}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
