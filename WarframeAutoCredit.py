import pyautogui
import keyboard
import random
import time
import threading

macro_running = False

# Coordinates and color for the operator form check
x, y = 1855, 958  # Screen coordinates
operator_color = (230, 229, 229)  # RGB color in operator form of the screen element I want

def check_operator_form():
    # Check if the color at the specified coordinates matches the operator color.
    pixel_color = pyautogui.pixel(x, y)
    return pixel_color == operator_color

def run_macro():
    while macro_running:
        # Press '5' to switch to operator form
        keyboard.press('5')
        time.sleep(random.uniform(0.05, 0.1))
        keyboard.release('5')
        time.sleep(random.uniform(0.5, 0.7))  # Small delay before pressing '5' again to prevent phantom presses

        # Press '5' again to switch back to Umbra form
        keyboard.press('5')
        time.sleep(random.uniform(0.05, 0.1))
        keyboard.release('5')

        keyboard.press('a')
        time.sleep(random.uniform(1,2))
        keyboard.release('a')


        # Wait for a random time before restarting the loop to prevent AFK kicks
        time.sleep(random.uniform(3, 5))

        # Check if we are still in operator form at the end of the loop
        if not check_operator_form():
            print("Not in operator form! Pressing '5' to correct")
            keyboard.press('5')
            time.sleep(random.uniform(0.05, 0.1))
            keyboard.release('5')

def toggle_macro():
    global macro_running
    if macro_running:
        # Stop the macro
        macro_running = False
        print("Macro stopped.")
    else:
        # Start the macro
        macro_running = True
        print("Macro started.")
        run_macro_thread = threading.Thread(target=run_macro, daemon=True)
        run_macro_thread.start()

def main():
    print("Press F5 to toggle the macro ON/OFF.")
    while True:
        if keyboard.is_pressed('F5'):  # Toggle macro on/off
            toggle_macro()
            time.sleep(0.5)  # Delay to debounce the key press

if __name__ == "__main__":
    main()
