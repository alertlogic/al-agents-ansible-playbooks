# Ansible Role: al-agents

An Ansible role that installs the AlertLogic Agent on Centos 6.x, 7.x and Debian 6.x and 7.x

## Role Variables

Available variables are listed below, along with default values:

    al_agent_registration_key: <your registration key goes here> # Required
    al_agent_egress_port: '' # Optional
    al_agent_egress_host: '' # Optional
    al_agent_proxy_url: '' # Optional
    al_agent_for_autoscaling: True/False # Default is False
    al_agent_for_imaging: True/False # Default is False

## Dependencies

- no known dependancies

## Example Playbook

    ---
    - name: Apply AL Agent install to specific hosts
      hosts: al_agents
      roles:
        - { role: alertlogic.al_agents}

## License

Apache
