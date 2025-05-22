import asyncio
print("Starting in file2")

async def printTem():
    print("Begin")
    await printTest()
    print("Finish")

async def printTest():
    print("Learning Git")
    await asyncio.sleep(2)
    print("Done for today.")

asyncio.run(printTem())
# asyncio.run(printTest())