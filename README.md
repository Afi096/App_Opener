# 🚀 Office Template Auto-Launcher

A Python-based GUI automation tool that streamlines the process of launching Microsoft Office applications and searching for specific templates. Built with **PyQt6** for the interface and **PyAutoGUI** for keyboard automation.

## 📝 Description

This application provides a user-friendly "Dashboard" to select a Microsoft Office application (Word, Excel, PowerPoint, Access, or Outlook). Depending on the user's choice, it automatically:

1.  Launches the correct application using system commands or URI protocols.
2.  Navigates to the "New" or "Template" gallery.
3.  Types in a search query (e.g., "Resume", "Budget") and executes the search.

It handles application-specific logic, such as different keyboard shortcuts for Access vs. Word and using URI schemes for modern Outlook.

## 🛠️ Built With

* **Python 3.13** - The core programming language.
* **PyQt6** - Used to create the Graphical User Interface (GUI).
* **Qt Designer** - Used to visually design the `interface.ui` file.
* **PyAutoGUI** - Used for keyboard simulation (Hotkeys, Tabbing, Typing).
* **OS & Webbrowser Modules** - Used for robust application launching.

## ⚙️ Prerequisites

Before running the application, ensure you have Python installed. You will need to install the following external libraries:

```bash
pip install pyautogui PyQt6
