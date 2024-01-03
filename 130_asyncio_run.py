import asyncio

async def main():
    print("main() has been started. sleep 2s")
    await asyncio.sleep(2)
    print("main() has been finished.")

# Ex1: Not using asyncio.run()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    asyncio.set_event_loop(None)
    loop.close()

# Ex2: Using asyncio.run()
asyncio.run(main())
