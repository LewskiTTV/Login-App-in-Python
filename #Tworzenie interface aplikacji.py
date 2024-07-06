import tkinter as tk
import os

# Function to save login data to a file
def save_login(username, password):
    # Get the current directory
    actual_directory = os.path.dirname(__file__)
    # Open the file in append mode
    with open(os.path.join(actual_directory, "logins.txt"), "a") as file:
        username = username.encode("utf-8").hex()
        password = password.encode("utf-8").hex()
        # Write the login data to the file
        file.write(f"{username}:{password}\n")

# Function to find login data in a file
def find_login(username, password):
    # Get the current directory
    actual_directory = os.path.dirname(__file__)
    encoded_username = username.encode("utf-8").hex()
    encoded_password = password.encode("utf-8").hex()
    try:
        # Open the file in read mode
        with open(os.path.join(actual_directory, "logins.txt"), "r") as file:
            # Search for the login data in the file
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if encoded_username == stored_username and encoded_password == stored_password:
                    return True
    except FileNotFoundError:
        return False
    return False

# Login menu class
class LoginMenu:
    def __init__(self, master):
        self.master = master
        master.title("Login Menu")

        # Create a frame for the buttons
        self.choice_frame = tk.Frame(master)
        self.choice_frame.pack()

        # Create a login button
        self.login_button = tk.Button(self.choice_frame, text="Login", command=self.show_login_window)
        self.login_button.pack(side=tk.LEFT)

        # Create a register button
        self.register_button = tk.Button(self.choice_frame, text="Register", command=self.show_register_window)
        self.register_button.pack(side=tk.LEFT)

        # Create a frame for the content
        self.content_frame = tk.Frame(master)
        self.content_frame.pack()

    # Function to show the login window
    def show_login_window(self):
        # Clear the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Create a username label
        self.username_label = tk.Label(self.content_frame, text="Username:")
        self.username_label.pack()

        # Create a username entry field
        self.username_entry = tk.Entry(self.content_frame)
        self.username_entry.pack()

        # Create a password label
        self.password_label = tk.Label(self.content_frame, text="Password:")
        self.password_label.pack()

        # Create a password entry field
        self.password_entry = tk.Entry(self.content_frame, show="*")
        self.password_entry.pack()

        # Create a show password checkbox
        self.show_password_var = tk.IntVar()
        self.show_password_checkbox = tk.Checkbutton(self.content_frame, text="Show password", variable=self.show_password_var, command=self.show_password)
        self.show_password_checkbox.pack()

        # Create a submit button
        self.submit_button = tk.Button(self.content_frame, text="Submit", command=self.submit_login)
        self.submit_button.pack()

    # Function to show the register window
    def show_register_window(self):
        # Clear the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Create a username label
        self.username_label = tk.Label(self.content_frame, text="Username:")
        self.username_label.pack()

        # Create a username entry field
        self.username_entry = tk.Entry(self.content_frame)
        self.username_entry.pack()

        # Create a password label
        self.password_label = tk.Label(self.content_frame, text="Password:")
        self.password_label.pack()

        # Create a password entry field
        self.password_entry = tk.Entry(self.content_frame, show="*")
        self.password_entry.pack()

        # Create a show password checkbox
        self.show_password_var = tk.IntVar()
        self.show_password_checkbox = tk.Checkbutton(self.content_frame, text="Show password", variable=self.show_password_var, command=self.show_password)
        self.show_password_checkbox.pack()

        # Create a submit button
        self.submit_button = tk.Button(self.content_frame, text="Submit", command=self.submit_register)
        self.submit_button.pack()

    # Function to show the password
    def show_password(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    # Function to submit the login
    def submit_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        if find_login(username, password):
            self.message_label = tk.Label(self.content_frame, text="Login successful!")
        else:
            self.message_label = tk.Label(self.content_frame, text="Invalid login or password")
        self.message_label.pack()

    # Function to submit the registration
    def submit_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        if not username or not password:
            self.message_label = tk.Label(self.content_frame, text="Please fill in all fields")
        elif find_login(username, password):
            self.message_label = tk.Label(self.content_frame, text="Login already exists")
        else:
            save_login(username, password)
            self.message_label = tk.Label(self.content_frame, text="Registration successful!")
        self.message_label.pack()

# Create the main window
root = tk.Tk()

# Create a login menu object
login_menu = LoginMenu(root)

# Set the title and size of the main window
root.title("My App")
root.geometry("1200x800")

# Start the main loop
root.mainloop()
