from importlib import resources
with resources.path("assets", "AddIcon.ico") as path:
    print(path)