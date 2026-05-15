roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}

is_editor = 'editor' in roles.values()
is_manager = 'manager' in roles.values()

print(f"Editor: {is_editor}")
print(f"IS Manager: {is_manager}")