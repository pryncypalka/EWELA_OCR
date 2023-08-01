def create_settings_file():
    default_settings = """lang=pol
first_key=print_screen
second_key=None
"""
    with open("settings.txt", "w") as file:
        file.write(default_settings)

def read_settings():
    settings = {}
    try:
        with open("settings.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                settings[key] = value
    except FileNotFoundError:
        create_settings_file()
        settings = {
            "lang": "pol",
            "first_key": "print_screen",
            "second_key": "None"
        }
    return settings

def change_settings(key, value):
    settings = read_settings()
    settings[key] = value
    with open("settings.txt", "w") as file:
        for key, value in settings.items():
            file.write(f"{key}={value}\n")
