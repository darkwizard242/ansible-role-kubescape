import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/kubescape'


def test_kubescape_binary_exists(host):
    """
    Tests if kubescape binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_kubescape_binary_file(host):
    """
    Tests if kubescape binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_kubescape_binary_which(host):
    """
    Tests the output to confirm kubescape's binary location.
    """
    assert host.check_output('which kubescape') == PACKAGE_BINARY
