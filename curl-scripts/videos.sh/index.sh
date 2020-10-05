#!/bin/bash

curl "http://localhost:8000/videos" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
