kube_description= \
"""
Levi: Four pure Ubuntu 18.04 VMs running DoH traffic captures.
"""
kube_instruction= \
"""
Check the following github repo for more information
https://github.com/cslev/quic_cloudlabs
"""

import geni.portal as portal
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab
import geni.rspec.igext as IG

# Create a portal object
pc = portal.Context()
request = pc.makeRequestRSpec()


tour = IG.Tour()
tour.Description(IG.Tour.TEXT,kube_description)
tour.Instructions(IG.Tour.MARKDOWN,kube_instruction)
request.addTour(tour)


# node quic on UTAH cluster
for i in range(1,11):
  key = str("quic_docker_{}".format(i))
  kube_quic = request.RawPC(str(key))
  # kube_quic.hardware_type = "m400" ##ARM - Eight 64-bit ARMv8 (Atlas/A57) cores at 2.4 GHz (APM X-GENE)
  kube_quic.hardware_type = "xl170" ##Intel x86_64 - 	Ten-core Intel E5-2640v4 at 2.4 GHz
  #kube_quic.hardware_type = "d6515"  ##AMD x86_64 -  AMD EPYC ROMTE, 32-cre AMD 7452 @ 2.35GHz
  #kube_doh.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:DEB8-64-STD' #<-- does not work
  kube_quic.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
  kube_quic.Site(str(key))

  #START the docker-based version
  kube_quic.addService(pg.Execute(shell="bash", command="/local/repository/cloudlabs_start_docker.sh"))

portal.context.printRequestRSpec()
