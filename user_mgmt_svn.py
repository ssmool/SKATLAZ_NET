# user_mgmt.py

import uuid
import base64
import os

def create_admin(username="admin"):
    """
    Generates admin user data (mock GUID, password, biometrics, voice) 
    and saves it as a Base64-encoded file.
    """
    print(f"--- Generating Admin User: {username} ---")

    # 1. Generate core data
    admin_guid = str(uuid.uuid4())
    admin_password = base64.b64encode(os.urandom(16)).decode('utf-8')[:16] # Mock secure password
    
    # 2. Mock Biometric/Voice Data (representing binary blobs)
    # 1KB mock biometric picture data
    mock_picture_blob = os.urandom(1024) 
    # 30-second mock voice sample (assuming 16-bit mono @ 8kHz -> 8000 * 2 * 30 bytes)
    mock_voice_blob = os.urandom(480000) 

    # 3. Create a dictionary of user data
    user_data = {
        "username": username,
        "guid": admin_guid,
        "password_hash": base64.b64encode(admin_password.encode()).decode(), # Hash/store securely in real life
        "biometric_picture_b64": base64.b64encode(mock_picture_blob).decode('utf-8'),
        "voice_sample_b64": base64.b64encode(mock_voice_blob).decode('utf-8')
    }

    # 4. Convert the user data dictionary to a single Base64-encoded string
    import json
    json_data = json.dumps(user_data)
    base64_file_content = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    
    # 5. Save the Base64 content to a file
    auth_dir = os.path.join("skatlaznet_svn", "_skatlaz__auth")
    os.makedirs(auth_dir, exist_ok=True) # Ensure auth dir exists
    
    file_path = os.path.join(auth_dir, f"{username}_admin.b64")
    with open(file_path, "w") as f:
        f.write(base64_file_content)

    print(f"Admin data saved to: {file_path}")
    print(f"GUID: {admin_guid}")
    print(f"Password (Mock): {admin_password}")
    print("--- Admin Creation Complete ---")
    
    return user_data

if __name__ == '__main__':
    # Execute admin creation
    create_admin()
