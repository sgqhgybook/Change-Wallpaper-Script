# Change Wallpaper Script

This Python script allows you to change your desktop wallpaper across Windows, macOS, and Linux systems from the command line.

## Features

- **Windows:** Uses Windows API to set the wallpaper.
- **macOS:** Uses AppleScript to update the wallpaper for all Spaces/Desktops.
- **Linux:** Supports GNOME (`gsettings`) and KDE Plasma (`qdbus-qt5`). Other desktop environments may need custom implementation.

## Usage

1. **Clone or download this repository.**

2. **Run the script from the terminal:**

   ```sh
   python change_wallpaper.py /path/to/image.jpg
   ```

   - Replace `/path/to/image.jpg` with the absolute path to your desired wallpaper image.

## Requirements

- **Python 3.x**
- **Windows:** No extra dependencies.
- **macOS:** No extra dependencies.
- **Linux:**
  - GNOME: `gsettings`
  - KDE: `qdbus-qt5`
  - Other desktop environments may not be supported out of the box.

## Notes

- The image path must be absolute.
- On Linux, if you use a desktop environment other than GNOME or KDE, you may need to modify the script for compatibility.
- Some desktop environments may require additional permissions or tools.

## License

MIT License
