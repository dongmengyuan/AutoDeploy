from main import db
from main.utils.jsonencoder import JsonSerializer
class hosts(JsonSerializer,db.Model):
    id = db.Column(db.BIGINT,primary_key=True)
    host_ip = db.Column(db.VARCHAR)
    ssh_username = db.Column(db.VARCHAR)
    ssh_password = db.Column(db.VARCHAR)
    ssh_port = db.Column(db.Integer)
    host_name = db.Column(db.VARCHAR)

    def __str__(self):
        return "host host_id is %s,host_ip: %s, ssh_username: %s,ssh_password : %s,ssh_port: %s,host_name: %s" % (self.id, self.host_ip,self.ssh_username,self.ssh_password,self.ssh_port,self.host_name)