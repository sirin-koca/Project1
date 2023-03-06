from IPython.display import display, Image, HTML, Audio, Video

# Display text
text = "Hello, World!"
display(text)

# Display img
image_path = "path/to/image.jpg"
Image(filename=image_path)

# Display HTML
html_code = "<h1>Hello, World!</h1>"
HTML(html_code)

# Display audio
audio_path = "path/to/audio.mp3"
Audio(filename=audio_path)

# Display video
video_path = "path/to/video.mp4"
Video(filename=video_path)


