# 📘 REQUESTS LIBRARY – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Requests?](#what-is-requests)
2. [Installation](#installation)
3. [Making GET Requests](#making-get-requests)
4. [Making POST Requests](#making-post-requests)
5. [Request Parameters](#request-parameters)
6. [Headers and Authentication](#headers-and-authentication)
7. [Response Handling](#response-handling)
8. [Error Handling](#error-handling)
9. [Sessions and Cookies](#sessions-and-cookies)
10. [Real-World Examples](#real-world-examples)
11. [Practice Exercises](#practice-exercises)

---

## What is Requests?

The **requests** library is the most popular HTTP client for Python. It makes sending HTTP requests simple and intuitive.

```python
import requests

# Simple GET request
response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())       # Parse JSON response

# Simple POST request
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.json())
```

**Key Characteristics:**
- ✅ Simple, intuitive API
- ✅ Handles GET, POST, PUT, DELETE, etc.
- ✅ Automatic JSON parsing
- ✅ Session persistence
- ✅ Connection pooling
- ✅ SSL verification

---

## Installation

### Installing Requests

```bash
# Install using pip
pip install requests

# Install specific version
pip install requests==2.28.0

# Upgrade to latest
pip install --upgrade requests
```

### Verify Installation

```python
import requests

print(requests.__version__)  # 2.28.0
```

---

## Making GET Requests

### Basic GET Request

```python
import requests

# Simple GET request
response = requests.get('https://httpbin.org/get')

print(f"Status: {response.status_code}")
print(f"Content: {response.text[:100]}...")
```

### GET with Parameters

```python
import requests

# Query parameters
params = {
    'q': 'python requests',
    'page': 2,
    'limit': 10
}

response = requests.get('https://httpbin.org/get', params=params)

print(f"URL: {response.url}")
# https://httpbin.org/get?q=python+requests&page=2&limit=10

print(response.json()['args'])
# {'q': 'python requests', 'page': '2', 'limit': '10'}
```

### GET with Custom Headers

```python
import requests

headers = {
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer token123'
}

response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json())
```

---

## Making POST Requests

### Basic POST Request

```python
import requests

# Form data
data = {
    'username': 'alice',
    'password': 'secret123'
}

response = requests.post('https://httpbin.org/post', data=data)
print(response.json()['form'])
# {'username': 'alice', 'password': 'secret123'}
```

### POST with JSON Data

```python
import requests

# JSON data
json_data = {
    'name': 'Alice',
    'age': 30,
    'email': 'alice@example.com'
}

response = requests.post('https://httpbin.org/post', json=json_data)
print(response.json()['json'])
# {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}
```

### POST with Files

```python
import requests

# Upload a file
files = {
    'file': open('document.pdf', 'rb')
}

response = requests.post('https://httpbin.org/post', files=files)
print(response.json()['files'])

# Multiple files
files = {
    'file1': open('file1.txt', 'rb'),
    'file2': open('file2.txt', 'rb')
}

response = requests.post('https://httpbin.org/post', files=files)
```

---

## Request Parameters

### Common HTTP Methods

```python
import requests

# GET
response = requests.get('https://httpbin.org/get')

# POST
response = requests.post('https://httpbin.org/post', data={'key': 'value'})

# PUT
response = requests.put('https://httpbin.org/put', json={'key': 'value'})

# DELETE
response = requests.delete('https://httpbin.org/delete')

# PATCH
response = requests.patch('https://httpbin.org/patch', json={'key': 'value'})

# HEAD
response = requests.head('https://httpbin.org/get')
print(response.headers)

# OPTIONS
response = requests.options('https://httpbin.org/get')
print(response.headers['allow'])
```

### Request Parameters Summary

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `params` | Query parameters | `params={'q': 'python'}` |
| `data` | Form data | `data={'name': 'Alice'}` |
| `json` | JSON data | `json={'name': 'Alice'}` |
| `headers` | HTTP headers | `headers={'User-Agent': 'MyApp'}` |
| `cookies` | Cookies | `cookies={'session': 'abc123'}` |
| `auth` | Authentication | `auth=('user', 'pass')` |
| `timeout` | Timeout seconds | `timeout=5` |
| `verify` | SSL verification | `verify=False` (not recommended) |
| `allow_redirects` | Follow redirects | `allow_redirects=False` |
| `proxies` | Proxy servers | `proxies={'http': 'http://proxy:8080'}` |

---

## Headers and Authentication

### Custom Headers

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Bearer your_token_here',
    'X-Custom-Header': 'custom-value'
}

response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json())
```

### Basic Authentication

```python
import requests
from requests.auth import HTTPBasicAuth

# Method 1: Using auth parameter
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=('user', 'pass')
)
print(response.status_code)  # 200

# Method 2: Using HTTPBasicAuth
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=HTTPBasicAuth('user', 'pass')
)
print(response.status_code)  # 200

# Method 3: Manual header
import base64
credentials = base64.b64encode(b'user:pass').decode()
headers = {'Authorization': f'Basic {credentials}'}
response = requests.get('https://httpbin.org/basic-auth/user/pass', headers=headers)
```

### Bearer Token Authentication

```python
import requests

# Bearer token (JWT, OAuth2)
token = 'your_access_token_here'

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get('https://api.example.com/protected', headers=headers)
print(response.status_code)
```

### API Key Authentication

```python
import requests

# In query string
params = {'api_key': 'your_api_key'}
response = requests.get('https://api.example.com/data', params=params)

# In header
headers = {'X-API-Key': 'your_api_key'}
response = requests.get('https://api.example.com/data', headers=headers)
```

---

## Response Handling

### Response Attributes

```python
import requests

response = requests.get('https://httpbin.org/get')

# Status code
print(f"Status: {response.status_code}")  # 200
print(f"Reason: {response.reason}")       # OK

# Headers
print(f"Content-Type: {response.headers['content-type']}")
print(f"Server: {response.headers.get('server', 'Unknown')}")

# Content
print(f"Text: {response.text[:100]}...")      # String content
print(f"Content: {response.content[:100]}...") # Bytes content

# URL
print(f"URL: {response.url}")
print(f"History: {response.history}")  # Redirect history

# Encoding
print(f"Encoding: {response.encoding}")
response.encoding = 'utf-8'  # Set custom encoding

# Elapsed time
print(f"Time: {response.elapsed.total_seconds():.2f}s")
```

### Parsing JSON Responses

```python
import requests

response = requests.get('https://api.github.com/users/octocat')

# Parse JSON
data = response.json()
print(f"Login: {data['login']}")
print(f"Name: {data['name']}")
print(f"Followers: {data['followers']}")
print(f"Public repos: {data['public_repos']}")

# Check if response is JSON
if response.headers['content-type'] == 'application/json':
    data = response.json()
else:
    print("Not JSON")
```

### Binary Content (Images, Files)

```python
import requests

# Download image
response = requests.get('https://www.python.org/static/img/python-logo.png')

# Save to file
with open('python-logo.png', 'wb') as f:
    f.write(response.content)

print(f"Downloaded {len(response.content)} bytes")

# Streaming large files
response = requests.get('https://example.com/large-file.zip', stream=True)

with open('large-file.zip', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

---

## Error Handling

### HTTP Status Codes

```python
import requests

response = requests.get('https://httpbin.org/status/404')

if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not found")
elif response.status_code == 500:
    print("Server error")
else:
    print(f"Other status: {response.status_code}")
```

### Raising Exceptions

```python
import requests

# raise_for_status() raises HTTPError for 4xx/5xx responses
response = requests.get('https://httpbin.org/status/404')

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    print(f"Status: {response.status_code}")

# Common request exceptions
try:
    response = requests.get('https://httpbin.org/delay/5', timeout=2)
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Failed to connect")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

### Complete Error Handling Example

```python
import requests
from requests.exceptions import Timeout, ConnectionError, HTTPError, RequestException

def safe_request(url, timeout=10):
    """Make request with comprehensive error handling"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response
    except Timeout:
        print(f"Timeout: {url}")
        return None
    except ConnectionError:
        print(f"Connection error: {url}")
        return None
    except HTTPError as e:
        print(f"HTTP error: {e.response.status_code} - {url}")
        return None
    except RequestException as e:
        print(f"Request failed: {e}")
        return None

# Usage
response = safe_request('https://httpbin.org/get')
if response:
    print(response.json())
```

---

## Sessions and Cookies

### Using Sessions

```python
import requests

# Create session
session = requests.Session()

# Set default headers for all requests
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Set default auth
session.auth = ('user', 'pass')

# Make requests using session
response1 = session.get('https://httpbin.org/get')
response2 = session.get('https://httpbin.org/headers')

# Session persists cookies across requests
session.get('https://httpbin.org/cookies/set?name=value')
response = session.get('https://httpbin.org/cookies')
print(response.json())  # {'cookies': {'name': 'value'}}

# Close session
session.close()

# Or use context manager
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response = session.get('https://httpbin.org/get')
```

### Working with Cookies

```python
import requests

# Send cookies
cookies = {'session_id': 'abc123', 'user_id': '42'}
response = requests.get('https://httpbin.org/cookies', cookies=cookies)
print(response.json())  # {'cookies': {'session_id': 'abc123', 'user_id': '42'}}

# Access cookies from response
response = requests.get('https://httpbin.org/cookies/set?name=value')
print(response.cookies['name'])  # value

# Iterate over cookies
for cookie in response.cookies:
    print(f"{cookie.name}: {cookie.value}")

# Session preserves cookies
session = requests.Session()
session.get('https://httpbin.org/cookies/set?session=123')
response = session.get('https://httpbin.org/cookies')
print(response.json())  # {'cookies': {'session': '123'}}
```

---

## Real-World Examples

### Example 1: GitHub API Client

```python
import requests
from datetime import datetime

class GitHubClient:
    def __init__(self, token=None):
        self.base_url = 'https://api.github.com'
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Python-GitHub-Client'
        })
        if token:
            self.session.headers.update({'Authorization': f'token {token}'})
    
    def get_user(self, username):
        """Get user information"""
        response = self.session.get(f'{self.base_url}/users/{username}')
        if response.status_code == 200:
            data = response.json()
            return {
                'login': data['login'],
                'name': data['name'],
                'followers': data['followers'],
                'public_repos': data['public_repos'],
                'created_at': datetime.fromisoformat(data['created_at'].replace('Z', '+00:00'))
            }
        return None
    
    def get_repos(self, username):
        """Get user repositories"""
        response = self.session.get(f'{self.base_url}/users/{username}/repos')
        if response.status_code == 200:
            repos = response.json()
            return [{'name': repo['name'], 'stars': repo['stargazers_count']} for repo in repos]
        return []
    
    def get_rate_limit(self):
        """Get API rate limit status"""
        response = self.session.get(f'{self.base_url}/rate_limit')
        if response.status_code == 200:
            data = response.json()
            return data['rate']
        return None

# Usage
client = GitHubClient()
user = client.get_user('octocat')
print(f"User: {user['login']}")
print(f"Name: {user['name']}")
print(f"Followers: {user['followers']}")
print(f"Repos: {user['public_repos']}")

repos = client.get_repos('octocat')
print(f"Recent repos: {repos[:3]}")

rate = client.get_rate_limit()
print(f"Rate limit: {rate['remaining']}/{rate['limit']}")
```

### Example 2: Weather API Client

```python
import requests

class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5'
    
    def get_current_weather(self, city):
        """Get current weather for a city"""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        
        response = requests.get(f'{self.base_url}/weather', params=params)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
        elif response.status_code == 404:
            return {'error': 'City not found'}
        else:
            return {'error': f'API error: {response.status_code}'}
    
    def get_forecast(self, city, days=5):
        """Get weather forecast"""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'cnt': days * 8  # 8 readings per day
        }
        
        response = requests.get(f'{self.base_url}/forecast', params=params)
        
        if response.status_code == 200:
            data = response.json()
            forecasts = []
            for item in data['list'][::8]:  # One per day
                forecasts.append({
                    'date': item['dt_txt'],
                    'temp': item['main']['temp'],
                    'description': item['weather'][0]['description']
                })
            return forecasts
        return []

# Usage (requires API key from openweathermap.org)
# client = WeatherClient('your_api_key')
# weather = client.get_current_weather('London')
# print(f"Temperature: {weather['temperature']}°C")
# print(f"Conditions: {weather['description']}")
```

### Example 3: File Downloader with Progress Bar

```python
import requests
import os
from tqdm import tqdm  # pip install tqdm

class FileDownloader:
    @staticmethod
    def download(url, filename=None, chunk_size=8192):
        """Download file with progress bar"""
        if filename is None:
            filename = os.path.basename(url)
        
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filename, 'wb') as f:
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as pbar:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
                    pbar.update(len(chunk))
        
        print(f"Downloaded: {filename}")
        return filename
    
    @staticmethod
    def download_with_resume(url, filename, chunk_size=8192):
        """Download with resume support"""
        existing_size = os.path.getsize(filename) if os.path.exists(filename) else 0
        
        headers = {'Range': f'bytes={existing_size}-'} if existing_size else {}
        response = requests.get(url, stream=True, headers=headers)
        
        mode = 'ab' if existing_size else 'wb'
        
        total_size = int(response.headers.get('content-length', 0)) + existing_size
        
        with open(filename, mode) as f:
            with tqdm(total=total_size, initial=existing_size, unit='B', unit_scale=True, desc=filename) as pbar:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
                    pbar.update(len(chunk))
        
        return filename

# Usage
# downloader = FileDownloader()
# downloader.download('https://example.com/large-file.zip')
```

### Example 4: REST API Wrapper

```python
import requests
from typing import Dict, Any, Optional

class RESTClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
        
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json() if response.content else {}
        except requests.exceptions.HTTPError as e:
            return {'error': str(e), 'status': response.status_code}
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """GET request"""
        return self._request('GET', endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """POST request"""
        return self._request('POST', endpoint, json=data)
    
    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """PUT request"""
        return self._request('PUT', endpoint, json=data)
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """DELETE request"""
        return self._request('DELETE', endpoint)
    
    def patch(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """PATCH request"""
        return self._request('PATCH', endpoint, json=data)

# Usage
client = RESTClient('https://jsonplaceholder.typicode.com')

# GET
users = client.get('/users')
print(f"Users: {len(users)}")

# GET with params
posts = client.get('/posts', params={'userId': 1})
print(f"User 1 posts: {len(posts)}")

# POST
new_post = client.post('/posts', data={'title': 'New Post', 'body': 'Content', 'userId': 1})
print(f"Created post ID: {new_post.get('id')}")

# PUT
updated = client.put('/posts/1', data={'title': 'Updated Title', 'body': 'New content', 'userId': 1})
print(f"Updated: {updated.get('title')}")

# DELETE
result = client.delete('/posts/1')
print(f"Deleted: {result}")
```

### Example 5: Web Scraper with Retry Logic

```python
import requests
from time import sleep
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class WebScraper:
    def __init__(self, retries=3, backoff_factor=1):
        self.session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Default headers
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get(self, url, retry_on_empty=False, max_empty_retries=3):
        """Get page with retry logic"""
        for attempt in range(max_empty_retries):
            try:
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                
                if retry_on_empty and not response.text.strip():
                    print(f"Empty response, retrying ({attempt + 1}/{max_empty_retries})")
                    sleep(1 * (attempt + 1))
                    continue
                
                return response
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                if attempt == max_empty_retries - 1:
                    raise
                sleep(1 * (attempt + 1))
        
        return None
    
    def get_with_rate_limit(self, url, delay=1):
        """Get with rate limiting"""
        response = self.get(url)
        sleep(delay)  # Be nice to servers
        return response
    
    def scrape_pages(self, urls, delay=1):
        """Scrape multiple pages"""
        results = {}
        for url in urls:
            try:
                response = self.get(url)
                results[url] = response.text if response else None
                sleep(delay)
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")
                results[url] = None
        return results

# Usage
scraper = WebScraper(retries=3)
# response = scraper.get('https://example.com')
# print(response.text[:200])
```

---

## Practice Exercises

### Beginner Level

1. **GET Request**
   ```python
   # Make GET request to https://httpbin.org/get
   # Print status code and response headers
   ```

2. **POST Request**
   ```python
   # Make POST request with form data
   # Data: name=Alice, age=30
   ```

3. **JSON Response**
   ```python
   # Get user data from GitHub API
   # https://api.github.com/users/octocat
   # Print username and follower count
   ```

### Intermediate Level

4. **Error Handling**
   ```python
   # Handle 404 and timeout errors
   ```

5. **Authentication**
   ```python
   # Make authenticated request using Bearer token
   ```

6. **File Download**
   ```python
   # Download an image and save to file
   ```

### Advanced Level

7. **Session Management**
   ```python
   # Use session to persist cookies
   ```

8. **REST API Client**
   ```python
   # Build complete REST client with CRUD operations
   ```

9. **Web Scraper**
   ```python
   # Build scraper with retry and rate limiting
   ```

---

## Quick Reference Card

```python
import requests

# GET
response = requests.get(url)
response = requests.get(url, params={'key': 'value'})

# POST
response = requests.post(url, data={'key': 'value'})
response = requests.post(url, json={'key': 'value'})
response = requests.post(url, files={'file': open('file.txt', 'rb')})

# Other methods
requests.put(url, data=data)
requests.delete(url)
requests.patch(url, json=data)
requests.head(url)
requests.options(url)

# Headers & Auth
response = requests.get(url, headers={'User-Agent': 'MyApp'})
response = requests.get(url, auth=('user', 'pass'))
response = requests.get(url, auth=HTTPBearerAuth(token))

# Response handling
response.status_code
response.headers
response.text          # String content
response.content       # Bytes content
response.json()        # Parse JSON
response.raise_for_status()

# Sessions
session = requests.Session()
session.headers.update({'User-Agent': 'MyApp'})
session.get(url)
session.close()

# Error handling
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    pass
except requests.exceptions.HTTPError as e:
    print(e.response.status_code)
```

---

## Next Step

- Move to [03_virtual_env.md](03_virtual_env.md) to learn about virtual enviorments.

---

*Master requests to interact with REST APIs and web services! 🐍✨*