import math
import cv2 as cv


class hexcolor:
    def __init__(self, str):
        self.red = int(str[1:3], 16)
        self.green = int(str[3:5], 16)
        self.blue = int(str[5:7], 16)

    def rgb(self):
        return (self.red, self.green, self.blue)

    def brg(self):
        return (self.blue, self.red, self.green)

    def hsv(self):
        r = self.red
        g = self.green
        b = self.blue
        # https://codeigo.com/python/convert-hex-to-rgb-and-hsv#:~:text=Let's%20put%20these%20steps%20into%20Python%20code.&text=To%20convert%20HEX%20to%20HSV,%2D%3ERGB%2D%3EHSV.
        # Normalize R, G, B values
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        # h, s, v = hue, saturation, value
        max_rgb = max(r, g, b)
        min_rgb = min(r, g, b)
        difference = max_rgb-min_rgb

        # if max_rgb and max_rgb are equal then h = 0
        if max_rgb == min_rgb:
            h = 0

        # if max_rgb==r then h is computed as follows
        elif max_rgb == r:
            h = (60 * ((g - b) / difference) + 360) % 360

        # if max_rgb==g then compute h as follows
        elif max_rgb == g:
            h = (60 * ((b - r) / difference) + 120) % 360

        # if max_rgb=b then compute h
        elif max_rgb == b:
            h = (60 * ((r - g) / difference) + 240) % 360

        # if max_rgb==zero then s=0
        if max_rgb == 0:
            s = 0
        else:
            s = (difference / max_rgb) * 100

        # compute v
        v = max_rgb * 100
        # return rounded values of H, S and V
        return tuple(map(round, (h, s, v)))


if __name__ == "__main__":
    gray = hexcolor("#4c4c4c")
    print(gray.rgb())
