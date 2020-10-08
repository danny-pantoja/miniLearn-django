#!/bin/bash

curl "http://localhost:8000/instructor-content/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "instructor_content": {
      "name": "'"${NAME}"'",
      "content": "'"${CONTENT}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
