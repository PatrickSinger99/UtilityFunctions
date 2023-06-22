# Import the os and ctypes modules
import os
import ctypes


def set_folder_icon(folder_path, icon_path):
    desktop_ini = os.path.join(folder_path, "desktop.ini")

    # Remove desktop.ini if already there
    if os.path.exists(folder_path):
        os.remove(desktop_ini)

    # Write the configuration to the desktop.ini file
    with open(desktop_ini, "w") as f:
        f.write(f"[.ShellClassInfo]\n"
                f"IconResource={icon_path},0\n"
                f"IconFile=%SystemRoot%\\system32\\SHELL32.dll\n"
                f"IconIndex=0\n")

    # Set the desktop.ini file as hidden and system
    ctypes.windll.kernel32.SetFileAttributesW(desktop_ini, 6)

    # Set the folder as read-only
    ctypes.windll.kernel32.SetFileAttributesW(folder_path, 1)


if __name__ == "__main__":
    folder = r"C:\Users\patri\Downloads\test\New folder (3)"
    icon = r"C:\Users\patri\Downloads\test\New folder\ico.ico"

    set_folder_icon(folder, icon)
