import os
import platform
import subprocess
import ctypes
import sys

def set_wallpaper_windows(image_path):
    # SPI_SETDESKWALLPAPER = 20
    try:
        result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        if not result:
            raise Exception("SystemParametersInfoW failed.")
    except Exception as e:
        print(f"Failed to set wallpaper on Windows: {e}")

def set_wallpaper_macos(image_path):
    try:
        script = f'''
        tell application "System Events"
            set desktopCount to count of desktops
            repeat with desktopNumber from 1 to desktopCount
                tell desktop desktopNumber
                    set picture to "{image_path}"
                end tell
            end repeat
        end tell
        '''
        subprocess.run(["osascript", "-e", script])
    except Exception as e:
        print(f"Failed to set wallpaper on macOS: {e}")

def set_wallpaper_linux(image_path):
    # Try for GNOME
    try:
        # GNOME 3/4
        subprocess.run([
            "gsettings", "set", "org.gnome.desktop.background", "picture-uri",
            f"file://{image_path}"
        ], check=True)
        return
    except Exception:
        pass
    # Try for KDE Plasma
    try:
        script = f"""
        var Desktops = desktops();
        for (i=0;i<Desktops.length;i++) {{
            d = Desktops[i];
            d.wallpaperPlugin = "org.kde.image";
            d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
            d.writeConfig("Image", "file://{image_path}")
        }}
        """
        subprocess.run(['qdbus-qt5', 'org.kde.plasmashell', '/PlasmaShell', 'org.kde.PlasmaShell.evaluateScript', script])
        return
    except Exception:
        pass
    print("Failed to set wallpaper: Desktop environment not supported or required tool not installed.")

def set_wallpaper(image_path):
    if not os.path.isfile(image_path):
        print(f"Image not found: {image_path}")
        sys.exit(1)

    current_os = platform.system()
    if current_os == "Windows":
        set_wallpaper_windows(image_path)
    elif current_os == "Darwin":
        set_wallpaper_macos(image_path)
    elif current_os == "Linux":
        set_wallpaper_linux(image_path)
    else:
        print(f"Unsupported OS: {current_os}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python change_wallpaper.py <path_to_image>")
        sys.exit(1)
    set_wallpaper(sys.argv[1])
