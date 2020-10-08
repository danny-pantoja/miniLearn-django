#!/bin/bash

curl "http://localhost:8000/videos/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
