import asyncio


async def send_message(writer: asyncio.StreamWriter):

    loop = asyncio.get_event_loop()

    while True:
        message = await loop.run_in_executor(None, input)
        writer.write((message + "\n").encode())
        await writer.drain()


async def receive_message(reader: asyncio.StreamReader):

    while True:
        data = await reader.read(1024)
        if not data:
            print("Server disconnected")
            break

        print(data.decode().strip())


async def main():
    reader, writer = await asyncio.open_connection(
        "127.0.0.1", 12345
    )

    print("Connected to server")

    await asyncio.gather(
        send_message(writer),
        receive_message(reader)
    )


asyncio.run(main())
