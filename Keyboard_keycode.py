import keyboard

def main():
    print("Press any keyboard key (Ctrl + C to exit):")

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f"Key code: {event.scan_code}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
