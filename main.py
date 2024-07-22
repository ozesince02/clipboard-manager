import tkinter as tk
from tkinter import Menu
import pyperclip  # type: ignore
import keyboard  # type: ignore

clipboard_history = []
updating_history = False

def copy_to_clipboard(item):
    global clipboard_history
    if item in clipboard_history:
        clipboard_history.remove(item)
    clipboard_history.insert(0, item)
    if len(clipboard_history) > 5:
        clipboard_history.pop()
    print(f"\nCopied to clipboard history: {clipboard_history}")

def update_clipboard_history():
    global updating_history
    if updating_history:
        return
    updating_history = True
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_history and clipboard_history[0] == clipboard_content:
            updating_history = False
            return
        if clipboard_content:
            copy_to_clipboard(clipboard_content)
    except Exception as e:
        print(f"Error updating clipboard history: {e}")
    finally:
        updating_history = False

def paste_from_clipboard(index):
    if index < len(clipboard_history):
        pyperclip.copy(clipboard_history[index])
        print(f"\nPasted from clipboard history: {clipboard_history[index]}")

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

def on_copy():
    update_clipboard_history()

def check_clipboard():
    update_clipboard_history()
    root.after(1000, check_clipboard)

def on_exit(event=None):
    root.quit()

keyboard.add_hotkey('ctrl+c', on_copy)

root = tk.Tk()
root.title("Clipboard Manager")

context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Paste Last", command=lambda: paste_from_clipboard(0))
context_menu.add_command(label="Paste Second Last", command=lambda: paste_from_clipboard(1))
context_menu.add_command(label="Paste Third Last", command=lambda: paste_from_clipboard(2))
context_menu.add_command(label="Paste Fourth Last", command=lambda: paste_from_clipboard(3))
context_menu.add_command(label="Paste Fifth Last", command=lambda: paste_from_clipboard(4))

root.bind("<Button-3>", show_context_menu)
root.bind("<Escape>", on_exit)

root.after(1000, check_clipboard)

print("Clipboard manager is running. Press ESC to stop.")
root.mainloop()
