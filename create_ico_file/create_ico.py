from PIL import Image


def create_ico(input_image, output_path="./icon.ico", resize=None):
    image = Image.open(input_image).convert("RGBA")

    # Resizing
    if resize is not None:
        image = image.resize((resize, resize))

    # Save the image as an ico file
    image.save(output_path)


if __name__ == "__main__":
    create_ico(r"**.jpg", r"**.ico", 128)
