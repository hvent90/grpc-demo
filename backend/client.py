import asyncio
from grpclib.client import Channel
from proto import PingTestServiceStub, PingTestRequest

async def main():
    channel = Channel(host="127.0.0.1", port=5000)
    service = PingTestServiceStub(channel)
    ping_request = PingTestRequest(message="hello")
    response = await service.ping(ping_request)
    print(response.message)
    channel.close()


if __name__ == "__main__":
    asyncio.run(main())
    
