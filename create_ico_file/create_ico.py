from PIL import Image
import os


def create_ico(input_image, output_path="./icon", resize=None):
    image = Image.open(input_image).convert("RGBA")

    # Resizing
    if resize is not None:
        image = image.resize((resize, resize))

    # Save the image as an ico file
    image.save(os.path.join(output_path, os.path.basename(input_image).split(".")[0] + ".ico"))


if __name__ == "__main__":
    create_ico(r"**.png", r"", 128)
