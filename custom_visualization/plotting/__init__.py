def get_projects_under_dbx_workspace(params="Some params"):
    """Get projects"""
    projects = ["project1","project2","project3"]
    return projects

def execute_project(path_to_project):
    """Executes a project given a path to the notebook"""
    pass


projects = get_projects_under_dbx_workspace()

for project in projects:
    execute_project(project)
