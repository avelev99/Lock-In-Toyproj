import cv2
import pyautogui
import time
import numpy

class ImageDetector:
    def __init__(self, image_path):
        self.image_path = image_path

    def detect_and_click(self):
        while True:
            # Take a screenshot of the entire screen
            screenshot = pyautogui.screenshot()
            # Convert the screenshot to a NumPy array
            screenshot_np = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)

            # Load the image to search for
            image = cv2.imread(self.image_path)
            # Check if the image is present in the screenshot
            result = cv2.matchTemplate(screenshot_np, image, cv2.TM_CCOEFF_NORMED)
            # Get the coordinates of the match
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val > 0.9:
                # Calculate the center of the match
                center_x, center_y = max_loc[0] + image.shape[1] // 2, max_loc[1] + image.shape[0] // 2
                # Click on the center of the match
                pyautogui.click(center_x, center_y)
                print("Clicked on the image!")
                break
            else:
                # Wait for 1 second before checking again
                time.sleep(3)

class coordinates_click:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pyautogui.click(self.x, self.y)
        print("Clicked on the coordinates!")

# Create ImageDetector objects for each image
detector1 = ImageDetector("Accept.png")
detector2 = ImageDetector("Search.png")
detector3 = ImageDetector("Ban_Inactive.png")
detector4 = ImageDetector("Ban_Active.png")
detector5 = ImageDetector("Lock_In.png")

# Insert champion name
pick_name = input("Enter champion name: ")
ban_name = input("Enter ban name: ")

import asyncio

async def run_detection_and_clicking_loop(detector, loop):
    while True:
        await detector.detect_and_click()
        if loop==False:
            break
        else:
            continue

async def run_typing_loop(text):
    while True:
        pyautogui.typewrite(text)
        break

async def run_sleeping_loop():
    while True:
        await asyncio.sleep(0.5)
        coordinates_click(962, 454)
        break

async def async_main():
    await asyncio.gather(
        run_detection_and_clicking_loop(detector1, loop=True),
        run_detection_and_clicking_loop(detector2 , loop=False),
        run_typing_loop(pick_name),
        run_sleeping_loop(),
        run_detection_and_clicking_loop(detector3 , loop=False),
        run_typing_loop(ban_name),
        run_sleeping_loop(),
        run_detection_and_clicking_loop(detector4 , loop=False),
        run_detection_and_clicking_loop(detector5 , loop=False)
    )

asyncio.run(async_main())

# q: How do I make a sub branch in a branch?

