import asyncio
# from asyncio import futures
# import sys
# import os
# Add the directory containing the proto files to the Python path
# proto_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "proto_generated")
# sys.path.insert(0, proto_dir)

# # Add the Backend directory to the Python path
# backend_dir = os.path.dirname(os.path.dirname(__file__))
# sys.path.insert(0, backend_dir)

from grpclib.server import Server
from proto import PingTestServiceBase, PingTestResponse, PingTestRequest

class PingServiceImpl(PingTestServiceBase):
    async def ping(self, ping_test_request: PingTestRequest) -> PingTestResponse:
        print(ping_test_request)
        return PingTestResponse(message=f"You said: {ping_test_request.message}")
    
async def serve():
    server = Server([PingServiceImpl()])
    await server.start("127.0.0.1", 5000)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(serve())

