
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# fig = plt.figure()
# ax  = fig.add_subplot(1,1,1)
# ax.axis([0, 6, 0,6])


# x = np.linspace(0, 2 * np.pi, 120)
# y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# # ims is a list of lists, each row is a list of artists to draw in the
# # current frame; here we are just animating one artist, the image, in
# # each frame
# ims = []
# for i in range(60):
# 	ax.clear()
# 	ax.text(i/20., i/10., 'A')
# 	ax.text(i/10.,i/20.,'B')
# 	fig.savefig(str(i)+'.png')
for the_file in os.listdir('./out'):
	os.remove('./out/'+the_file)
# ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
#                                 repeat_delay=1000)

# ani.save('dynamic_images.mp4')
