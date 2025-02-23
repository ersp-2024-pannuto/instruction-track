from moviepy.editor import VideoFileClip, TextClip
import os
# os.environ["IMAGEMAGICK_BINARY"] = "C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"

# print("Using ImageMagick from:", os.environ["IMAGEMAGICK_BINARY"])
try:
    clip = TextClip("Test", fontsize=50, color='white', method='caption')
    print("Success! MoviePy is using ImageMagick.")
except Exception as e:
    print("Error:", e)
