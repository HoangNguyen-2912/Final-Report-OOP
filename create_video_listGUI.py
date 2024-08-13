import tkinter as tk
import tkinter.scrolledtext as tkst

class CreateVideoList():
    def __init__(self, window):
        # Set window size
        window.geometry("750x350")
        # Set window title
        window.title("Create Video List")

        # Label for video name
        name_lbl = tk.Label(window, text="Video Name:")
        name_lbl.grid(row=0, column=0, padx=10, pady=10)

        # Entry for video name
        self.name_txt = tk.Entry(window, width=50)
        self.name_txt.grid(row=0, column=1, padx=10, pady=10)

        # Label for director name
        director_lbl = tk.Label(window, text="Director Name:")
        director_lbl.grid(row=1, column=0, padx=10, pady=10)

        # Entry for director name
        self.director_txt = tk.Entry(window, width=50)
        self.director_txt.grid(row=1, column=1, padx=10, pady=10)

        # Label for video rating
        rating_lbl = tk.Label(window, text="Rating:")
        rating_lbl.grid(row=2, column=0, padx=10, pady=10)

        # Entry for video rating
        self.rating_txt = tk.Entry(window, width=50)
        self.rating_txt.grid(row=2, column=1, padx=10, pady=10)

        # Button to save video details
        save_btn = tk.Button(window, text="Save Video", command=self.save_video_clicked)
        save_btn.grid(row=3, column=0, columnspan=2, pady=20)

        # ScrolledText widget to display saved videos
        self.saved_videos_txt = tkst.ScrolledText(window, width=70, height=10, wrap="none")
        self.saved_videos_txt.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=5, column=0, columnspan=2, sticky="W", padx=10, pady=10)

    def save_video_clicked(self):
        # Placeholder for the save functionality
        self.status_lbl.configure(text="Save Video button was clicked!")

if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    # Initialize the CreateVideoList application
    CreateVideoList(window)
    # Start the main event loop
    window.mainloop()

    def save_video_clicked(self):
        # Collecting the video details from entries 
        video_name = self.name_txt.get()
        director_name = self.director_txt.get()
        rating = self.rating_txt.get()

        # Check if all fields are filled
        if video_name and director_name and rating:
            # Append the video details to the ScrolledText widget
            self.saved_videos_txt.insert(tk.END, f"Video Name: {video_name}\n")
            self.saved_videos_txt.insert(tk.END, f"Director Name: {director_name}\n")
            self.saved_videos_txt.insert(tk.END, f"Rating: {rating}\n")
            self.saved_videos_txt.insert(tk.END, "-"*50 + "\n")
            
            # Clear the entry fields after saving
            self.name_txt.delete(0, tk.END)
            self.director_txt.delete(0, tk.END)
            self.rating_txt.delete(0, tk.END)

            # Update the status label
            self.status_lbl.configure(text="Video saved successfully!")
        else:
            # Update the status label if any field is empty 
            self.status_lbl.configure(text="Please fill in all fields!")