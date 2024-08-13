import asyncio
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

