import gitlab

token = 'glpat-SXyvLbG39bct_FdBpbD_'  # This is sensitive data!!
project_id = 42318536
gl = gitlab.Gitlab(private_token=token)
project = gl.projects.get(project_id)

print(project.name)