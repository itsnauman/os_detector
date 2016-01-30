import os

name = ""

def hasImportOS():
    with open(name,"r") as f:
        for line in f:
            if "import os" in line:
                f.close()
                return True
        f.close()
        return False

def getInput():
    global name
    name = str(raw_input("Enter student LastFirst name: "))
    assign = str(raw_input("Enter assignment #: "))
    prob = str(raw_input("Enter problem #: "))
    name += ("_assign" + assign + "_problem" + prob + ".py")

def runProgram():
    if not hasImportOS():
        os.system("clear")
        os.system("python " + name)
    else:
        print hasImportOS()

def main():
    getInput()
    runProgram()

main()
