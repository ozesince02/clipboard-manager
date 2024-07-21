import tkinter as tk
from tkinter import Menu
import pyperclip # type: ignore
import keyboard # type: ignore

clipboard_history = []

def copy_to_clipboard(item):
    global clipboard_history
    clipboard_history.insert(0, item)
    if len(clipboard_history) > 5:
        clipboard_history.pop()
    print(f"Copied to clipboard history: {clipboard_history}")

def update_clipboard_history():
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_history and clipboard_history[0] == clipboard_content:
            return
        copy_to_clipboard(clipboard_content)
    except Exception as e:
        print(f"Error updating clipboard history: {e}")

def paste_from_clipboard(index):
    if index < len(clipboard_history):
        pyperclip.copy(clipboard_history[index])
        root.clipboard_clear()
        root.clipboard_append(clipboard_history[index])
        print(f"Pasted from clipboard history: {clipboard_history[index]}")

def show_context_menu(event):
    update_clipboard_history()
    context_menu.tk_popup(event.x_root, event.y_root)

def on_copy():
    update_clipboard_history()

# Set up the keyboard event listener for Ctrl+C
keyboard.add_hotkey('ctrl+c', on_copy)

# Create the main application window
root = tk.Tk()
root.title("Clipboard Manager")

# Create a context menu
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Paste Last", command=lambda: paste_from_clipboard(0))
context_menu.add_command(label="Paste Second Last", command=lambda: paste_from_clipboard(1))
context_menu.add_command(label="Paste Third Last", command=lambda: paste_from_clipboard(2))
context_menu.add_command(label="Paste Fourth Last", command=lambda: paste_from_clipboard(3))
context_menu.add_command(label="Paste Fifth Last", command=lambda: paste_from_clipboard(4))

# Bind right-click to show the context menu
root.bind("<Button-3>", show_context_menu)

# Start the main event loop
print("Clipboard manager is running. Press ESC to stop.")
root.mainloop()
