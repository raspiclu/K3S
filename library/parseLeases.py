from isc_dhcp_leases import Lease, IscDhcpLeases

from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
   'metadata_version': '1.0',
   'status' : ['stable'],
   'supported_by': 'community'
}

#allIps = []
#allHostnames = []


def parse():
   leases = IscDhcpLeases('/var/lib/dhcp/dhcpd.leases')
   allLeases = leases.get()

   for lease in allLeases :
     # print('Lease ist: '+ lease.ip + ', Hostname ist:'  + lease.hostname)
     allIps.append(lease.ip)

   for ip in allIps:
     hostname = 'worker1-'+ ip[8:]
     allHostnames.append(hostname)
     print(hostname)


def run_module():
    module_args = dict(
      ips=dict(type='str', required=True)
    )

    result = dict(
      changed=False,
      original_message='',
      message=''
    )

    # create ansible module object
    module = AnsibleModule(
      argument_spec=module_args,
      supports_check_mode=True
    )

    ips = module.params['ips']
    print('die aktuellen ips sind giulio:' +  ips)


def main():
    run_module()


if __name__ == '__main__': main()
