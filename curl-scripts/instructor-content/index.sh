#!/bin/bash

curl "http://localhost:8000/instructor-content" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
