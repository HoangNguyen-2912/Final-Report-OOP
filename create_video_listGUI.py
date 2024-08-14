import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox, filedialog
from tkinter import font as tkfont
import os

class LibraryItem:
    def __init__(self, key, name, director, rating):
        self.key = key
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0

    def increment_play_count(self):
        self.play_count += 1

class VideoLibrary:
    def __init__(self):
        self.videos = {}
        self.videos["01"] = LibraryItem("01", "Tom and Jerry", "Fred Quimby", 4)
        self.videos["02"] = LibraryItem("02", "Breakfast at Tiffany's", "Blake Edwards", 5)
        self.videos["03"] = LibraryItem("03", "Casablanca", "Michael Curtiz", 2)
        self.videos["04"] = LibraryItem("04", "The Sound of Music", "Robert Wise", 1)
        self.videos["05"] = LibraryItem("05", "Gone with the Wind", "Victor Fleming", 3)

    def get_name(self, key):
        return self.videos[key].name if key in self.videos else None

    def get_director(self, key):
        return self.videos[key].director if key in self.videos else None

    def get_rating(self, key):
        return self.videos[key].rating if key in self.videos else None

    def get_play_count(self, key):
        return self.videos[key].play_count if key in self.videos else None

    def increment_play_count(self, key):
        if key in self.videos:
            self.videos[key].increment_play_count()

    def list_videos(self, keys):
        output = ""
        for key in keys:
            if key in self.videos:
                video = self.videos[key]
                output += f"{key}: {video.name}\n"
        return output

    def search_videos_by_name(self, name):
        results = [key for key, video in self.videos.items() if name.lower() in video.name.lower()]
        return results

    def search_videos_by_director(self, director):
        results = [key for key, video in self.videos.items() if director.lower() in video.director.lower()]
        return results

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class PlaylistManager:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x700")
        self.window.title("Video Playlist Manager")
        self.videos = []
        self.current_index = -1  # To keep track of the current video in the playlist

        # Create a Font
        self.custom_font = tkfont.Font(family="Helvetica", size=12)

        # Initialize the video library
        self.video_library = VideoLibrary()

        # Header Label
        self.header_lbl = tk.Label(window, text="Video Playlist Manager", font=("Helvetica", 16, "bold"))
        self.header_lbl.grid(row=0, column=0, columnspan=6, pady=10)

        # Search and Add Frame
        self.frame_search_add = tk.Frame(window)
        self.frame_search_add.grid(row=1, column=0, columnspan=6, pady=10)

        self.search_lbl = tk.Label(self.frame_search_add, text="Search (Video Name or Director):", font=self.custom_font)
        self.search_lbl.grid(row=0, column=0, padx=10)

        self.search_txt = tk.Entry(self.frame_search_add, width=30, font=self.custom_font)
        self.search_txt.grid(row=0, column=1, padx=10)

        self.search_video_btn = tk.Button(self.frame_search_add, text="Search Video", font=self.custom_font, command=self.search_video_clicked)
        self.search_video_btn.grid(row=0, column=2, padx=10)

        self.search_director_btn = tk.Button(self.frame_search_add, text="Search Director", font=self.custom_font, command=self.search_director_clicked)
        self.search_director_btn.grid(row=0, column=3, padx=10)

        self.enter_lbl = tk.Label(self.frame_search_add, text="Enter Video Number", font=self.custom_font)
        self.enter_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(self.frame_search_add, width=10, font=self.custom_font)
        self.input_txt.grid(row=1, column=1, padx=10, pady=10)

        self.add_btn = tk.Button(self.frame_search_add, text="Add to Playlist", font=self.custom_font, command=self.add_video_clicked)
        self.add_btn.grid(row=1, column=2, padx=10, pady=10)

        self.play_btn = tk.Button(self.frame_search_add, text="Play", font=self.custom_font, command=self.play_video_clicked)
        self.play_btn.grid(row=1, column=3, padx=10, pady=10)

        # Playlist Frame
        self.frame_playlist = tk.Frame(window)
        self.frame_playlist.grid(row=2, column=0, rowspan=2, columnspan=3, pady=10, padx=10, sticky="nsew")

        self.playlist_lbl = tk.Label(self.frame_playlist, text="Playlist", font=self.custom_font)
        self.playlist_lbl.pack()

        self.playlist_txt = tkst.ScrolledText(self.frame_playlist, width=50, height=20, wrap="none", font=self.custom_font)
        self.playlist_txt.pack()

        # Video Details Frame
        self.frame_video_details = tk.Frame(window)
        self.frame_video_details.grid(row=2, column=3, rowspan=2, columnspan=3, pady=10, padx=10, sticky="nsew")

        self.video_details_lbl = tk.Label(self.frame_video_details, text="Video Details", font=self.custom_font)
        self.video_details_lbl.pack()

        self.video_details_txt = tk.Text(self.frame_video_details, width=50, height=20, wrap="none", font=self.custom_font)
        self.video_details_txt.pack()

        # Status Label
        self.status_lbl = tk.Label(window, text="", font=self.custom_font, fg="blue")
        self.status_lbl.grid(row=5, column=0, columnspan=6, pady=10)

        # Navigation Buttons Frame
        self.frame_navigation = tk.Frame(window)
        self.frame_navigation.grid(row=4, column=0, columnspan=6, pady=10)

        self.previous_btn = tk.Button(self.frame_navigation, text="Previous Video", font=self.custom_font, command=self.previous_video_clicked)
        self.previous_btn.grid(row=0, column=0, padx=10)

        self.next_btn = tk.Button(self.frame_navigation, text="Next Video", font=self.custom_font, command=self.next_video_clicked)
        self.next_btn.grid(row=0, column=1, padx=10)

        self.reset_btn = tk.Button(self.frame_navigation, text="Reset Playlist", font=self.custom_font, command=self.reset_video_clicked)
        self.reset_btn.grid(row=0, column=2, padx=10)

        self.save_btn = tk.Button(self.frame_navigation, text="Save Playlist", font=self.custom_font, command=self.save_playlist_clicked)
        self.save_btn.grid(row=0, column=3, padx=10)

        self.load_btn = tk.Button(self.frame_navigation, text="Load Playlist", font=self.custom_font, command=self.load_playlist_clicked)
        self.load_btn.grid(row=0, column=4, padx=10)

        self.delete_btn = tk.Button(self.frame_navigation, text="Delete Video", font=self.custom_font, command=self.delete_video_clicked)
        self.delete_btn.grid(row=0, column=5, padx=10)

    def add_video(self):
        key = self.input_txt.get()
        if key not in self.videos:
            self.videos.append(key)
            output = self.video_library.list_videos(self.videos)
            set_text(self.playlist_txt, output)
        else:
            messagebox.showinfo("Info", "This video is already in the playlist.")

    def check_video_clicked(self):
        key = self.input_txt.get()
        name = self.video_library.get_name(key)
        if name is not None:
            director = self.video_library.get_director(key)
            rating = self.video_library.get_rating(key)
            play_count = self.video_library.get_play_count(key)
            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.video_details_txt, video_details)
        else:
            set_text(self.video_details_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def search_video_clicked(self):
        search_term = self.search_txt.get().strip()
        results = self.video_library.search_videos_by_name(search_term)
        if results:
            output = self.video_library.list_videos(results)
            set_text(self.playlist_txt, output)
            self.status_lbl.configure(text=f"Search results for videos containing '{search_term}'")
        else:
            messagebox.showinfo("Info", "No videos found with the given name.")
            self.status_lbl.configure(text=f"No results for '{search_term}'")

    def search_director_clicked(self):
        search_term = self.search_txt.get().strip()
        results = self.video_library.search_videos_by_director(search_term)
        if results:
            output = self.video_library.list_videos(results)
            set_text(self.playlist_txt, output)
            self.status_lbl.configure(text=f"Search results for directors containing '{search_term}'")
        else:
            messagebox.showinfo("Info", "No directors found with the given name.")
            self.status_lbl.configure(text=f"No results for '{search_term}'")

    def add_video_clicked(self):
        key = self.input_txt.get()
        name = self.video_library.get_name(key)
        if name is not None:
            self.add_video()
            self.current_index = len(self.videos) - 1  # Set current index to the last added video
            self.show_current_video_details()
        else:
            messagebox.showerror("Error", "Please enter a valid number")
        self.status_lbl.configure(text="Add to Playlist button was clicked")

    def play_video_clicked(self):
        self.play_all()
        self.status_lbl.configure(text="Play button was clicked")

    def reset_video_clicked(self):
        self.videos.clear()
        self.current_index = -1  # Reset the current index
        set_text(self.playlist_txt, "")
        set_text(self.video_details_txt, "")
        self.status_lbl.configure(text="Playlist has been reset")

    def previous_video_clicked(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_current_video_details()
        else:
            messagebox.showinfo("Info", "This is the first video in the playlist.")
        self.status_lbl.configure(text="Previous Video button was clicked!")

    def next_video_clicked(self):
        if self.current_index < len(self.videos) - 1:
            self.current_index += 1
            self.show_current_video_details()
        else:
            messagebox.showinfo("Info", "This is the last video in the playlist.")
        self.status_lbl.configure(text="Next Video button was clicked!")

    def delete_video_clicked(self):
        """Delete the current video from the playlist."""
        if 0 <= self.current_index < len(self.videos):
            del self.videos[self.current_index]
            if self.current_index >= len(self.videos):
                self.current_index -= 1
            self.show_current_video_details()
            output = self.video_library.list_videos(self.videos)
            set_text(self.playlist_txt, output)
            self.status_lbl.configure(text="Video deleted from playlist")
        else:
            messagebox.showerror("Error", "No video selected to delete.")

    def play_all(self):
        if 0 <= self.current_index < len(self.videos):
            key = self.videos[self.current_index]
            self.video_library.increment_play_count(key)
            self.show_current_video_details()
        else:
            messagebox.showerror("Error", "No video selected to play.")

    def show_current_video_details(self):
        """Display details of the current video."""
        if 0 <= self.current_index < len(self.videos):
            key = self.videos[self.current_index]
            name = self.video_library.get_name(key)
            director = self.video_library.get_director(key)
            rating = self.video_library.get_rating(key)
            play_count = self.video_library.get_play_count(key)
            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.video_details_txt, video_details)
        else:
            set_text(self.video_details_txt, "")

    def save_playlist_clicked(self):
        """Save the current playlist to a file."""
        if not self.videos:
            messagebox.showinfo("Info", "No videos in the playlist to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                for key in self.videos:
                    file.write(f"{key}\n")
            messagebox.showinfo("Success", f"Playlist saved to {file_path}")

    def load_playlist_clicked(self):
        """Load a playlist from a file."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    self.videos = [line.strip() for line in file if line.strip() in self.video_library.videos]
                self.current_index = 0 if self.videos else -1
                output = self.video_library.list_videos(self.videos)
                set_text(self.playlist_txt, output)
                self.show_current_video_details()
                self.status_lbl.configure(text=f"Playlist loaded from {file_path}")
            else:
                messagebox.showerror("Error", f"Cannot open file: {file_path}")


if __name__ == "__main__":
    window = tk.Tk()
    PlaylistManager(window)
    window.mainloop()
