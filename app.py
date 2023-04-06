import asyncio
import websockets
import json
import numpy as np

testLatentCode_path ="./testingWebApp/data/testLatentCode.npy"
testPointCloud_path = "./testResult/out.npy"

async def handler(websocket):
    async for message in websocket:
        testLatentCode = np.load(testLatentCode_path)
        testPointCloud = np.load(testPointCloud_path)
        examplePC = json.dumps({"requestId": "exampleID", 
                                "latentCodes": testLatentCode.tolist(), 
                                "pointClouds": testPointCloud.tolist()})
        await websocket.send(examplePC)


# entry point
async def main():
    ############## Load Model


    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())