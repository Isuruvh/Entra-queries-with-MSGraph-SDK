import asyncio
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from graph_client1 import get_graph_client


async def list_users():
    client = get_graph_client()
    result = await client.users.get()

    print("=" * 60)
    print("  Microsoft Graph API - User List")
    print("=" * 60)

    if result and result.value:
        print(f"  Total users found: {len(result.value)}")
        print("-" * 60)
        for i, user in enumerate(result.value, start=1):
            print(f"  [{i}] Display Name : {user.display_name}")
            print(f"      Email        : {user.mail or user.user_principal_name}")
            print(f"      User ID      : {user.id}")
            print("-" * 60)
    else:
        print("  No users found.")
        print("-" * 60)

    print("  Done.")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(list_users())
