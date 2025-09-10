weekly_playlist = ["Blinding Lights", "Levitating", "As It Was", "Heat Waves", "Good 4 u"]
weekly_playlist.append("Drivers License")
weekly_playlist.insert(0,"Bohemian Rhapsody")
weekly_playlist.remove("Good 4 u")

print("Incert a commercial break after Levitating is in the place:")
print(weekly_playlist.index("Levitating"))
print("A special segment is planned where you play all songs by Harry Styles. By him are currently on the playlist this number of songs:")
print(weekly_playlist.count("As It Was"))

print("___Weekly playlist___")
print(weekly_playlist)

print("___Throwback Thursday___")
weekly_playlist.reverse()
print(weekly_playlist)

print("___Alphabetical order___")
weekly_playlist.sort()
print(weekly_playlist)