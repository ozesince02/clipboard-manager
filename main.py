import keyboard # type: ignore
import pyperclip # type: ignore

clipboard_history = []

def copy_to_clipboard(item):
    global clipboard_history
    clipboard_history.insert(0, item)
    if len(clipboard_history) > 5:
        clipboard_history.pop()
    print(f"Copied to clipboard history: {clipboard_history}")

def paste_from_clipboard(index):
    if index < len(clipboard_history):
        pyperclip.copy(clipboard_history[index])
        keyboard.write(clipboard_history[index])
        print(f"Pasted from clipboard history: {clipboard_history[index]}")

def on_copy():
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_history and clipboard_history[0] == clipboard_content:
            return
        copy_to_clipboard(clipboard_content)
    except Exception as e:
        print(f"Error copying to clipboard: {e}")

def on_paste(index):
    try:
        paste_from_clipboard(index)
    except Exception as e:
        print(f"Error pasting from clipboard: {e}")

# Register hotkeys
keyboard.add_hotkey('ctrl+c', on_copy)
keyboard.add_hotkey('ctrl+v+f1', lambda: on_paste(0))
keyboard.add_hotkey('ctrl+v+f2', lambda: on_paste(1))
keyboard.add_hotkey('ctrl+v+f3', lambda: on_paste(2))
keyboard.add_hotkey('ctrl+v+f4', lambda: on_paste(3))
keyboard.add_hotkey('ctrl+v+f5', lambda: on_paste(4))

# Start the event loop
print("Clipboard manager is running. Press ESC to stop.")
keyboard.wait('esc')
