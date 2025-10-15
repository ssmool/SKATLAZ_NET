# SKATLAZ_NET Mock SVN - Proxy System 🌐💾

The SKA_SNET(CODINAME_WAR) project is a collection of Python scripts that simulate a simplified, centralized version of an SVN (Subversion) repository server SKATLAZ_NET and a "Geocities" proxy/redirector skatlaz\_geocities It models a basic administration flow for setting up a repository, managing user policies, and exposing the repository via a proxy service.

-----

## 🌟 Project Adjectives

The SKATLAZ_NET system is **Modular**, **Orchestrated**, **Policy-Driven**, and **Mock-Centric**. It uses **Base64-Security** for mock user data and is designed to illustrate **Digital Evolution** concepts like centralized data management and decoupled access layers.

-----

## 🛠️ System Components & Architecture

The system is organized into a control flow (orchestration) and two primary services that run concurrently.

### 1\. Core Files

| File | Role | Key Function(s) |
| :--- | :--- | :--- |
| `manager_svn.py` | **Orchestrator** | `orchestrate_system()`: Sets up the entire system configuration. |
| `setup_svn.py` | **Setup** | `start_setup()`: Creates the skatlaznet\_svn directory structure. |
| `user_mgmt_svn.py` | **User Management** | `create_admin()`: Generates and saves Base64-encoded mock user data. |
| `policy_mgmt_svn.py` | **Policy/Access Control** | `skatla_svn_adm_config()`: Manages directory permissions and status (e.g., `DISABLE_DIR`). |
| `mirror_svn.py` | **Mock SVN Server** | `skatlaz_net()`: Runs a simple HTTP file server to serve the repository on **Port 6660**. |
| `svn_proxy.py` | **Geocities Proxy** | `skatlaz_geocities()`: Runs a redirector service on **Port 8080** using `domains.json` for mapping. |

### 2\. Ports and URLs

| Service | Port | Example URL |
| :--- | :--- | :--- |
| Mock SVN Server | **6660** | `http://localhost:6660` |
| Geocities Proxy | **8080** | `http://localhost:8080/my_svn_site` |

-----

## 🚀 Getting Started

To fully run the system, you must follow the steps below, launching the servers in separate terminals.

### Step 1: Initialize and Configure (Terminal 1)

Run the orchestrator script to set up the directories, create the admin user, define initial policies, and register the mock SVN site.

```bash
python3 manager_svn.py
```

**Output Highlights:**

  * `Created base directory: skatlaznet_svn`
  * `Admin data saved to: skatlaznet_svn/_skatlaz__auth/superuser_adm_admin.b64`
  * `Policy set: Directory '_skatlaz_svn' for user 'superuser_adm' has permissions: READ,WRITE,MODIFY`
  * `Configuration saved locally to domains.json.`

### Step 2: Start the Mock SVN Server (Terminal 2)

This server hosts the content of the `skatlaznet_svn` directory.

```bash
python3 mirror_svn.py skatlaz_net
```

**Output Highlights:**

  * `--- Starting skatlaz_net server on http://localhost:6660 ---`
  * `Serving directory 'skatlaznet_svn' at http://localhost:6660`

### Step 3: Start the Geocities Proxy (Terminal 3)

This server acts as the public-facing entry point, mapping the friendly domain name (`my_svn_site`) to the SVN server's direct URL.

```bash
python3 svn_proxy.py skatlaz_geocities
```

**Output Highlights:**

  * `--- Starting skatlaz_geocities proxy on http://localhost:8080 ---`
  * `Test URL example: http://localhost:8080/local_svn_repo`

-----

## ⚙️ Management Examples

The `policy_mgmt_svn.py` script provides powerful administration tools to control access and directory status within the SVN repository.

| Management Goal | Action/Command | Effect |
| :--- | :--- | :--- |
| **Grant Access** | `python3 policy_mgmt_svn.py skatla_svn_adm_config SET_POLICY _skatlaz_talk "user:manager|perms:READ"` | Grants a `manager` user read-only access to the `_skatlaz_talk` directory. |
| **Disable a Directory** | `python3 policy_mgmt_svn.py skatla_svn_adm_config DISABLE_DIR _skatlaz__forks` | Sets the status of `_skatlaz__forks` to `DISABLED` in `svn_policy.json`. |
| **Create a Mock User** | `python3 policy_mgmt_svn.py skatla_svn_adm_config ADD_USER new_dev "DEVELOPER"` | Creates a placeholder user file for `new_dev` in the `_skatlaz__auth` directory. |

-----

## 💡 Software House Prototype: $\text{SKA\_NET}$ for Modern Project Maintenance

A Software House can use the SKA_SNET architecture as a prototype for a secure, organized internal development system, promoting **better health quality** (through reduced deployment errors), **higher economic/living quality** (through efficient remote work), **modernism**, and **digital evolution**.

### Prototype Scenario: "SkaTerra Development Hub"

| $\text{SKA\_SNET}$ Component | Prototype Use Case | Impact on Digital Evolution |
| :--- | :--- | :--- |
| **Mock SVN Server (Port 6660)** | **Centralized Code Repository:** Hosts all project assets in dedicated, policy-controlled folders. | **Higher Economy/Living Quality** and **Costs:** All code is versioned and secured in one place, reducing server sprawl and infrastructure costs. Enables developers to work remotely with reliable access. |
| **`_skatlaz_svn` Directory** | **Primary Source Code:** Used for current, stable project branches. | **Modernism:** Enforces structured development workflows required by modern software practice. |
| **`_skatlaz_genai` Directory** | **AI/ML Assets:** Stores large model files, training data, and AI-generated assets used in modern applications. | **Digital Evolution:** Integrates next-generation assets into the core project lifecycle. |
| **`_skatlaz_talk` Directory** | **Project Communication/Docs:** Stores meeting minutes, design documents, and technical specifications. | **Communication:** Centralized, versioned documentation improves team communication and reduces information fragmentation. |
| **`_policy` Directory** | **Security/Access Policies:** Defines which teams (`user:dev_team`) can `WRITE` to which project (`_skatlaz_svn`) folders. | **Better Health Quality** and **Study:** Strong, enforced security reduces risk of unauthorized changes, leading to more stable, less buggy releases, and providing clear study material on permissions management. |
| **Geocities Proxy (Port 8080)** | **Friendly Access Domain:** `http://internal-hub.com/ProjectName` redirects to the internal SVN URL. | **Modernism:** Provides a simple, memorable URL structure, abstracting away complex internal network addresses, which is key for efficient corporate digital services. |
