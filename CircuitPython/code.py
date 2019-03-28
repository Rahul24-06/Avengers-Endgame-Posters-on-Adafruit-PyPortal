import time
import board
from adafruit_pyportal import PyPortal
# Images
a1 = 'a1.bmp'
a2 = 'a2.bmp'
a3 = 'a3.bmp'
a4 = 'a4.bmp'
a5 = 'a5.bmp'
a6 = 'a6.bmp'
a7 = 'a7.bmp'
a8 = 'a8.bmp'
a9 = 'a9.bmp'
a10 = 'a10.bmp'
a11 = 'a11.bmp'
a12 = 'a12.bmp'
a13 = 'a13.bmp'
a14 = 'a14.bmp'
a15 = 'a15.bmp'
a16 = 'a16.bmp'
a17 = 'a17.bmp'
a18 = 'a18.bmp'
a19 = 'a19.bmp'
a20 = 'a20.bmp'
a21 = 'a21.bmp'
a22 = 'a22.bmp'
a23 = 'a23.bmp'
a24 = 'a24.bmp'

bw = 'bw.bmp'
cap = 'cap.bmp'
hulk = 'hulk.bmp'
iron = 'iron.bmp'
marvel = 'marvel.bmp'
post = 'post.bmp'
spider = 'spider.bmp'
thor = 'thor.bmp'
vis = 'vis.bmp'
witch = 'witch.bmp'

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(status_neopixel=board.NEOPIXEL)

# pyportal.play_file(audio)
# speed up projects with lots of text by preloading the font!
pyportal.preload_font()
pyportal.set_backlight(1.00)
i = 0.001

# disp
pyportal.set_background(a1)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a2)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a3)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a4)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a5)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a6)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a7)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a8)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a9)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a10)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a11)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a12)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a13)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a14)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a15)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a16)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a17)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a18)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a19)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a20)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a21)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a22)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a23)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(a24)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(i)

pyportal.set_background(witch)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(0.5)

pyportal.set_background(vis)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(0.5)

pyportal.set_background(spider)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(0.5)

pyportal.set_background(bw)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(1)

pyportal.set_background(hulk)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(1)

pyportal.set_background(marvel)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(1)

pyportal.set_background(thor)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(1)

pyportal.set_background(cap)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(1)

pyportal.set_background(iron)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(1)

pyportal.set_background(post)
board.DISPLAY.refresh_soon()
board.DISPLAY.wait_for_frame()
time.sleep(5)

while True:
    try:

    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    time.sleep(0.1)