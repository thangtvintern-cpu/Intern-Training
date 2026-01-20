import asyncio


clients = {}
client_number = 1


async def broadcast(message, sender_writer):

    sender_name = clients[sender_writer]

    for writer, name in clients.items():
        if writer == sender_writer:
            writer.write(f"You: {message}\n".encode())
        else:
            writer.write(f"{sender_name}: {message}\n".encode())

        await writer.drain()


async def handle_client(reader: asyncio.StreamReader,
                        writer: asyncio.StreamWriter):

    global client_number

    addr = writer.get_extra_info("peername")
    username = f"User{client_number}"
    client_number += 1

    clients[writer] = username
    print(f"[+] {username} connected from {addr}")

    try:
        while True:
            data = await reader.read(1024)

            if not data:
                break  

            message = data.decode().strip()
            print(f"{username}: {message}")

            await broadcast(message, writer)

    except Exception as e:
        print(f"[!] {username} error:", e)

    finally:
        print(f"[-] {username} disconnected")
        del clients[writer]

        writer.close()
        await writer.wait_closed()


async def main():

    server = await asyncio.start_server(
        handle_client,
        host="127.0.0.1",
        port=12345
    )

    print("Listening on 127.0.0.1:12345")

    async with server:
        await server.serve_forever()



asyncio.run(main())
