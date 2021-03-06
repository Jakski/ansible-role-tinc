ansible-role-tinc
*****************

Role to setup tinc.

Warning:

  Although this role supports multiple instances of tinc running on
  single node, it doesn't handle tinc upgrades well. Package upgrade
  event is emitted only once, so if you apply this role multiple times
  on single node in different plays, than only first play will
  actually trigger restart. It's good to perform manual restart after
  upgrade, if you own complicated setup.


Variables
=========

tinc_packages

   Packages with tinc and related tools

tinc_host_name

   Host identifier in network

tinc_service

   systemd service template

tinc_default_release

   Default packages release

tinc_state

   Desired service state

tinc_enabled

   Whether to enable system service

tinc_restart

   Whether to restart when necessary

tinc_reload

   Whether to reload when necessary

tinc_conf_dir

   Configuration directory

tinc_key_bits

   Generated keys length

tinc_network_name

   Network name

tinc_group

   Inventory group with network nodes

tinc_main_conf

   Main configuration

tinc_host_conf

   Host configuration. It will be propagated to all nodes in network.

tinc_private_key

   Private key. Must be used together with public key.

tinc_public_key

   Public key. Must be used together with private key.

tinc_scripts

   Hooks

tinc_manage_hosts

   Whether to remove host configurations non-existent in group

tinc_hosts_whitelist

   Don't manage this hosts. It let's you authorize external hosts,
   managing the rest at the same time.


Examples
========

   ---
   - hosts: all
     tasks:
       - import_role:
           name: tinc
         vars:
           tinc_network_name: "test1"
           tinc_group: "{{ test_networks.test1.group }}"
           tinc_main_conf: "{{ test_networks.test1.main_conf }}"
           tinc_host_conf: "{{ test_networks.test1.host_conf }}"
           tinc_scripts: "{{ test_networks.test1.scripts }}"

       - import_role:
           name: tinc
         vars:
           tinc_network_name: "test2"
           tinc_group: "{{ test_networks.test2.group }}"
           tinc_main_conf: "{{ test_networks.test2.main_conf }}"
           tinc_host_conf: "{{ test_networks.test2.host_conf }}"
           tinc_scripts: "{{ test_networks.test2.scripts }}"


Documentation
=============

Compile:

   $ pip3 install -r requirements.txt
   $ make man

View:

   $ man ./docs/man/ansible-role-tinc.1
