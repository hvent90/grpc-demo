# import asyncio
# import sys
# import os

# # Add the directory containing the proto files to the Python path
# import os
# import sys


# proto_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'proto_generated')
# sys.path.insert(0, proto_dir)

# # # Add the Backend directory to the Python path
# backend_dir = os.path.dirname(os.path.dirname(__file__))
# sys.path.insert(0, backend_dir)

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
    