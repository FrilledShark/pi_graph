import os
import re

filenames = sorted([frame for frame in os.listdir("frames")], key=lambda x: int(re.search(r'\d+', os.path.splitext(x)[0]).group()))

print("creating gif")
import imageio
with imageio.get_writer('storage/pi.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(os.path.join("frames", filename))
        writer.append_data(image)

print("creating mp4")
import moviepy.editor as mp
clip = mp.VideoFileClip("storage/pi.gif")
clip.write_videofile("storage/pi.mp4")