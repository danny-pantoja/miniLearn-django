#!/bin/bash

curl "http://localhost:8000/videos/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
