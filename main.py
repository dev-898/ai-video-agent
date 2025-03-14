from moviepy.editor import TextClip, CompositeVideoClip

# Step 1: Define your message (pretend this is your Medium content summary)
message = "Boost Your Productivity! 🚀\nRead more on Medium!"

# Step 2: Create a text clip
text_clip = TextClip(message,
                     fontsize=70,
                     color='white',
                     size=(1080, 1920), # Instagram story/reel size
                     method='caption')

# Step 3: Set duration of the clip
text_clip = text_clip.set_duration(7)

# Step 4: Add background color
video = CompositeVideoClip([text_clip.on_color(size=(1080, 1920),
                                               color=(0, 0, 0),
                                               pos=('center', 'center'))])

# Step 5: Export video
video.write_videofile("promo_video.mp4", fps=24)

print("✅ Your video has been created successfully!")
