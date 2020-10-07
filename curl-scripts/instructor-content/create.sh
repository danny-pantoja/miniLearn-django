#!/bin/bash

curl "http://localhost:8000/instructor-content/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "instructorContent": {
      "name": "'"${NAME}"'",
      "content": "'"${CONTENT}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
