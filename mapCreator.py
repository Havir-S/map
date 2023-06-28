import time
import tkinter as tk
from PIL import ImageGrab
import os
from PIL import Image, ImageEnhance
import keyboard
from PIL import ImageOps
from variables import obserwatorium_drag_values, geoportal_drag_values, current_drag_values, desktop_path, obserwatorium_delete_colors
from libs.dragFunctions import click_and_drag_right, click_and_drag_left, click_and_drag_top, click_and_drag_bottom
from libs.keyEvents import on_key_event


# STOP PROGRAM key event
keyboard.on_press(on_key_event)


# MAKE SCREENSHOT
def makeScreenshot(fileName):
    global current_drag_values
    # capture the screen and crop it to the specified rectangle
    screenshot = ImageGrab.grab(bbox=(
                                    current_drag_values["screenshot_value_1"],
                                    current_drag_values["screenshot_value_2"],
                                    current_drag_values["screenshot_value_3"], 
                                    current_drag_values["screenshot_value_4"]
                                ))
    # save the cropped screenshot to a file
    screenshot.save(fileName)

# DELETE SCREENSHOTS AFTER FUNCTION DONE PROPERLY

def cleanupScreenshots():
    for filename in os.listdir():
        if filename.startswith("screenshot_row_") and filename.endswith(".png") and filename != "final_result.png":
            os.remove(filename)

# GEOPORTAL - CHANGE SATURATION
def changeSaturationFunc(img):
    global obserwatorium_delete_colors
    # Convert the image to HSV color space
    img_hsv = img.convert("HSV")

    # Adjust the saturation
    saturation_factor = 0.15
    saturation_enhancer = ImageEnhance.Color(img_hsv)
    img_hsv_saturation = saturation_enhancer.enhance(saturation_factor)

    # Convert the image back to RGB color space
    img_result = img_hsv_saturation.convert("RGB")

    # Return the processed image
    return img_result
    
# OBSERWATORIUM - DELETE COLORS
obserwatorium_delete_colors = [(211, 250, 197), (249, 215, 152), (239, 241, 228), (197, 205, 193), (202, 174, 218), (199, 172, 215), (173, 210, 212), (230, 231, 230), (212, 213, 210), (255, 221, 158), (244, 239, 180), (181, 209, 205), (194, 219, 221), (251, 218, 152), (255, 201, 97), (249, 234, 188), (246, 218, 218), (235, 229, 231), (180, 215, 158), (228, 239, 220), (219, 250, 176), (248, 233, 187), (202, 204, 201), (232, 232, 232), (230, 238, 227), (251, 237, 188), (245, 231, 184), (203, 225, 231), (214, 230, 246), (201, 218, 249), (246, 215, 190), (210, 210, 210), (227, 232, 234), (228, 229, 227), (201, 255, 161), (132, 210, 184), (241, 228, 179), (198, 214, 248), (237, 207, 214), (209, 209, 209), (195, 169, 210), (255, 170, 0), (225, 225, 225), (214, 217, 212), (192, 224, 234), (184, 218, 225), (248, 214, 151), (218, 218, 174), (239, 222, 188), (115, 76, 0), (211, 246, 221)]

def turn_colors_to_white(img):
    # Define the color you want to replace it with (white in this case)
    replacement_color = (255, 255, 255)  # RGB value of white

    # Loop through each pixel in the image
    for x in range(img.width):
        for y in range(img.height):
            pixel_color = img.getpixel((x, y))
            # Check if the pixel color is in the obserwatorium_delete_colors array
            if pixel_color in obserwatorium_delete_colors:
                # Replace the pixel color with the replacement color
                img.putpixel((x, y), replacement_color)

    # Save the modified image
    return img

def make_darker(img):
    # inverted_img = ImageOps.invert(img)
    curves_img = ImageOps.autocontrast(img, cutoff=0.2, ignore=None)
    curves_img.save(os.path.join(desktop_path, f'{mapName_input.get()} darker.png'))



