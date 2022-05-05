import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_alagent_bin(host):
    assert host.file("/var/alertlogic").is_directory
    assert host.file("/var/alertlogic/lib/agent/bin/al-agent").is_file
    assert host.file("/var/alertlogic/lib/agent/bin/al-agent").mode == 0o755
