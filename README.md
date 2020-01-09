# Build a Kubernetes cluster using k3s via Ansible.

@author @mhizli

Credits and source:

*  https://github.com/itwars 
*  https://github.com/rancher/k3s 
*  https://everythingshouldbevirtual.com/ansible-generating-inventory-from-dnsmasq-leases/
*  https://github.com/giuaig/ansible-raspi-config
*  https://github.com/ryankwilliams/ansible-ssh-copy-id
            


## K3s Ansible Playbook

Build a Kubernetes cluster using Ansible with k3s. The goal is easily install a Kubernetes cluster on Raspberry Pis. If a Cluster exists then the goal is easily to join a worker into the cluster


## System requirements:

Deployment environment must have Ansible 2.4.0+
Master and nodes must have passwordless SSH access. This will be automatically executes with scripts.
DNSMASQ DHCP-Server must be running on the master.

There are two different inventory files:
1. hosts.ini (Inventory which is  for creating a new Cluster by DHCP-Leases)
2. oneHost.ini (Inventory which is for joining one single new worker by DHCP-Lease)


Start provisioning of the cluster using the following command:

Create a dynamic inventory (takes the entries from the leases file)

```
ansible-playbook -i hosts.ini capture_all_dhcp_leases.yml

ansible-playbook -i hosts.ini site.yml
```

Start script to join an new worker to the cluster:
Create a dynamic inventory (takes the last entry from the leases file)

```
ansible-playbook -i oneHost.ini capture_dhcp_leases.yml

ansible-playbook -i oneHost.ini joinNew.yml
```

## Dynamic Inventory

For creating dynamic inentories there are two definied jinja2 templates,

For hosts.ini the template file is hosts.ini.j2 
For oneHost.ini the template file is oneHost.ini.j2

The scripts: capture_all_dhcp_leases.yml and capture_dhcp_leases.yml read the jinja2 templates and generate the new .ini inventory.

The scripts: site.yml and joinNew.yml are scripts and they contain the procedure for executing the tasks. The executed tasks script are in the directory /roles/{taskname}/tasks/main.yml





