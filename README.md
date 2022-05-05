# Ansible Role: alagent

[![Molecule](https://github.com/deekayen/al-agents-ansible-playbooks/actions/workflows/ci.yml/badge.svg)](https://github.com/deekayen/al-agents-ansible-playbooks/actions/workflows/ci.yml) [![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)

This playbook is used to install and configure the Alert Logic agent.

Forked from the abandoned project originally sponsored by Alert Logic at https://github.com/alertlogic/al-agents-ansible-playbooks to have a workaround for https://github.com/alertlogic/al-agents-ansible-playbooks/issues/32 where GPG checks for RPMs caused installations to fail.

## Requirements

The following platforms are supported.

Debian versions:

* buster
* bullseye

Ubuntu versions:

* 22.04
* 20.04

RHEL/CentOS versions:

* 7.x
* 8.x

Amazon Linux versions:

* Karoo

Windows versions:

* Windows Server 2016, 2019

## Role Variables

* `al_agent_registration_key` - your unique registration key, required except in supported cloud deployments (AWS, Azure) String defaults to `your_registration_key_here`
* `al_agent_for_imaging` - The `al_agent_for_imaging` variable determines if the agent will be configured and provisioned.  If  set to `true` then the install process performs an installation of the agent but will not start the agent once installation is completed.  This allows for instance snapshots to be saved and started for later use.  With this variables set to `false` then the provisioning process is performed during setup and the agent is started once complete.  Boolean defaults to `false`
* `al_agent_egress_host`,`al_agent_egress_port` - By default all traffic is sent to <https://vaporator.alertlogic.com.>  This variable is useful if you have a machine that is responsible for outbound traffic (NAT box).  If you specify your own URL ensure that it is a properly formatted URI.  String defaults to `https://vaporator.alertlogic.com`
* `al_agent_proxy_url` - By default al-agent does not require the use of a proxy.  This variable is useful if you want to avoid a single point of egress.  When a proxy is used, both `al_agent_egress_host` and `al_agent_proxy_url` values are required.  If you specify a proxy URL ensure that it is a properly formatted URI.  String defaults to `nil`

## Dependencies

* no known dependancies

## Example Playbook

    ---
    - name: Apply AL Agent install to specific hosts
      hosts: al_agents
      roles:
        - { role: deekayen.alagent}

## Configurations

The variable `al_agent_for_imaging` determine your installation type.  It is a boolean value and by default is `false`.  Setting this value to true will prepare your agent for imaging only and will not provision the agent.

Performing an agent install using the cookbook's default attributes, will setup the agent and provision the instance immediately. If you have properly set your registration key, your host should appear within Alert Logic's Console within 15 minutes. Note: in AWS and Azure deployments the use of the key is optional and in general not necessary.

## Contributing

1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

## License and Authors

License:

Distributed under the Apache 2.0 license.

Authors:
Muram Mohamed (mmohamed@alertlogic.com)
Justin Early (jearly@alertlogic.com)
