# HTTP Gateway

```
docker build -t http-gateway .
docker run -e BACKEND=https://httpbin.org -p 5000:5000 http-gateway
open http://localhost:5000/anything?color=blue
curl http://localhost:5000/anything?color=blue
```