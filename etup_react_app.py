import os
import subprocess

def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Command failed with error: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))

# Step 1: Create React app
def create_react_app(app_name):
    run_command(f"npx create-react-app {app_name}")

# Step 2: Set up Git repository
def setup_git_repo(repo_path):
    commands = [
        "git init",
        "git add .",
        "git commit -m 'Initial commit'",
        "git remote add origin <your-github-repo-url>",
        "git push -u origin master"
    ]
    for command in commands:
        run_command(command, cwd=repo_path)

# Step 3: Install dependencies
def install_dependencies(app_directory):
    run_command("npm install", cwd=app_directory)

# Step 4: Start the React app
def start_react_app(app_directory):
    run_command("npm start", cwd=app_directory)

# Main process
if __name__ == "__main__":
    app_name = "my-app"
    my_app_dir = os.path.join(os.getcwd(), app_name)
    if not os.path.exists(my_app_dir):
        print('Calling create react app')
        # Create React app
        create_react_app(app_name)
        print('React app created')
        
        # Ensure .gitignore file is in place
        with open(os.path.join(my_app_dir, ".gitignore"), "w") as f:
            f.write("node_modules/\nbuild/\n")
        
        print('Setting up Git repository')
        # Set up the Git repository
        setup_git_repo(my_app_dir)
        print('Git repository setup completed')
        
        print('Installing dependencies')
        # Install dependencies
        install_dependencies(my_app_dir)
        print('Dependencies installed')

    print('Starting the React app')
    # Start the React app
    start_react_app(my_app_dir)
    print('Program has ended')
