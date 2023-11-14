import urllib.request
import json
import colorama
colorama.init()
import pyautogui
import keyboard

print('''
██╗░░██╗░█████╗░██╗░░██╗░█████╗░░█████╗░████████╗  ██████╗░░█████╗░████████╗
██║░██╔╝██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝
█████═╝░███████║███████║██║░░██║██║░░██║░░░██║░░░  ██████╦╝██║░░██║░░░██║░░░
██╔═██╗░██╔══██║██╔══██║██║░░██║██║░░██║░░░██║░░░  ██╔══██╗██║░░██║░░░██║░░░
██║░╚██╗██║░░██║██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░  ██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░
TerrierDev on youtube

- Kahoot must be public
	- Get the uuid by typing the long string in the teacher's search bar that comes after "quizid"
	- Example :https://play.kahoot.it/v2/lobby?quizId=d48a7243-48b4-457f-b69a-19be0182dfa5
	                                                  ↑ starts here			     ↑ ends here''')

def get_answers(id):
    url = f"https://play.kahoot.it/rest/kahoots/{id}"
    color_list = [colorama.Fore.RED + "red", colorama.Fore.BLUE + "blue", colorama.Fore.YELLOW + "yellow", colorama.Fore.GREEN + "green"]
    correct_colors = []  # Create a list to store the correct colors

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
        questions = json.loads(data)["questions"]

        for index, slide in enumerate(questions):
            for i, choice in enumerate(slide.get("choices", [])):
                if choice.get("correct", False):
                    correct_colors.append(i)  # Store the index of the correct answer

        for index, slide in enumerate(questions):
            for i, choice in enumerate(slide.get("choices", [])):
                if choice.get("correct", False):
                    print(f"{color_list[i]}")
                    print(f"{index+1}: {choice.get('answer')}")
                    print()

        for color_index in correct_colors:
            # Map color index to mouse coordinates
            if color_index == 0:  # Red
                x, y = 648, 805
            elif color_index == 1:  # Blue
                x, y = 1550, 804
            elif color_index == 2:  # Yellow
                x, y = 690, 1000
            elif color_index == 3:  # Green
                x, y = 1481, 968

            print("Press shift to auto answer when ready...")

            # Wait for the Shift keypress
            keyboard.wait('shift')

            # Move the mouse and click
            pyautogui.moveTo(x, y)
            pyautogui.click(x, y)

    except urllib.error.HTTPError:
        print("That Kahoot doesn't exist. Your spelling could be incorrect or the Kahoot could be private.")

while True:
    get_answers(input(colorama.Fore.WHITE + "Enter uuid: "))


