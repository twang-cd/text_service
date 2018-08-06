# text-service

`text-service` is a small microservice that provides services for working with strings.

## alphacheck

The `alphacheck` api provides a simple utility that checks if a given string contains all letters of the alphabet.

```
GET /alphacheck/v1/{query}

Checks whether {query} contains all letters of the alphabet.

Params:
  query [string] - The input string.
  
Query Parms:
  case_insensitive [bool] - Flag to determine whether check is case sensitive.  Defaults to True.
  
Request:
  GET /alphacheck/v1/abcdefghijklmnopqrstuvwxyz?case_insensitive=true HTTP/1.1
  Host: 142.93.31.156:8000
  Accept: application/json
  
Response:
  HTTP/1.1 200 OK
  Server: nginx/1.15.2
  Date: Mon, 06 Aug 2018 07:06:05 GMT
  Content-Type: application/json
  Content-Length: 17
  
  {
    "response": true
  }
```

A `v2` endpoint is also available at:

```
GET /alphacheck/v2/{query}
```

The `v2` endpoint implements the alphacheck functionality with a different algorithm with different performance characteristics.

Swagger docs are also available at the `/docs/` endpoint of the service.

# Development

This microservice can be run locally via Docker Compose:

```
$ ./run build
$ ./run up
```

Tests (and coverage, lint) can be run via tox (recommend using virtualenv):

```
$ virtualenv env -p python3
$ source env/bin/activate
$ pip install tox
$ tox
```