# START SCROLLING

def startScrollingGeoportal():
    global current_drag_values
    global geoportal_drag_values
    current_drag_values = geoportal_drag_values
    columns = int(column_input.get() )
    rows = int(row_input.get() )
    for row in range(rows):

        # FIRST ROW REQUIRES NO CLICK_AND_DRAG_BOTTOM
        if row == 0:
            for column in range(columns):
                if column == 0:
                    makeScreenshot(f'screenshot_row_{row}_column_{column}.png')
                else:
                    click_and_drag_right(current_drag_values, dragDuration_input)
                    time.sleep(float(sleepDuration_input.get()))
                    makeScreenshot(f'screenshot_row_{row}_column_{column}.png')
        else:
            click_and_drag_bottom(current_drag_values, dragDuration_input)
            time.sleep(float(sleepDuration_input.get()))
            if row % 2 == 0:
                for column in range(columns):
                    if column == 0:
                        makeScreenshot(f'screenshot_row_{row}_column_{column}.png')
                    else:
                        click_and_drag_right(current_drag_values, dragDuration_input)
                        time.sleep(float(sleepDuration_input.get()))
                        makeScreenshot(f'screenshot_row_{row}_column_{column}.png')
            else:
                for column in range(columns):
                    if column + 1 == columns:
                        time.sleep(float(sleepDuration_input.get()))
                        makeScreenshot(f'screenshot_row_{row}_column_{columns - column - 1}.png')
                    else:
                        time.sleep(float(sleepDuration_input.get()))
                        makeScreenshot(f'screenshot_row_{row}_column_{columns - column - 1}.png')
                        click_and_drag_left(current_drag_values, dragDuration_input)

    # calculate the width and height of the cropped region
    width = current_drag_values["screenshot_value_3"] - current_drag_values["screenshot_value_1"]
    height = current_drag_values["screenshot_value_4"] - current_drag_values["screenshot_value_2"]

    # Create a new blank image for the collage
    collage = Image.new('RGB', (width * columns, height * rows))
    
    for column in range(columns):
        for row in range(rows):
            # print(f'now pasting image from screenshot_column_{column}_row_{row}.png')
            screenshot_path = f'screenshot_row_{row}_column_{column}.png'
            screenshot = Image.open(screenshot_path)
            collage.paste(screenshot, (column * width, row * height))

    ###### ADDITIONAL FUNCTIONALITY
    #SATURATION
    if changeSaturation_state.get():
        collage = changeSaturationFunc(img=collage)

    collage.save(os.path.join(desktop_path, f'{mapName_input.get()}.png'))
    time.sleep(5)
    cleanupScreenshots()

