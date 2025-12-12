import os
from PIL import Image, ImageFilter

# Path to your dishes folder
INPUT_DIR = "./dishes"
OUTPUT_DIR = os.path.join(INPUT_DIR, "lqip")

# Create LQIP output folder if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Desired LQIP size (tiny + blurred)
LQIP_WIDTH = 40
LQIP_HEIGHT = 40

def create_lqip_image(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGB")

        # Resize to tiny image
        img = img.resize((LQIP_WIDTH, LQIP_HEIGHT), Image.LANCZOS)

        # Add blur effect
        img = img.filter(ImageFilter.GaussianBlur(4))

        # Save as JPEG (quality low to reduce size)
        img.save(output_path, "JPEG", quality=30)
        print(f"Generated: {output_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    if not files:
        print("No image files found in the directory.")
        return

    print("Generating LQIP thumbnails...\n")

    for filename in files:
        input_path = os.path.join(INPUT_DIR, filename)
        name, _ = os.path.splitext(filename)
        output_path = os.path.join(OUTPUT_DIR, f"{name}_low.jpg")

        create_lqip_image(input_path, output_path)

    print("\nDone! LQIP files saved in:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
