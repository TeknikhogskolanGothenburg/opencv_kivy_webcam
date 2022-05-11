from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import numpy as np
import cv2

vid = cv2.VideoCapture(1)
# --- functions ---

def generate_texture():

    # numpy array
    #img = np.random.randint(0, 256, size=(500, 500, 3), dtype=np.uint8)
    _, img = vid.read()

    cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

    data = img.tobytes()

    # texture
    texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt="bgr")
    texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="bgr")

    return texture


def update_image(dt):
    """Replace texture in existing image."""

    image.texture = generate_texture()


# --- main ---

# empty image at start
image = Image()


class MyPaintApp(App):
    def build(self):
        return image


# run function every 0.25 s
Clock.schedule_interval(update_image, 0.025)

if __name__ == '__main__':
    MyPaintApp().run()
