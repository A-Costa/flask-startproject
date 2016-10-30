#!/usr/bin/python
import sys, os

if len(sys.argv) != 2:
    print "usage: {} <name>".format(sys.argv[0])
    sys.exit(1)
else:
    projectPath = os.path.abspath(sys.argv[1])
    appName = os.path.basename(projectPath)
    if not os.path.exists(os.path.dirname(projectPath)):
        print 'folder: "{}" doesn\'t exist. aborting...'.format(os.path.dirname(projectPath))
        sys.exit(1)
    if os.path.exists(projectPath):
        print 'File or folder with name "{}" already exists. aborting...'.format(projectPath)
        sys.exit(1)
    else:
        os.mkdir(projectPath)
        appFolder = os.path.join(projectPath, appName)
        templatesFolder = os.path.join(appFolder, "templates")
        staticFolder = os.path.join(appFolder, "static")
        instanceFolder = os.path.join(appFolder, "instance")

        os.mkdir(appFolder)
        os.mkdir(templatesFolder)
        os.mkdir(staticFolder)
        os.mkdir(instanceFolder)

        initFilePath = os.path.join(appFolder, "__init__.py")
        initFile = open(initFilePath, "w+")
        initFile.write("from flask import Flask\n")
        initFile.write("app = Flask(__name__)\n\n")
        initFile.write("from {} import views".format(appName))
        initFile.close()

        viewsFilePath = os.path.join(appFolder, "views.py")
        viewsFile = open(viewsFilePath, "w+")
        viewsFile.write("from {} import app\n\n".format(appName))
        viewsFile.write("@app.route('/')\n")
        viewsFile.write("def index():\n")
        viewsFile.write("    return 'Hello World'\n")
        viewsFile.close()

        runFilePath = os.path.join(projectPath, "run.py")
        runFile = open(runFilePath, "w+")
        runFile.write("#!/usr/bin/python\n")
        runFile.write("from {} import app\n\n".format(appName))
        runFile.write("app.run(debug=True, host='0.0.0.0')")
        runFile.close()
