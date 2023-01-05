import gitlab

token = 'YOUR_API_TOKEN'  # This is sensitive data!!
group_id = 62122681  # mhr-corp group id
gl = gitlab.Gitlab(private_token=token)
group = gl.groups.get(group_id)

print(group.name)