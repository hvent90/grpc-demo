# GRPC communication between front and backend

## Quick Start

### Prerequisites

- Docker: Download [4.24.2](https://docs.docker.com/desktop/release-notes/#4242), because it is the newest version that is compatible with Big Sur.
- Python packages: `pip install -r requirements.txt`

### Generate the types
```sh
cd proto && ./generate_proto.sh
```

### Run Envoy
```sh
cd backend/envoy && ./run_envoy.sh
```

### Run Backend
```sh
# pip install -r requirements.txt <-- you should have already done this
cd backend && python server.py
```

### (optional) Test GRPC server from Python client
Do this after you have ran the backend.
```sh
cd backend && python client.py
```

### Run Frontend
```sh
cd frontend
npm install
npm run dev
```

Open browser to localhost:5173 and look in the console. You should see the grpc response logged.

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

