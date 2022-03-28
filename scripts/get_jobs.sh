#!/bin/bash

AIRTABLE_URL="https://api.airtable.com/v0/appTgR7p7sKXHvip2/Table%201"
AIRTABLE_API_KEY=$EMEATECH_AIRTABLE_API_KEY

records=$(curl $AIRTABLE_URL -H "Authorization: Bearer $AIRTABLE_API_KEY")

echo $records > jobs.txt
