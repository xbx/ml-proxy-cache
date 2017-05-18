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

Kibana disponible en http://localhost:5601/

Se utilizó el Standard para API's: API Standard https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md
Implementación: Easy Swagger UI for your Flask API https://github.com/rochacbruno/flasgger

API Framework: Flask (Python)
Storage: Redis (Items), Elastisearch (Health)


TODO:

- UniTest
- Config files (hosts, debug, etc)
- Exception handling (En varias capas, especialmente comunicación)
- El resto del /health
- Falta pulir bastante el codigo que ya se hizo rapidamente para poder cumplir con los requisitos.
