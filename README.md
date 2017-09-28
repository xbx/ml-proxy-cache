# ML

Author: Roberto Bravo
Time: 4hs

# Usage

```
docker-compose up -d
```

```
curl http://127.0.0.1:8080/items/MLA641513497/
```

```
curl http://127.0.0.1:8080/health
{
  "avg_response_time": 0.3853865274383376,
  "avg_response_time_api_calls": 0.38253239790598553,
  "total_requests": 6
}
```

Kibana available at: http://localhost:5601/
API Standard https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md
Implementation: Easy Swagger UI for your Flask API https://github.com/rochacbruno/flasgger

API Framework: Flask (Python)
Storage: Redis (Items), Elastisearch (Health)


TODO:

- UniTest
- Config files (hosts, debug, etc)
- Exception handling (at several layers)
- More features that /health should check
- A lot of code polishing
