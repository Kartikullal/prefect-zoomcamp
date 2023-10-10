from prefect.filesystems import GitHub

github_block = GitHub.load("git-zoom")


github_block.get_directory("flows") # specify a subfolder of repo
github_block.save("flows")
