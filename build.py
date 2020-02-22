import os
from sys import *
from string import Template

SRC_DIR_POS = 1
INDEX_PATH = "index.html"

preFileBufffer = []
postFileBufffer = []
targetLineNo = -1
indentLevel = 0
contents = []

def validDir(dest):
    if os.path.isdir(dest):
        targetFiles = os.listdir(dest)
        if len(targetFiles):
            return targetFiles

    return None

def fileContainsID(id):
    file = open(INDEX_PATH, "r")

    for line in file.readlines():
        if line.__contains__("id=\""+id+"\""):
            file.close()
            return True

    file.close()
    return False

def readIndexFile(id):
    global preFileBufffer
    global postFileBufffer
    global targetLineNo
    file = open(INDEX_PATH, "r")
    pre = True
    restartTag = None

    fileBuffer = file.readlines()

    for line in fileBuffer:
        if pre:
            preFileBufffer.append(line)
        else:
            if not restartTag == None and line.__contains__(restartTag):
                restartTag = None
                postFileBufffer.append(line)
            elif restartTag == None:
                postFileBufffer.append(line)

        if line.__contains__("id=\"" + id + "\""):
            pre = False
            targetLineNo = fileBuffer.index(line)
            restartTag = line.split(" ")[0].strip().split("<")[1]
            restartTag = "</"+restartTag+">"

    file.close()

def indentAmount(line):
    global indentLevel
    for i in range(len(preFileBufffer)):
        if i == line:
            for c in preFileBufffer[i]:
                if str.isspace(c):
                    indentLevel += 1
                else:
                    break

    indentLevel += 1

def heading(name):
    container = Template("<span class=\"inline-link\">${heading}<a href=${link} target=\"blank\">View</a></span>")
    heading = "<h1>{0}</h1>".format(name);
    link = "https://github.com/cvr-skidz/" + str(name).replace(" ", "-")
    return container.substitute(heading=heading, link=link)

def insert(path, files):
    os.chdir(path)
    for i in files:
        contents.append(heading(i) + "\n")
        currProject = open(i, "r")
        contents.append("<p>" + currProject.read()+"</p>\n")
        currProject.close()
    os.chdir("../")

def write():
    global preFileBufffer
    global postFileBufffer
    global indentLevel
    global contents
    global INDEX_PATH

    file = open(INDEX_PATH, "w")

    for i in preFileBufffer:
        file.write(i)

    for i in contents:
        newLine = True
        buffer = [];
        for c in i:
            if newLine:
                buffer.append("\t" * indentLevel)
                newLine = False
            buffer.append(c)
            if c == '\n':
                newLine = True

        file.write("".join(buffer))
    file.write("\n")

    for i in postFileBufffer:
        file.write(i)

    file.close()

def printPreview():
    global preFileBufffer
    global postFileBufffer
    global indentLevel
    global contents

    for i in preFileBufffer:
        print(i, end="")

    for i in contents:
        newLine = True
        buffer = [];
        for c in i:
            if newLine:
                buffer.append("\t" * indentLevel)
                newLine = False
            buffer.append(c)
            if c == '\n':
                newLine = True

        print("".join(buffer), end="")
    print("")

    for i in postFileBufffer:
        print(i, end="")

def clearBuffers():
    global preFileBufffer
    global postFileBufffer
    global contents
    global indentLevel

    preFileBufffer = []
    postFileBufffer = []
    contents = []
    indentLevel = 0


if __name__ == "__main__":
    argv.remove(argv[0])

    if not os.path.isfile(INDEX_PATH):
        print("Can not find index.html in current working directory.")

    for src in argv:
        targetFiles = validDir(src)

        if targetFiles == None:
            print("Supplied build source directory is invalid.")
        else:
            if not fileContainsID(src):
                print("Can not find supplied id in " + INDEX_PATH)
            else:
                readIndexFile(src)
                indentAmount(targetLineNo)
                insert(src, targetFiles)

                write()
                clearBuffers()