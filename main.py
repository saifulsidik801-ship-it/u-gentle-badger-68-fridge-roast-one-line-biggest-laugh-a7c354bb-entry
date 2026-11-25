import os

ENTRY = "My smart fridge pushed a firmware update at 3 AM and now the ice maker holds my cubes hostage until I rate the update five stars."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
