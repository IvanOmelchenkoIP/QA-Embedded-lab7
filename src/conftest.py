import paramiko
import subprocess
import pytest

server_ip = '192.168.56.1'
password = 'i252002'
username = 'ivanvm1'

decode_format = 'UTF-8'


@pytest.fixture(scope="function")
def server():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=server_ip, username=username, password=password) 
        client.exec_command("iperf3 -s")
        return None
    except Exception as error_serv:
        return error_serv
    finally:
        client.close()


@pytest.fixture(scope="function")
def client(server):
    error_serv = server
    if error_serv:
        return (None, None, error_serv)
    p = subprocess.Popen(
            ["iperf3", "-c", server_ip, "-i", "1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    stdout, stderr = p.communicate()
    return (stdout.decode(decode_format), stderr.decode(decode_format), error_serv)
