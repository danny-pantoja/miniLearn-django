#!/bin/bash

curl "http://localhost:8000/videos/" \
  --include \
  --request POST \
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
