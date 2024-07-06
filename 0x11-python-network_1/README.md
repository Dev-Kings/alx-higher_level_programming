# 0x11. Python - Network #1

## Fetching Internet Resources with Python

This project demonstrates how to fetch internet resources using Python's `urllib` and `requests` packages. It covers making GET and POST requests, decoding responses, and handling JSON data.

## Prerequisites

- Python 3.8.5
- `requests` package

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run the scripts using `python3 script_name.py`.

## Example

### Fetching a URL with `urllib`

```python
import urllib.request

url = 'http://example.com'
with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')
print(html)
```
