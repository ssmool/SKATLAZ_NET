# policy_mgmt.py

import json
import os

POLICY_DIR = os.path.join("skatlaznet_svn", "_policy")
AUTH_DIR = os.path.join("skatlaznet_svn", "_skatlaz__auth")
POLICY_FILE = os.path.join(POLICY_DIR, "svn_policy.json")

def _load_policies():
    """Helper to load the current policy file."""
    if not os.path.exists(POLICY_FILE):
        return {}
    with open(POLICY_FILE, 'r') as f:
        return json.load(f)

def _save_policies(policies):
    """Helper to save the current policy file."""
    os.makedirs(POLICY_DIR, exist_ok=True)
    with open(POLICY_FILE, 'w') as f:
        json.dump(policies, f, indent=4)
    print(f"Policies updated in {POLICY_FILE}.")

def skatla_svn_adm_config(action, target, value=None):
    """
    Admin function to manage policies, users, and groups.
    Actions: SET_POLICY, ADD_USER, CHANGE_PASS (mock).
    Target: The directory, user, or group.
    Value: The permission level or new password/role.
    """
    policies = _load_policies()
    
    print(f"\n--- Admin Action: {action} on {target} (Value: {value}) ---")

    if action == "SET_POLICY":
        # Example policy structure: {"_skatlaz_svn": {"admin": "READ,WRITE", "guest": "READ"}}
        
        # Parse value: e.g., "user:admin|perms:READ,WRITE"
        try:
            user_part, perms_part = value.split('|')
            user = user_part.split(':')[-1]
            perms = perms_part.split(':')[-1]
        except Exception:
            print("Error: SET_POLICY value format must be 'user:NAME|perms:PERMISSIONS'.")
            return

        policies.setdefault(target, {})[user] = perms
        _save_policies(policies)
        print(f"Policy set: Directory '{target}' for user '{user}' has permissions: {perms}")
        
    elif action == "ADD_USER":
        # MOCK: In a real system, this would call create_admin or similar
        print(f"MOCK: Creating user file for {target} with role {value} in {AUTH_DIR}.")
        # Create a placeholder user file (e.g., in a real system this would be more complex)
        mock_user_data = {"username": target, "role": value}
        with open(os.path.join(AUTH_DIR, f"{target}.json"), 'w') as f:
            json.dump(mock_user_data, f, indent=4)

    elif action == "CHANGE_PASS":
        # MOCK: Would securely update the user's password hash in the _skatlaz__auth files
        print(f"MOCK: Password for user '{target}' changed.")
        
    elif action == "DISABLE_DIR":
        policies.setdefault('dir_status', {})[target] = 'DISABLED'
        _save_policies(policies)
        print(f"Directory '{target}' is now DISABLED.")
        
    else:
        print(f"Unknown admin action: {action}")

if __name__ == '__main__':
    # Example usage:
    # skatla_svn_adm_config("SET_POLICY", "_skatlaz_svn", "user:admin|perms:READ,WRITE,MODIFY")
    # skatla_svn_adm_config("ADD_USER", "guest_user", "GUEST")
    # skatla_svn_adm_config("DISABLE_DIR", "_skatlaz__forks")
    pass
