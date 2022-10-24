import json
import time
import pyautogui

with open('config.json', "r") as configfile:
    config = json.load(configfile)

with open(config["projects_filename"], "r") as project_keys:
    project_list = [p.replace("\n", "").strip() for p in project_keys.readlines()]


def press(key):
    pyautogui.press(key)


def hotkey(key1, key2):
    pyautogui.hotkey(key1, key2, interval=0.10)


def write(text, interval=0.00):
    pyautogui.write(text, interval=interval)


def select_projects(destination_url, list_of_projects):
    time.sleep(config["seconds_to_start"])
    for project in list_of_projects:
        hotkey("ctrl", "f")
        write(destination_url)
        press("esc")
        hotkey("alt", "enter")
        press("tab")
        write(project)

        for _ in range(12):
            time.sleep(0.01)
            press("tab")

        press("space")

    hotkey("ctrl", "f")
    write(destination_url)
    press("esc")
    hotkey("alt", "enter")
    press("tab")
    press("backspace")


select_projects(config["cloud_destination_url"], project_list)
