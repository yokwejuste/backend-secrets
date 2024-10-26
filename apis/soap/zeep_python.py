import requests

# Define the SOAP API endpoint
url = "http://www.dneonline.com/calculator.asmx"

# Construct the SOAP request headers
headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "http://tempuri.org/Add"
}

# Constructing the SOAP XML body (for the 'Add' operation)
body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Add xmlns="http://tempuri.org/">
      <intA>5</intA>
      <intB>10</intB>
    </Add>
  </soap:Body>
</soap:Envelope>"""

response = requests.post(url, data=body, headers=headers)

print("Status Code:", response.status_code)
print("Response XML:", response.text)
