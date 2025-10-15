# orchestrator.py

import setup
import user_mgmt
import server_and_push
import geocities_proxy
import policy_mgmt
import time
import subprocess
import sys

def orchestrate_system():
    """
    Runs the system in sequence or in parallel processes.
    """
    print("=========================================")
    print("      SVN/Proxy System Orchestrator      ")
    print("=========================================")

    # --- Part 1: Setup and Initialization ---
    print("\n--- 1. SYSTEM SETUP (Script 1) ---")
    setup.start_setup()
    
    print("\n--- 2. ADMIN CREATION (Script 2) ---")
    admin_data = user_mgmt.create_admin(username="superuser_adm")
    
    print("\n--- 3. POLICY CONFIGURATION (Script 6) ---")
    policy_mgmt.skatla_svn_adm_config("SET_POLICY", "_skatlaz_svn", f"user:{admin_data['username']}|perms:READ,WRITE,MODIFY")
    policy_mgmt.skatla_svn_adm_config("DISABLE_DIR", "_skatlaz__postmail")

    # --- Part 2: Networking Configuration ---
    print("\n--- 4. SVN REPO REGISTRATION (Script 4) ---")
    server_and_push.skatlaz_geocities_push(
        named_domain="my_svn_site", 
        user=admin_data['username'], 
        password="mock_password", 
        local_token=admin_data['guid'][:8]
    )

    # --- Part 3: Running Servers (Requires separate terminal/threading in reality) ---
    print("\n--- 5. STARTING SERVERS (Scripts 3 & 5) ---")
    
    # NOTE: Running both servers in the same script requires threading or
    # multiprocessing, which is complex for a simple example.
    # The following shows the *command* to run them separately.
    
    print("\n--- TO RUN THE SYSTEM, YOU MUST EXECUTE THESE IN SEPARATE TERMINALS: ---\n")
    print(f"1. Start the SVN Server (Script 3):")
    print(f"   python3 server_and_push.py skatlaz_net")
    print(f"   (Access at: http://{server_and_push.HOST_NAME}:{server_and_push.PORT})")
    
    print("\n2. Start the Geocities Proxy (Script 5):")
    print(f"   python3 geocities_proxy.py skatlaz_geocities")
    print(f"   (Access at: http://{geocities_proxy.PROXY_HOST}:{geocities_proxy.PROXY_PORT}/my_svn_site)")
    
    print("\n=========================================")
    print("Orchestration script finished execution.")
    print("=========================================")

if __name__ == '__main__':
    # This block allows running specific functions from the command line
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "setup":
            setup.start_setup()
        elif command == "create_admin":
            user_mgmt.create_admin()
        elif command == "push":
            server_and_push.skatlaz_geocities_push()
        elif command == "net":
