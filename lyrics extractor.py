import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch lyrics
def fetch_lyrics():
    song = song_entry.get()
    artist = artist_entry.get()
    if not song or not artist:
        messagebox.showerror("Error", "Please enter both song and artist names.")
        return

    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)

    if response.status_code == 200:
        lyrics = response.json().get('lyrics', 'Lyrics not found')
        lyrics_text.delete(1.0, tk.END)
        lyrics_text.insert(tk.END, lyrics)
    else:
        messagebox.showerror("Error", "Could not fetch lyrics. Please try again.")

# Create the main window
root = tk.Tk()
root.title("Lyrics Fetcher")

# Create and place the labels, entries, and button
tk.Label(root, text="Song:").grid(row=0, column=0)
song_entry = tk.Entry(root)
song_entry.grid(row=0, column=1)

tk.Label(root, text="Artist:").grid(row=1, column=0)
artist_entry = tk.Entry(root)
artist_entry.grid(row=1, column=1)

fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2)

# Text area to display lyrics
lyrics_text = tk.Text(root, height=20, width=50)
lyrics_text.grid(row=3, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
