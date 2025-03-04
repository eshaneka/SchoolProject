def get_projects():
    projects = []
    for i in range(10):
        project = {}
        project["name"] = f"Project {i+1}"
        project["description"] = "This is a random project."
        project["status"] = "in progress"
        projects.append(project)
    return projects
