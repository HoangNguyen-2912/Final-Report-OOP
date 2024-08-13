import tkinter as tk
import tkinter.scrolledtext as tkst

class UpdateVideos():
    def __init__(self, window):
        # Set window size and title
        window.geometry("800x600")
        window.title("Video Update")

        # Initialize a dictionary to store video data
        self.videos = {}

        # Title label with padding
        title_lbl = tk.Label(window, text="Video Update", font=("Helvetica", 18, "bold"))
        title_lbl.grid(row=0, column=0, columnspan=2, pady=10)

        # Frame for input fields
        input_frame = tk.Frame(window, padx=20, pady=10, relief=tk.GROOVE, borderwidth=2)
        input_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # Label and Entry for video number
        number_lbl = tk.Label(input_frame, text="Video Number:", font=("Helvetica", 12))
        number_lbl.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.number_txt = tk.Entry(input_frame, width=10, font=("Helvetica", 12))
        self.number_txt.grid(row=0, column=1, padx=10, pady=5)

        # Label and Entry for video name
        name_lbl = tk.Label(input_frame, text="New Video Name:", font=("Helvetica", 12))
        name_lbl.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.name_txt = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
        self.name_txt.grid(row=1, column=1, padx=10, pady=5)

        # Label and Entry for director name
        director_lbl = tk.Label(input_frame, text="New Director Name:", font=("Helvetica", 12))
        director_lbl.grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.director_txt = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
        self.director_txt.grid(row=2, column=1, padx=10, pady=5)

        # Label and Entry for video rating
        rating_lbl = tk.Label(input_frame, text="New Rating:", font=("Helvetica", 12))
        rating_lbl.grid(row=3, column=0, padx=10, pady=5, sticky="E")
        self.rating_txt = tk.Entry(input_frame, width=10, font=("Helvetica", 12))
        self.rating_txt.grid(row=3, column=1, padx=10, pady=5, sticky="W")

        # Frame for buttons
        button_frame = tk.Frame(window, padx=20, pady=10)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Button to update video details
        update_btn = tk.Button(button_frame, text="Update Video", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.update_video_clicked)
        update_btn.grid(row=0, column=0, padx=10, pady=5)

        # Button to clear the form
        clear_btn = tk.Button(button_frame, text="Clear Form", font=("Helvetica", 12), bg="#f44336", fg="white", command=self.clear_form)
        clear_btn.grid(row=0, column=1, padx=10, pady=5)

        # Frame for displaying current videos
        display_frame = tk.Frame(window, padx=20, pady=10, relief=tk.GROOVE, borderwidth=2)
        display_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        display_lbl = tk.Label(display_frame, text="Current Videos:", font=("Helvetica", 12, "bold"))
        display_lbl.grid(row=0, column=0, padx=5, pady=5)

        self.current_videos_txt = tkst.ScrolledText(display_frame, width=75, height=10, font=("Helvetica", 12))
        self.current_videos_txt.grid(row=1, column=0, padx=5, pady=5)

        # Status label with a distinct background
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10, "italic"), bg="#ddd", anchor="w", padx=10)
        self.status_lbl.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    def update_video_clicked(self):
        # Get user inputs
        video_number = self.number_txt.get().strip()
        video_name = self.name_txt.get().strip()
        director_name = self.director_txt.get().strip()
        rating = self.rating_txt.get().strip()

        if video_number and video_name and director_name and rating:
            # Update video details in the dictionary
            self.videos[video_number] = {
                "name": video_name,
                "director": director_name,
                "rating": rating
            }

            # Create a status message
            status_message = f"Video {video_number} updated: '{video_name}', Director: '{director_name}', Rating: '{rating}'."
            self.status_lbl.configure(text=status_message, fg="green")

            # Refresh the display of current videos
            self.display_videos()

            # Clear the form fields
            self.clear_form()

        else:
            # Notify the user if any fields are empty
            self.status_lbl.configure(text="All fields must be filled out.", fg="red")

    def display_videos(self):
        # Clear the ScrolledText widget before updating it
        self.current_videos_txt.delete(1.0, tk.END)

        # Display all videos in the ScrolledText widget
        for number, details in self.videos.items():
            video_info = f"Video {number}: Name: '{details['name']}', Director: '{details['director']}', Rating: '{details['rating']}'\n"
            self.current_videos_txt.insert(tk.END, video_info)

    def clear_form(self):
        # Clear all entry fields
        self.number_txt.delete(0, tk.END)
        self.name_txt.delete(0, tk.END)
        self.director_txt.delete(0, tk.END)
        self.rating_txt.delete(0, tk.END)
        self.status_lbl.configure(text="")

if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    # Initialize the UpdateVideos application
    UpdateVideos(window)
    # Start the main event loop
    window.mainloop()
