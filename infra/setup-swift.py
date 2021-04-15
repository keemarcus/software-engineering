from server import Server

def install_apt_packages(server):
    server.update_apt_packages()
    server.install_apt_package("python3-pip")

def install_pip_packages(server):
    version = server.get_pip3_version()
    assert version.startswith("20.")
    server.install_pip3_package("bottle")
    server.install_pip3_package("dataset")
    packages = server.get_installed_pip3_packages()
    assert "bottle" in packages
    assert "dataset" in packages

def install_application_source(server):
    # make sure we have a project directory
    _, stderr = server.run("mkdir -p ~/projects")

    # make sure the code isn't there already
    server.run("rm -rf ~/projects/swift")

    # make sure we have a version of git
    version = server.get_git_version()
    assert version.startswith("2.")

    # get the source by cloning the repo
    server.run("cd ~/projects; git clone --depth 1 https://github.com/keemarcus/swift.git")

    # verify the code is there
    stdout, _ = server.run("ls ~/projects/swift")
    assert "swift.py" in stdout

def start_application(server):
    server.run("cd ~/projects/swift; screen -S webapp -dm python3 swift.py")

if __name__ == "__main__":

    server = Server(host="3.235.134.202", user="ubuntu", key_filename="C:/Users/keema/Downloads/LightsailDefaultKey-us-east-1.pem")

    install_apt_packages(server)
    install_pip_packages(server)
    install_application_source(server)
    start_application(server)

    print("done.")

