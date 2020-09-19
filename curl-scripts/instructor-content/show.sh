#!/bin/bash

curl "http://localhost:8000/instructor-content/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
