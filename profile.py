kube_description= \
"""
Levi: Four pure Ubuntu 18.04 VMs running DoH traffic captures.
"""
kube_instruction= \
"""
Check the following github repo for more information
https://github.com/cslev/cloudlab_simple
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

for i in range(1,5):
  key = str("doh_docker_{}".format(i))
  node = request.RawPC(str(key))
#   node.hardware_type = "m400" ##ARM
  #node.hardware_type = "xl170" ##AMD64
  node.hardware_type = "d6515" ##Amd epyc
  #node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:DEB8-64-STD' #<-- does not work
  node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
  node.Site(str(key))

  #START the docker-based version
  node.addService(pg.Execute(shell="bash", command="/local/repository/cloudlabs_start_docker.sh"))

portal.context.printRequestRSpec()
