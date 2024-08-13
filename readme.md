# GRPC communication between front and backend

## Quick Start

### Prerequisites

- (recommended) Create python venv: `python -m venv .venv && source .venv/bin/activate`
- Docker: Download [4.24.2](https://docs.docker.com/desktop/release-notes/#4242) if you're like me, because it is the newest version that is compatible with Big Sur on your 2014 macbook pro.
- Python packages: `pip install -r requirements.txt`

### Generate the types
```sh
cd proto
npm install
./generate_proto.sh
```

### Run Envoy
`./run_envoy.sh` will download an older version of Envoy: v1.25 - because Macbook 2014.
```sh
cd backend/envoy
./run_envoy.sh
```
For future me, because you will forget - this is how you manage docker:
```
# Check if the docker image has downloaded:
docker images
> envoyproxy/envoy   v1.25-latest   eca697ab203d   10 months ago   161MB

# Check if the container is running
docker container ls
> 58bafe55318d   envoyproxy/envoy:v1.25-latest   "/docker-entrypoint.…"   About an hour ago   Up About an hour   0.0.0.0:8080->8080/tcp, 10000/tcp   envoy

# Stop the docker container
docker ps -a
> 254ab82b3350   envoyproxy/envoy:v1.25-latest   "/docker-entrypoint.…"   13 hours ago        Exited (0) 11 hours ago                                       envoy-envoy-1
docker rm -f {container id, which in this scenario is 254ab82b3350}
```

### Run Backend
```sh
# pip install -r requirements.txt <-- you should have already done this
cd backend
python server.py
```

### (optional) Test GRPC server from Python client
Do this after you have ran the backend.
```sh
cd backend
python client.py
```

### Run Frontend
```sh
cd frontend
npm install
npm run dev
```

Open browser to http://localhost:5173 and look in the console. You should see the grpc response logged.

## Stack

Frontend:
- vite
- typescript
- react
- grpc-web

Envoy:
- listens on port 8080

Backend:
- python
- grpc
- listens on port 5000

## A poem

Stop closing unresolved github issues.

