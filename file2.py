import asyncio
print("Starting in file2")

async def printTem():
    print("Started")
    await asyncio.sleep(1)
    print("Done")

asyncio.run(printTem())