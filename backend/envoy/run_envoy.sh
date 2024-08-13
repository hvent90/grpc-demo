# !/bin/bash

docker run -d --name envoy \
  -p 8080:8080 \
  -v $(pwd)/envoy.yaml:/etc/envoy/envoy.yaml \
  envoyproxy/envoy:v1.25-latest