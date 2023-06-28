import pyautogui


# DRAG FUNCTIONS

def click_and_drag_right(current_drag_values, dragDuration_input):
    pyautogui.mouseDown(current_drag_values['screenshot_value_3'], current_drag_values['click_X'])
    pyautogui.moveTo(current_drag_values['screenshot_value_1'], current_drag_values['click_X'], float(dragDuration_input.get()))
    pyautogui.mouseUp()


def click_and_drag_left(current_drag_values, dragDuration_input):
    pyautogui.mouseDown(current_drag_values['screenshot_value_1'], current_drag_values['click_X'])
    pyautogui.moveTo(current_drag_values['screenshot_value_3'], current_drag_values['click_X'], float(dragDuration_input.get()))
    pyautogui.mouseUp()


def click_and_drag_top(current_drag_values, dragDuration_input):
    pyautogui.mouseDown(current_drag_values['click_Y'], current_drag_values['screenshot_value_2'])
    pyautogui.moveTo(current_drag_values['click_Y'], current_drag_values['screenshot_value_4'], float(dragDuration_input.get()))
    pyautogui.mouseUp()


def click_and_drag_bottom(current_drag_values, dragDuration_input):
    pyautogui.mouseDown(current_drag_values['click_Y'], current_drag_values['screenshot_value_4'])
    pyautogui.moveTo(current_drag_values['click_Y'], current_drag_values['screenshot_value_2'], float(dragDuration_input.get()))
    pyautogui.mouseUp()