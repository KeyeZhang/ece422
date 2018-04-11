#!/usr/bin/python2.7
import dpkt
import sys
import socket
from collections import defaultdict
from dpkt.tcp import TCP

def main():
	if (len(sys.argv) < 2):
		print "error: need argument"
		sys.exit(1)

	filename = sys.argv[1]
	print "input filename: " + filename

	syn_dict = defaultdict(int)
	syn_ack_dict = defaultdict(int)

	with open(filename, "rb") as f:
		pcap = dpkt.pcap.Reader(f)
		print "\nParsing Packets...\n"

		for ts, buf in pcap:
			try:
				eth = dpkt.ethernet.Ethernet(buf)
				ip = eth.data
				ip_addr = socket.inet_ntoa(ip.src)

				if type(ip.data) == TCP:
					tcp = ip.data
					ip_addr_src = socket.inet_ntoa(ip.src)
					ip_addr_dst = socket.inet_ntoa(ip.dst)
					syn_flag = ((tcp.flags & dpkt.tcp.TH_SYN) != 0) and ((tcp.flags & dpkt.tcp.TH_ACK) == 0)
					syn_ack_flag = ((tcp.flags & dpkt.tcp.TH_SYN) != 0) and ((tcp.flags & dpkt.tcp.TH_ACK) != 0)

					if syn_flag:
						syn_dict[ip_addr_src] += 1
					if syn_ack_flag:
						syn_ack_dict[ip_addr_dst] += 1

			except: pass

	for key, value in syn_dict.iteritems():
		# print key, value, syn_ack_dict[key]
		if value > 3*syn_ack_dict[key]:
			print key

	sys.exit(0)


if __name__ == '__main__':
	main()
