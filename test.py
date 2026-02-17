import sys
import pyautogui
import time
import os
from PyQt6 import QtWidgets, uic
import webbrowser

list_of_apps = ["Document", "Presentation", "Spreadsheet", "Database", "Email"]

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("interface.ui")

window.DONE.hide()
window.TemplateLabel.hide()
window.TemplateText.hide()

window.FileTypeChooser.addItems(list_of_apps)

def search(temp):
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)
    for i in range(2):
          pyautogui.press('tab')
          time.sleep(0.2)

    pyautogui.write(temp, interval=0.1)
    pyautogui.press('enter')

def start_app():
    file_choice = window.FileTypeChooser.currentText()
    template_choice = window.TemplateText.text()

    window.close()

    if file_choice == "Document":
        os.startfile('winword.exe')
        time.sleep(1.5)
        search(template_choice)
    elif file_choice == "Presentation":
        os.startfile('powerpnt.exe')
        time.sleep(1.5)
        search(template_choice)
    elif file_choice == "Spreadsheet":
        os.startfile('excel.exe')
        time.sleep(1.5)
        search(template_choice)
    elif file_choice == "Database":
        os.startfile('msaccess.exe')
        time.sleep(1.5)
        pyautogui.press('alt')
        time.sleep(0.5)
        pyautogui.press('n')
        time.sleep(0.5)

        for i in range(2):
            pyautogui.press('tab')
            time.sleep(0.2)
        
        pyautogui.write(template_choice, interval=0.1)
        pyautogui.press('enter')
    elif file_choice == "Email":
        webbrowser.open('https://outlook.office.com/mail/')
        time.sleep(3)
        pyautogui.hotkey('n')

def go_to_next_question():
    if window.FileTypeChooser.currentText() == "Email":
        start_app()
        return
        
    window.FileTypeLabel.hide()
    window.FileTypeChooser.hide()
    window.OK.hide()
    window.TemplateLabel.show()
    window.TemplateText.show()
    window.DONE.show()

window.OK.clicked.connect(go_to_next_question)

window.DONE.clicked.connect(start_app)

window.show()
app.exec()