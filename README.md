# Kahoot-Answer-Bot
Simple Kahoot answer bot with automatic answer feature.

![thumbnail](https://github.com/WODdev/Kahoot-Answer-Bot/assets/150499155/9c1425ef-8928-481c-8d97-a31800402b51)


## **USAGE**:

- install the necessary packages:
```
pip install keyboard pyautogui colorama
```
- cd the folder:
- run the kahoot.py file
```
python kahoot.py
```

## Once You Run
once you run the file it should look something like this:
```
██╗░░██╗░█████╗░██╗░░██╗░█████╗░░█████╗░████████╗  ██████╗░░█████╗░████████╗
██║░██╔╝██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝
█████═╝░███████║███████║██║░░██║██║░░██║░░░██║░░░  ██████╦╝██║░░██║░░░██║░░░
██╔═██╗░██╔══██║██╔══██║██║░░██║██║░░██║░░░██║░░░  ██╔══██╗██║░░██║░░░██║░░░
██║░╚██╗██║░░██║██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░  ██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░
By WODdev

- Kahoot must be public
        - Get the uuid by typing the long string in the teacher's search bar that comes after "quizid"
        - Example :https://play.kahoot.it/v2/lobby?quizId=d48a7243-48b4-457f-b69a-19be0182dfa5
                                                          ↑ starts here                      ↑ ends here
Enter uuid:
```
- now enter the kahoot uuid that appears after the quizId statement in the kahoot link.

### **EXAMPLE**:
```
d48a7243-48b4-457f-b69a-19be0182dfa5
```

Example output:
```
red
1: Amygdala

blue
3: decrease

yellow
4: Cerebrum

etc..

Press shift to auto answer when ready...
```
- Finally, press shift to automatically move the mouse cursor to the answer when ready.

## HAVE FUN!
**Liscence** : MIT
