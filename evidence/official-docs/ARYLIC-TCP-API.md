# Arylic TCP API — official web documentation

Source: https://developer.arylic.com/tcpapi/#tcp-api

## Scope
Official TCP API documentation for Arylic/Linkplay devices using the A31 Wi-Fi module and model-dependent passthrough functions.

## Transport
- TCP port 8899
- persistent bidirectional connection
- minimum command interval: 200 ms
- documentation states one connection per client IP at a time
- packet header: 18 96 18 20
- payload length: little-endian integer
- checksum: sum of payload bytes, little-endian integer
- reserved: 8 zero bytes
- command payload normally starts MCU; received messages normally AXX, except PAS behavior
- payloads longer than 11 bytes normally terminate with &

## Canonical import
Records 222–258 were imported from this source. Existing records already supported by captures/implementation were not duplicated.

## Applicability warning
The basic command family is associated with the A31 Wi-Fi module. PAS passthrough talks to the product base board; AP8064 and BP10XX command sets are model/platform dependent and are not automatically valid on every A31-based product.

Status for newly imported commands: DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED.
