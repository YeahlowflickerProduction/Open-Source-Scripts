from os.path import exists, expanduser


def _name():
    name = raw_input("Enter application name: ")
    if len(name) > 0:
        return name
    else:
        print("ERROR: Name cannot be empty.")
        _name()



def _version():
    return raw_input("Enter application version (Skip by entering nothing): ")



def _exec():
    path = raw_input("Enter executable path (full path): ")
    if exists(path):
        return path
    else:
        print("ERROR: Path is invalid.")
        return _exec()


def _icon():
    return raw_input("Enter icon path (full path) (Skip by entering nothing): ")



#   Main Program
if __name__ == "__main__":

    print("Yeahlowflicker Production")
    print("SCPT000 - Linux Desktop Entry Generator")
    raw_input("Press any key to start...")


    name = _name()
    version = _version()
    exec_path = _exec()
    icon = _icon()


    print("Saving...")

    dirpath = expanduser("~") + "/.local/share/applications/{}.desktop".format(name.replace(" ", "-"))

    #   Save file
    with open(dirpath, 'a') as file:
        file.write("[Desktop Entry]\n")
        file.write("Type=Application\n")
        file.write("Name={}\n".format(name))
        file.write("Version={}\n".format(version))
        file.write("Exec={}\n".format(exec_path))
        file.write("Icon={}\n".format(icon))

    print("File saved successfully at {}.".format(dirpath))
    raw_input("Press any key to exit...")

