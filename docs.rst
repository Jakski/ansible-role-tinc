ansible-role-tinc
================================================================================

Role to setup tinc.

.. warning::

   Although this role supports multiple instances of tinc running on single
   node, it doesn't handle tinc upgrades well. Package upgrade event is emitted
   only once, so if you apply this role multiple times on single node in
   different plays, than only first play will actually trigger restart. It's
   good to perform manual restart after upgrade, if you own complicated setup.

Variables
--------------------------------------------------------------------------------

.. autoyaml:: defaults/main.yml

Examples
--------------------------------------------------------------------------------

.. literalinclude:: molecule/default/playbook.yml
   :language: yaml

Documentation
--------------------------------------------------------------------------------

Compile::

   $ pip3 install -r requirements.txt
   $ make man

View::

   $ man ./docs/man/ansible-role-tinc.1
