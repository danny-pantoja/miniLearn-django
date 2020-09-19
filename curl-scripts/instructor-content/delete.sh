#!/bin/bash

curl "http://localhost:8000/instructor-content/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
