from PIL import ImageGrab

def makeScreenshot(fileName,current_drag_values):
    # capture the screen and crop it to the specified rectangle
    screenshot = ImageGrab.grab(bbox=(
                                    current_drag_values["screenshot_value_1"],
                                    current_drag_values["screenshot_value_2"],
                                    current_drag_values["screenshot_value_3"], 
                                    current_drag_values["screenshot_value_4"]
                                ))
    # save the cropped screenshot to a file
    screenshot.save(fileName)