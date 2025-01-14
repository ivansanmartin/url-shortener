# URL Shortener API Documentation

## Overview
A URL shortening service that creates shortened URLs with a 5-day expiration period. The service tracks click counts and provides metadata for each shortened URL.

## Base URL
```
ivsm.link
```

## Authentication
All management endpoints require authentication using an API key. **This API uses API Key Manager for API key verification.** (NOT YET).

**Headers Required:**
```
X-API-Key: TOKEN (NOT YET)
```

Failure to provide a valid token will result in a 401 Unauthorized response.

## Endpoints

### 1. Create Shortened URL
Creates a new shortened URL from an original URL.

**Endpoint:** `POST /api/v1/url-shortener`  
**Status Code:** 201 Created  
**Authentication Required:** Yes

**Request Body:**
```json
{
  "original_url": "string"
}
```

**Response:**
```json
{
  "ok": true,
  "message": "URL Shortener created successfully"
}
```

### 2. Get All Shortened URLs
Retrieves a list of all shortened URLs.

**Endpoint:** `GET /api/v1/url-shorteners`  
**Status Code:** 200 OK  
**Authentication Required:** Yes

**Response:**
```json
{
  "ok": true,
  "data": {
    "url_shorteners": [
      {
        "_id": "string",
        "original_url": "string",
        "short_url": "string",
        "slug": "string",
        "created_at": "ISO datetime string",
        "updated_at": "ISO datetime string",
        "clicks": number,
        "expiration_date": "ISO datetime string",
        "metadata": {}
      }
    ]
  }
}
```

### 3. Redirect to Original URL
Redirects to the original URL using the shortened slug.

**Endpoint:** `GET /{slug}`  
**Status Code:** 200 OK  
**Authentication Required:** No

**Path Parameters:**
- `slug`: String (6 characters)

**Response:**
```json
{
  "ok": true,
  "original_url": "string"
}
```

## Error Responses

### Not Found (404)
```json
{
  "ok": false,
  "message": "URL Shortener not found."
}
```

### Unauthorized (401)
```json
{
  "detail": "Token not provided or invalid"
}
```

### MongoDB Error
```json
{
  "ok": false,
  "error": "MongoDB error message"
}
```

## Technical Details

### URL Structure
- Short URL format: `ivsm.link/{slug}`
- Slug length: 6 characters
- Characters used: lowercase letters (a-z)

### Features
- Automatic click tracking
- 5-day expiration period
- Metadata support
- Click counter

### Data Model
```python
{
    "original_url": str,
    "short_url": str,
    "slug": str,
    "created_at": datetime,
    "updated_at": datetime,
    "clicks": int,
    "expiration_date": datetime,
    "metadata": dict
}
```

### Dependencies
- MongoDB for storage
- FastAPI framework
- PyMongo for MongoDB operations

## Example Usage

### Creating a Shortened URL
```bash
curl -X POST "https://ivsm.link/api/v1/url-shortener" \
  -H "X-API-Key: TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://www.example.com/very/long/url"}'
```

### Getting All Shortened URLs
```bash
curl -X GET "https://ivsm.link/api/v1/url-shorteners" \
  -H "X-API-Key: TOKEN"
```

### Using a Shortened URL
```bash
curl -X GET "https://ivsm.link/abcdef"
```

## Notes
- URLs automatically expire after 5 days
- Click counting is automatically incremented on each valid redirect
- The service uses MongoDB for persistence
- All management endpoints require API key authentication
- Slugs are randomly generated using lowercase letters