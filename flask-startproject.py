#!/usr/bin/python
import sys, os, stat

if len(sys.argv) != 2:
    print "usage: {} <name>".format(sys.argv[0])
    sys.exit(1)
else:
    projectPath = os.path.abspath(sys.argv[1])
    appName = os.path.basename(projectPath)
    #check if given path is ok
    if not os.path.exists(os.path.dirname(projectPath)):
        print 'folder: "{}" doesn\'t exist. aborting...'.format(os.path.dirname(projectPath))
        sys.exit(1)
    if os.path.exists(projectPath):
        print 'File or folder with name "{}" already exists. aborting...'.format(projectPath)
        sys.exit(1)
    if os.system('virtualenv --version')!= 0:
        print 'Dependency Error: virtualenv not installed. aborting...'
        sys.exit(1)
    else:
        #create the main folder for the project
        os.mkdir(projectPath)

        #set the names for all other folders needed
        appFolder = os.path.join(projectPath, appName)
        templatesFolder = os.path.join(appFolder, "templates")
        staticFolder = os.path.join(appFolder, "static")
        instanceFolder = os.path.join(appFolder, "instance")

        #create all other folders
        os.mkdir(appFolder)
        os.mkdir(templatesFolder)
        os.mkdir(staticFolder)
        os.mkdir(instanceFolder)

        #create virtualenv
        virtualenvpath = os.path.join(projectPath, "venv")
        os.system('virtualenv ' + virtualenvpath)
        virtualpythonenv = os.path.join(virtualenvpath, "bin/python")
        os.system(virtualpythonenv + ' -c "import pip; pip.main([\'install\', \'flask\'])"')

        #create file __init__.py
        initFilePath = os.path.join(appFolder, "__init__.py")
        initFile = open(initFilePath, "w+")
        initFile.write("from flask import Flask\n")
        initFile.write("app = Flask(__name__)\n\n")
        initFile.write("from {} import views".format(appName))
        initFile.close()

        #create file views.py
        viewsFilePath = os.path.join(appFolder, "views.py")
        viewsFile = open(viewsFilePath, "w+")
        viewsFile.write("from {} import app\n\n".format(appName))
        viewsFile.write("@app.route('/')\n")
        viewsFile.write("def index():\n")
        viewsFile.write("    return 'Hello World'\n")
        viewsFile.close()

        #create file run.py
        runFilePath = os.path.join(projectPath, "run.py")
        runFile = open(runFilePath, "w+")
        runFile.write("#!venv/bin/python\n")
        runFile.write("from {} import app\n\n".format(appName))
        runFile.write("app.run(debug=True, host='0.0.0.0')")
        runFile.close()
        os.chmod(runFilePath, 0775)
