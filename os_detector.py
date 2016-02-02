import os

def has_import_os(name):
    with open(name, "r") as fp:
        for line in fp:
            if "import os" in line:
                return True
        return False

def run_program():
    name = raw_input("Enter student LastFirst name: ")
    assign = raw_input("Enter assignment #: ")
    prob = raw_input("Enter problem #: ")
    name += ("_assign" + assign + "_problem" + prob + ".py")

    if not has_import_os(name):
        os.system("clear")
        os.system("python " + name)
    else:
        print has_import_os(name)


if __name__ == '__main__':
    run_program()
