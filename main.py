from mem0 import MemoryClient
client = MemoryClient(api_key="m0-XNp3Y8LxJLfsOHGMxoKQOtFlUx2qZ6d8pmJPNgTP")

# Store user preference
client.add([
    {"role": "user", "content": "I need a developer."},
    {"role": "assistant", "content": "Noted! You need a developer."}
], user_id="user123")

# Later, retrieve and use the preference
query = "What does the user like?"
memory = client.search(query, user_id="user123")
print(f"Retrieved: {memory}")