def startScrollingObserwatorium():
    global current_drag_values
    global obserwatorium_drag_values
    current_drag_values = obserwatorium_drag_values
    columns = int(column_input.get() )
    rows = int(row_input.get() )
    for row in range(rows):

        # FIRST ROW REQUIRES NO CLICK_AND_DRAG_BOTTOM
        if row == 0:
            for column in range(columns):
                if column == 0:
                    makeScreenshot(f'screenshot_row_{row}_column_{column}.png')
                else:
                    click_and_drag_right(current_drag_values, dragDuration_input)
                    time.sleep(float(sleepDuration_input.get()))
                    makeScreenshot(f'screenshot_row_{row}_column_{column}.png')
        else:
            click_and_drag_bottom(current_drag_values, dragDuration_input)
            time.sleep(float(sleepDuration_input.get()))
            if row % 2 == 0:
                for column in range(columns):
                    if column == 0:
                        makeScreenshot(f'screenshot_row_{row}_column_{column}.png')
                    else:
                        click_and_drag_right(current_drag_values, dragDuration_input)
                        time.sleep(float(sleepDuration_input.get()))
                        makeScreenshot(f'screenshot_row_{row}_column_{column}.png')
            else:
                for column in range(columns):
                    if column + 1 == columns:
                        time.sleep(float(sleepDuration_input.get()))
                        makeScreenshot(f'screenshot_row_{row}_column_{columns - column - 1}.png')
                    else:
                        time.sleep(float(sleepDuration_input.get()))
                        makeScreenshot(f'screenshot_row_{row}_column_{columns - column - 1}.png')
                        click_and_drag_left(current_drag_values, dragDuration_input)

    # calculate the width and height of the cropped region
    width = current_drag_values["screenshot_value_3"] - current_drag_values["screenshot_value_1"]
    height = current_drag_values["screenshot_value_4"] - current_drag_values["screenshot_value_2"]

    # Create a new blank image for the collage
    collage = Image.new('RGB', (width * columns, height * rows))
    
    for column in range(columns):
        for row in range(rows):
            # print(f'now pasting image from screenshot_column_{column}_row_{row}.png')
            screenshot_path = f'screenshot_row_{row}_column_{column}.png'
            screenshot = Image.open(screenshot_path)
            collage.paste(screenshot, (column * width, row * height))
    

    ###### ADDITIONAL FUNCTIONALITY
    #DELETE COLORS
    if usunKolor_state.get():
        print('usuwamy')
        collage = turn_colors_to_white(img=collage)

    collage.save(os.path.join(desktop_path, f'{mapName_input.get()}.png'))
    #MAKE DARKER
    if zrobCzarne_state.get():
        print('robimy czarne')
        make_darker(collage)


    collage.save(os.path.join(desktop_path, f'{mapName_input.get()}.png'))
    time.sleep(5)
    cleanupScreenshots()

def changeMapType(type):
    global map
    map = type
    if (type == 'Geoportal'):
        print('Geoportal')
        button2.configure(bd=2, highlightbackground='red', bg='blue')
        button1.configure(bd=0, highlightbackground='white', bg='white')
        geoportal_frame.pack(side=tk.LEFT, pady=10, padx=10, anchor="n")
        obserwatorium_frame.pack_forget()
    elif (type == 'Obserwatorium'):
        print('Obserwatorium')
        button1.configure(bd=2, highlightbackground='red', bg='blue')
        button2.configure(bd=0, highlightbackground='white', bg='white')
        obserwatorium_frame.pack(side=tk.LEFT, pady=10, padx=10, anchor="n")
        geoportal_frame.pack_forget()


# Create the tkinter window
window = tk.Tk()
window.configure(bg='gray')

window.geometry("1000x600")



##
# Map type
##

map = 'Geoportal'

chooseMapType_frame = tk.Frame(window, highlightthickness=2,)
chooseMapType_frame.pack(side=tk.LEFT, pady=10, padx=10, anchor="n")
chooseMapType_frame.configure()

image1 = tk.PhotoImage(file="obserwatorium.png")
image2 = tk.PhotoImage(file="geoportal.png")

button1 = tk.Button(chooseMapType_frame, text="Mapa z Obserwatorium", image=image1, command=lambda: changeMapType('Obserwatorium'), compound=tk.TOP, highlightthickness=2, bg='white')
button1.pack(side=tk.TOP, padx=10,)

button2 = tk.Button(chooseMapType_frame, text="Mapa z Geoportalu", image=image2, command=lambda: changeMapType('Geoportal'), compound=tk.TOP, highlightthickness=2, bg='white')
button2.pack(side=tk.TOP, padx=10, pady=5)

##
# Map settings
##

chooseMapSize_frame = tk.Frame(window, bg='gray', highlightthickness=2,)
chooseMapSize_frame.pack(side=tk.LEFT, pady=10, padx=10, anchor="n")
chooseMapSize_frame.configure()

