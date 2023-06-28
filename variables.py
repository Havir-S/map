import os

##variables

obserwatorium_delete_colors = [(211, 250, 197), (249, 215, 152), (239, 241, 228), (197, 205, 193), (202, 174, 218), (199, 172, 215), (173, 210, 212), (230, 231, 230), (212, 213, 210), (255, 221, 158), (244, 239, 180), (181, 209, 205), (194, 219, 221), (251, 218, 152), (255, 201, 97), (249, 234, 188), (246, 218, 218), (235, 229, 231), (180, 215, 158), (228, 239, 220), (219, 250, 176), (248, 233, 187), (202, 204, 201), (232, 232, 232), (230, 238, 227), (251, 237, 188), (245, 231, 184), (203, 225, 231), (214, 230, 246), (201, 218, 249), (246, 215, 190), (210, 210, 210), (227, 232, 234), (228, 229, 227), (201, 255, 161), (132, 210, 184), (241, 228, 179), (198, 214, 248), (237, 207, 214), (209, 209, 209), (195, 169, 210), (255, 170, 0), (225, 225, 225), (214, 217, 212), (192, 224, 234), (184, 218, 225), (248, 214, 151), (218, 218, 174), (239, 222, 188), (115, 76, 0), (211, 246, 221)]

obserwatorium_drag_values = {
    "screenshot_value_1": 42,
    "screenshot_value_2": 160,
    "screenshot_value_3": 1900,
    "screenshot_value_4": 995,
    "click_X": 400,
    "click_Y": 452,
    "drag_start_x": 1900,
    "drag_end_x": 42,
    "drag_start_y": 160,
    "drag_end_y": 995,
}

geoportal_drag_values = {
    "screenshot_value_1": 72,
    "screenshot_value_2": 75,
    "screenshot_value_3": 1885,
    "screenshot_value_4": 950,
    "click_X": 400,
    "click_Y": 452,
    "drag_start_x": 1900,
    "drag_end_x": 42,
    "drag_start_y": 160,
    "drag_end_y": 995,
}

current_drag_values = {
    "screenshot_value_1": 42,
    "screenshot_value_2": 160,
    "screenshot_value_3": 1900,
    "screenshot_value_4": 995,
    "click_X": 400,
    "click_Y": 452,
    "drag_start_x": 1900,
    "drag_end_x": 42,
    "drag_start_y": 160,
    "drag_end_y": 995,
}

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
