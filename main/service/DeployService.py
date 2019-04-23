from Base import Base
from main.model.Deploy import deploys
from main.service.ProjectService import projectService
from main.service.HostService import hostService
from main.service.ProjectHostService import projectHostService
from main.utils.git import Git

class DeployService(Base):
    __model__ = deploys
    def deploy(self,form):
        dest = "/home/aaa/"
        target = "/target"
        project = projectService.get(form.project_id)
        git  = Git(project.name,project.repo_url)
        # clone
        git.clone()
        # checkout
        git.checkout_branch(form.branch,form.commit)
        # deploy
        git.package(form.branch)
        hosts = projectHostService.first(project_id=form.project_id)
        host = hostService.get(hosts.host_id)
        cmd = ("rsync -vzq "
               "--rsh=\"sshpass -p {ssh_pass} ssh -p {ssh_port}\" "
               "--include='.jar' {local_dest}/ {ssh_user}@{ssh_host}:"
               "{remote_dest}/")
        cmd = cmd.format(ssh_pass=host.ssh_password,
                   ssh_port=22,
                   local_dest=git.location+project.name+target,
                   ssh_user=host.ssh_username,
                   ssh_host=host.host_ip,
                   remote_dest=dest+project.name)
        print(cmd)
        # rsync
        # rsync -avzq --rsh="sshpass -p itcast ssh -p 22"
        # /home/dongmengyuan/deployProjects/SpringBootTest/target/demo-0.0.1-SNAPSHOT.jar
        # itcast@172.20.10.2:/home/itcast/Desktop/deployProjects/
        pass
deployService = DeployService()