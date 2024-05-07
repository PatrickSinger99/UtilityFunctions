from PIL import Image


def change_icon_color(img_obj: Image, target_color: tuple):

    img_obj = img_obj.convert('RGBA')  # Open the source image and convert it to RGBA mode
    data = img_obj.getdata()  # Load the image data into a list

    # Create a new data list
    new_data = []

    # Replace black color with the desired target color
    for item in data:
        # Change all black (also shades of blacks) pixels to the target color
        new_data.append((target_color[0], target_color[1], target_color[2], item[3]))

    # Update image data
    img_obj.putdata(new_data)

    return img_obj
