# Envoy Setup

The role of Envoy is that it receives HTTP1 requests from `grpc-web`, converts it to HTTP2, and then forwards the request to the backend GRPC server.

- Envoy is listening on port 8080.
- The backend is listening on port 5000.
- The frontend makes requests to port 8080, which reaches Envoy. Envoy forwards the request to port 5000, which reaches the python backend grpc server.

## Docker
Download [4.24.2](https://docs.docker.com/desktop/release-notes/#4242), because it is the newest version that is compatible with Big Sur.

## Envoy
You can run it via a shell script or via `docker-compose`
- `./run_envoy.sh`
- `docker-compose up -d`

To turn off a docker container:
```
docker ps -a
docker rm -f {container id}
```