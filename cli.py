import upload
import PIL as pillow
import sys

# Basically the gui app, but only with commands

def main() -> None:
    print("| StrawPage Image Command Generator |")
    print("Please input the StrawPage URL:\n")
    url: str = input()
    print("\nPlease input the path to the image you want to upload:\n")
    path: str = input()

    try:
        image = pillow.Image.open(path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    upload.ToStrawpage(url, image)

if __name__ == "__main__":
    main()