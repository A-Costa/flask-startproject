#!/usr/bin/python
import sys, os

if len(sys.argv) != 2:
    print "usage: {} <name>".format(sys.argv[0])
    sys.exit(1)
else:
    projectName = os.path.abspath(sys.argv[1])
    if not os.path.exists(os.path.dirname(projectName)):
        print 'folder: "{}" doesn\'t exist. aborting...'.format(os.path.dirname(projectName))
        sys.exit(1)
    if os.path.exists(projectName):
        print 'File or folder with name "{}" already exists. aborting...'.format(projectName)
        sys.exit(1)
    else:
        os.mkdir(projectName)
        appFolder = os.path.join(projectName, os.path.basename(projectName))
        templatesFolder = os.path.join(appFolder, "templates")
        staticFolder = os.path.join(appFolder, "static")
        instanceFolder = os.path.join(appFolder, "instance")

        os.mkdir(appFolder)
        os.mkdir(templatesFolder)
        os.mkdir(staticFolder)
        os.mkdir(instanceFolder)
