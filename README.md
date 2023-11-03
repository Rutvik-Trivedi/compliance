# Compliance Checker API

## Description

Given two URLS ```compliance_url``` and ```url_to_check```, this API uses ChatGPT to check whether contents of the page at ```url_to_check``` is compliant with the policies provided in the content of the ```compliance_url```.

## Usage

To use the API locally, run the following command:
```python
python3 index.py
```

Then, make a POST request to the API at ```http://0.0.0.0:8002/check``` with the following payload:
```json
{
    "compliance_url": "https://example.com/compliance",
    "url_to_check": "https://example.com"
}
```

## Authorization

To Authenticate your API calls with OpenAI, send your OpenAI API key in the `x-api-key` header. For example:

```json
{
    "x-api-key": "xxxxxxxxxxxxxxxxxxxxxxxx",
    "Content-Type": "application/json"
}
```

### Note:
Make sure the contents of the web pages provided are easily scrappable and does not block crawlers.

## Python Usage

To call the API using python, run the following command:
```python
# pip install requests
import requests
import json

url = "http://0.0.0.0:8002/check"

payload = json.dumps({
    "compliance_url": "https://example.com/compliance",
    "url_to_check": "https://example.com"
})
headers = {
    'x-api-key': 'xxxxxxxxx',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```


## Online Demo

Instead of running the API locally, you can also make the POST request to the demo URL at [https://compliance-demo-flax.vercel.app/check](https://compliance-demo-flax.vercel.app/check).