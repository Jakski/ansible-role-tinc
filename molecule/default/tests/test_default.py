import os

from pytest import fixture
import testinfra.utils.ansible_runner


ansible_runner = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE'])
instance_prefix = os.environ.get('MOLECULE_INSTANCE_PREFIX', 'instance')


@fixture
def instance1():
    return ansible_runner.get_host(instance_prefix + '1')


@fixture
def instance2():
    return ansible_runner.get_host(instance_prefix + '2')


def test_service(host):
    assert host.service('tinc@test1').is_running
    assert host.service('tinc@test2').is_running

    assert host.socket('tcp://0.0.0.0:655').is_listening
    assert host.socket('tcp://0.0.0.0:656').is_listening
    assert host.socket('udp://0.0.0.0:655').is_listening
    assert host.socket('udp://0.0.0.0:656').is_listening


def test_interfaces(host):
    iface = host.interface('test1')
    assert iface.exists
    assert len(iface.addresses) == 1
    iface = host.interface('test2')
    assert iface.exists
    assert len(iface.addresses) == 1


def test_instance1_connection(instance1):
    assert instance1.addr('10.0.0.2').is_reachable
    assert instance1.addr('10.0.0.4').is_reachable


def test_instance2_connection(instance2):
    assert instance2.addr('10.0.0.1').is_reachable
    assert instance2.addr('10.0.0.3').is_reachable
