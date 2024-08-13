# !/bin/bash

cd "$(dirname "$0")"


# Regenerate typescript folder
rm -rf ./typescript
mkdir -p ./typescript

# Generate typescript files
npx protoc \
    --ts_out=./typescript \
    --proto_path=. \
    ./types.proto

# Copy typescript files to frontend
rm -rf ../frontend/src/proto
mkdir -p ../frontend/src/proto
cp -r ./typescript/* ../frontend/src/proto

# Regenerate python folder
rm -rf ./python
mkdir -p ./python

# Generate python files
python -m grpc_tools.protoc \
    -I . \
    --python_betterproto_out=./python \
    types.proto

# Copy python files to backend
rm -rf ../backend/proto
mkdir -p ../backend/proto
cp -r ./python/*/** ../backend/proto