import re

# Given address string
address = "University of Kent, Canterbury, Kent, CT2 7NT"

# Define regex pattern for UK postcode
postcode_pattern = r"\b[A-Z]{1,2}\d[A-Z\d]? \d[A-Z]{2}\b"

# Search for postcode in the address string
postcode = re.search(postcode_pattern, address)

# Extract and print the result
if postcode:
    result = postcode.group(0)
    print(f"Extracted postcode: {result}")
else:
    print("No postcode found")

