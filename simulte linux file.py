class File:
    def __init__(self, name, owner, group, permissions):
        """
        permissions: string of 9 characters like 'rwxr-xr--'
        owner: owner username
        group: group name
        """
        self.name = name
        self.owner = owner
        self.group = group
        self.permissions = permissions

    def check_permission(self, user, action):
        """
        user: dictionary { 'name': str, 'groups': list }
        action: 'read', 'write', 'execute'
        """
        # Map action to index in permissions
        perm_index = {'read': 0, 'write': 1, 'execute': 2}

        if user['name'] == self.owner:
            start = 0  # Owner permissions
        elif self.group in user['groups']:
            start = 3  # Group permissions
        else:
            start = 6  # Others permissions

        allowed = self.permissions[start + perm_index[action]] != '-'
        return allowed

    def __str__(self):
        return f"{self.permissions} {self.owner}:{self.group} {self.name}"


# Example usage
if __name__ == "__main__":
    # Users
    alice = {'name': 'alice', 'groups': ['staff']}
    bob = {'name': 'bob', 'groups': ['staff']}
    charlie = {'name': 'charlie', 'groups': ['users']}

    # Files
    file1 = File("file1.txt", owner="alice", group="staff", permissions="rw-r-----")
    file2 = File("script.sh", owner="bob", group="users", permissions="rwxr-xr-x")

    files = [file1, file2]

    # Display files
    print("Files on system:")
    for f in files:
        print(f)

    # Attempt actions
    actions = ['read', 'write', 'execute']
    users = [alice, bob, charlie]

    print("\nPermission Check:")
    for user in users:
        for f in files:
            for action in actions:
                result = f.check_permission(user, action)
                print(f"User '{user['name']}' trying to {action} '{f.name}': {'Allowed' if result else 'Denied'}")
