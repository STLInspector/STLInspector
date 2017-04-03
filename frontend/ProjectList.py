import re
import os
import json
from .Project import Project

# maintains the project list and all open projects
class ProjectList:
    # filepath should point to the dir
    # where files are saved and loaded
    def __init__(self, filepath):
        self.openProjects = {}
        self.filepath = filepath
        self.suffix = '.stlinspector'

    # returns a list containing dicts with
    # id, title, and coverage of available projects
    def list(self):
        lst = []

        for p in self.openProjects:
            lst.append(self.openProjects[p].overview())

        # load files from filepath
        for f in os.listdir(self.filepath):
            file = os.path.join(self.filepath, f)
            if not os.path.isfile(file):
                continue

            # only file-extension .stlinspector allowed
            suffixLen = len(self.suffix)
            if f[-suffixLen:] != self.suffix:
                continue

            # check if id already loaded
            id = f[:-suffixLen]
            if id in self.openProjects:
                continue

            try:
                p = self.loadProject(id, file)
                lst.append(p.overview())
            except:
                lst.append({
                    'id': id,
                    'title': id,
                    'error': 'load error'
                })

        return lst

    # deletes the project with the given id (string)
    def delete(self, id):
        # close project if opened
        self.close(id)

        # delete file if it exists
        file = os.path.join(self.filepath, id+self.suffix)
        if not os.path.isfile(file):
            return

        os.remove(file)

    # loads a file into a project
    def loadProject(self, id, filename):
        with open(filename) as fp:
            p = Project(id, data=json.load(fp))
            fp.close()
            return p

    # saves the project with id
    def saveProject(self, id):
        p = self.project(id)
        with open(os.path.join(self.filepath, id+self.suffix), 'w') as fp:
            json.dump(p.save(), fp, indent=2)
            fp.close()

    # creates a project with the given title
    # returns the same object as list() elements
    def create(self, title):
        id = re.sub(r'\W', '_', title)
        project = Project(id)
        project.setTitle(title)
        self.openProjects[id] = project
        return project.overview()

    # closes a project
    def close(self, id):
        if id in self.openProjects:
            del self.openProjects[id]

    # returns the project to the given id
    # loads it if not already loaded
    # throws an exception if project cannot be found
    def project(self, id):
        if id in self.openProjects:
            return self.openProjects[id]

        file = os.path.join(self.filepath, id+self.suffix)
        if not os.path.isfile(file):
            raise Exception('Project not found')

        p = self.loadProject(id, file)
        self.openProjects[id] = p
        return p
