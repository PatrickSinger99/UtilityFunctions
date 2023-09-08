import base64
from typing import Union
import os


def img_to_base64(img_paths: Union[list, str, os.PathLike], print_results: bool = True) -> dict:
    """
    Encode images to base64 strings.
    INFO: Can be used in tkinter as tk.PhotoImage(data="*base64_string*").

    :param img_paths: Image path, list of image paths, or directory path/paths.
    :param print_results: Print encoded strings when finished.
    :return: Dictionary with keys: image path, and values: base64 image encoding.
    """

    valid_paths = []  # Valid paths to image files extracted from the input paths.
    return_vals = {}  # Return dictionary with key as image path and value the base64 encoding.
    supported_formats = ("jpg", "jpeg", "png", "gif", "webp")  # File types that are converted to base64.

    # If input path is string, convert to list.
    if type(img_paths) is not list:
        img_paths = [img_paths]

    # Extract all valid img paths from the input strings as input can be individual files and directories.
    for path in img_paths:
        try:
            # CASE: Input string is dictionary.
            if os.path.isdir(path):
                for file in os.listdir(path):
                    if os.path.splitext(os.path.join(path, file))[-1][1:].lower() in supported_formats:
                        valid_paths.append(os.path.join(path, file))

            # CASE: Input string is file path.
            elif os.path.isfile(path) and os.path.splitext(path)[-1][1:].lower() in supported_formats:
                valid_paths.append(path)

        except TypeError:
            print("Wrong input Type! Needs to be array of path strings or single path string.")

    # Convert every valid image to base64. Add to return dictionary.
    for img_path in valid_paths:
        with open(img_path, "rb") as file:
            return_vals[img_path] = base64.b64encode(file.read()).decode("utf-8")

    # If printing is enabled, print every encoding string (Intended for easy copying).
    if print_results:
        for img_path, encoding in return_vals.items():
            print(f"[{img_path}]\n{encoding}\n")

    return return_vals


if __name__ == '__main__':
    img_to_base64("./test_imgs")