# Create the inputs for rows and columns
column_label = tk.Label(chooseMapSize_frame, text="Kolumny:")
column_label.pack(padx=3,pady=3, fill=tk.BOTH, expand=True,)
column_input = tk.Entry(chooseMapSize_frame,justify='center')
column_input.insert(0, '3') 
column_input.pack()

row_label = tk.Label(chooseMapSize_frame, text="Szeregi:")
row_label.pack(padx=3,pady=3, fill=tk.BOTH, expand=True,)
row_input = tk.Entry(chooseMapSize_frame,justify='center')
row_input.insert(0, '3') 
row_input.pack()

sleepDuration_label = tk.Label(chooseMapSize_frame, text="Czas czekania na załadowanie:")
sleepDuration_label.pack(padx=3,pady=3, fill=tk.BOTH, expand=True,)
sleepDuration_input = tk.Entry(chooseMapSize_frame,justify='center')
sleepDuration_input.insert(0, '4') 
sleepDuration_input.pack()

dragDuration_label = tk.Label(chooseMapSize_frame, text="Czas przesuwania:")
dragDuration_label.pack(padx=3,pady=3, fill=tk.BOTH, expand=True,)
dragDuration_input = tk.Entry(chooseMapSize_frame,justify='center')
dragDuration_input.insert(0, '0.4') 
dragDuration_input.pack()

mapName_label = tk.Label(chooseMapSize_frame, text="Nazwa mapy:")
mapName_label.pack(padx=3,pady=3, fill=tk.BOTH, expand=True,)
mapName_input = tk.Entry(chooseMapSize_frame,justify='center',)
mapName_input.insert(0, 'Mapa') 
mapName_input.pack()







##
# OBSERWATORIUM SETTINGS
##

obserwatorium_frame = tk.Frame(window, bg='gray', highlightthickness=2,)
obserwatorium_frame.pack(side=tk.LEFT, pady=10, padx=10, anchor="n")

# create a variable to hold the checkbox state
usunKolor_state = tk.BooleanVar()

# create the checkbox using Checkbutton
usunKolory = tk.Checkbutton(obserwatorium_frame, text='Usuń kolory', variable=usunKolor_state, justify='left', anchor='w')

# pack the checkbox onto the window
usunKolory.pack(fill=tk.BOTH, expand=True, anchor='w')

# create a variable to hold the checkbox state
zrobCzarne_state = tk.BooleanVar()

# create the checkbox using Checkbutton
zrobCzarne = tk.Checkbutton(obserwatorium_frame, text='Zrób ciemniejsze kreski', variable=zrobCzarne_state, justify='left', anchor='w')

# pack the checkbox onto the window
zrobCzarne.pack(fill=tk.BOTH, expand=True, anchor='w')

# Create the start button
start_buttonObserwatorium = tk.Button(obserwatorium_frame, text="Start", command=lambda: startScrollingObserwatorium())
start_buttonObserwatorium.pack(padx=3, pady=3, fill=tk.BOTH, expand=True, anchor='w')

# Forget at start
obserwatorium_frame.pack_forget()



##
# GEOPORTAL SETTINGS
##

geoportal_frame = tk.Frame(window, bg='gray', highlightthickness=2,)
geoportal_frame.pack(side=tk.LEFT, pady=10, padx=10, anchor="n")

# create a variable to hold the checkbox state
changeSaturation_state = tk.BooleanVar()

# create the checkbox using Checkbutton
changeSaturation = tk.Checkbutton(geoportal_frame, text='Zrób szarą', variable=changeSaturation_state, justify='left', anchor='w')

# pack the checkbox onto the window
changeSaturation.pack(fill=tk.BOTH, expand=True, anchor='w')

# Create the start button
start_buttongeoportal = tk.Button(geoportal_frame, text="Start", command=lambda: startScrollingGeoportal())
start_buttongeoportal.pack(padx=3, pady=3, fill=tk.BOTH, expand=True, anchor='w')

# Forget at start
geoportal_frame.pack_forget()





# Run the window
window.mainloop()
