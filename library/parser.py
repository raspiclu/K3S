from isc_dhcp_leases import Lease, IscDhcpLeases



def parse():
	all_ips = []
	all_hostnames = []

	leases = IscDhcpLeases('/var/lib/dhcp/dhcpd.leases')
	all_leases = leases.get()

	for lease in all_leases:
  		all_ips.append(lease.ip)

	for ip in all_ips:
  		hostname = 'worker1-'+ ip[8:]
  		all_hostnames.append(hostname)

	return all_ips

parse()
