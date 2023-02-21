import cv2 as opencv
import pyautogui
import numpy as np
import time

def click_image(image_file, threshold=0.9):
    # Load image to be searched
    image = opencv.imread(image_file, opencv.IMREAD_GRAYSCALE)
    # Capture screenshot of entire screen
    screenshot = pyautogui.screenshot()
    # Convert screenshot to numpy array and grayscale
    screenshot = np.array(screenshot)
    screenshot = opencv.cvtColor(screenshot, opencv.COLOR_BGR2GRAY)
    # Search for image in screenshot using matchTemplate
    result = opencv.matchTemplate(screenshot, image, opencv.TM_CCOEFF_NORMED)
    # Get location of image on screen
    min_val, max_val, min_loc, max_loc = opencv.minMaxLoc(result)
    # Check if maximum value is greater than threshold
    if max_val >= threshold:
        # Calculate coordinates of center of image
        top_left = max_loc
        bottom_right = (top_left[0] + image.shape[1], top_left[1] + image.shape[0])
        center = (int((bottom_right[0] - top_left[0])/2 + top_left[0]), int((bottom_right[1] - top_left[1])/2 + top_left[1]))
        # Click on image
        pyautogui.click(center)
        return True
    else:
        return False


# Prompt user for champion name and ban name
champion_name = input("Enter champion name: ")
ban_name = input("Enter ban name: ")

def run_detection_and_clicking_loop(image_file):
    while not click_image(image_file):
        time.sleep(1)

def champion_pick_and_ban(variable):
    run_detection_and_clicking_loop("Search.png")
    pyautogui.typewrite(variable) # Type champion name
    time.sleep(1)
    pyautogui.click(962, 454) # Click on champion

def start_game():
    search_flag = False
    while True:
        if not search_flag:
            try:
                if click_image("Search.png"):
                    search_flag = True
                    break
            except:
                pass
            click_image("Accept.png")
        time.sleep(1)

def main():
    start_game()
    champion_pick_and_ban(champion_name)
    run_detection_and_clicking_loop("Ban_Inactive.png")
    champion_pick_and_ban(ban_name)
    run_detection_and_clicking_loop("Ban_Active.png")
    run_detection_and_clicking_loop("Lock_In.png")

if __name__ == "__main__":
    main()