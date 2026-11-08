import webbrowser

# Place ID extracted from your game link
place_id = "125967160926572"

# Direct protocol URL to launch the Roblox app
protocol_url = f"roblox://placeId={place_id}/"

print(f"Launching Roblox client for Place ID: {place_id}")
webbrowser.open(protocol_url)