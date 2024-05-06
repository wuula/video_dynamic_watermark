#  video_move_watermark

**中文 readme** [README_CN.md](README_CN.md)

# Functionality
A watermark that can be moved on videos, used for copyright protection.

# Background
I run a Taobao shop myself, and some videos need to have a moving watermark added. After searching online and finding that most options were either paid or lacked batch processing capabilities, I decided to write my own.

# Features
The functionality is quite simple. There are two types of watermarks: one moves from top to bottom, and the other moves from bottom to top. The principle is to add the watermark frame by frame and gradually move it. Users with more complex requirements can freely modify it.

# Usage
My Python version is 3.10, theoretically 3.6 or above is acceptable

Open `video_move_watermark.py` and replace the configurations below with your own preferences:

```
# Define watermark text and font
text1 = "Shuke is flying the plane" # Top watermark
text2 = "Beta is driving the tank" # Bottom watermark
font_path = "font/Arial Unicode.ttf" # Please replace with your font file path
font_size = 36 # Text size
font_color = (255, 255, 255) # White

# Input and output folder paths
input_folder = "1/" # Input folder
output_folder = "2/" # Output folder
```

Then execute the command:

```
pip install -r requirements.txt 
python video_move_watermark.py
```

# Effect

![demo](demo.png)
