# Proration API

POST /proration

Request body:
{
  "old_price": number,
  "new_price": number,
  "days_remaining": number,
  "days_in_actual_month": number,
  "spec": "v1" | "v2"
}

Response:
{ "charge": number }