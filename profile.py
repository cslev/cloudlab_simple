kube_description= \
"""
cslev: Some pure Ubuntu 18.04 VMs bootstrapped with docker and docker-compose capabilities
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

# Hardware profiles that can be enforced here via 'hardware_type'
# ------
# Utah cluster (as of 04/2022)
# ------
#   - m400: 	315 nodes (64-bit ARM)
#   CPU:  Eight 64-bit ARMv8 (Atlas/A57) cores at 2.4 GHz (APM X-GENE)
#   MEM:  64GB ECC Memory (8x 8 GB DDR3-1600 SO-DIMMs)  
#   DISK: 120 GB of flash (SATA3 / M.2, Micron M500)
#   NIC:  Dual-port Mellanox ConnectX-3 10 GB NIC (PCIe v3.0, 8 lanes

#   - m510: 270 nodes (Intel Xeon-D)
#   CPU:  Eight-core Intel Xeon D-1548 at 2.0 GHz 
#   MEM:  64GB ECC Memory (4x 16 GB DDR4-2133 SO-DIMMs)
#   DISK: 256 GB NVMe flash storage
#   NIC:  Dual-port Mellanox ConnectX-3 10 GB NIC (PCIe v3.0, 8 lanes

#   - xl170: 200 nodes (Intel Broadwell, 10 core, 1 disk)
#   CPU:  Ten-core Intel E5-2640v4 at 2.4 GHz
#   MEM:  64GB ECC Memory (4x 16 GB DDR4-2400 DIMMs)
#   DISK: Intel DC S3520 480 GB 6G SATA SSD
#   NIC:  Two Dual-port Mellanox ConnectX-4 25 GB NIC (PCIe v3.0, 8 lanes

#   - d6515: 28 nodes (AMD EPYC Rome, 32 core, 2 disk, 100Gb Ethernet)
#   CPU:  32-core AMD 7452 at 2.35GHz
#   MEM:  128GB ECC Memory (8x 16 GB 3200MT/s RDIMMs)
#   DISK: Two 480 GB 6G SATA SSD
#   NIC:  Dual-port Mellanox ConnectX-5 100 GB NIC (PCIe v4.0)
#   NIC:  Dual-port Broadcom 57414 25 GB NIC

#   - c6525-25g: 144 nodes (AMD EPYC Rome, 16 core, 2 disk, 25Gb Ethernet)
#   CPU:  16-core AMD 7302P at 3.00GHz
#   MEM:  128GB ECC Memory (8x 16 GB 3200MT/s RDIMMs)
#   DISK: Two 480 GB 6G SATA SSD
#   NIC:  Two dual-port Mellanox ConnectX-5 25Gb GB NIC (PCIe v4.0)

#   - c6525-100g: 36 nodes (AMD EPYC Rome, 24 core, 2 disk, 25/100Gb Ethernet)
#   CPU:  24-core AMD 7402P at 2.80GHz
#   MEM:  128GB ECC Memory (8x 16 GB 3200MT/s RDIMMs)
#   DISK: Two 1.6 TB NVMe SSD (PCIe v4.0)
#   NIC:  Dual-port Mellanox ConnectX-5 25 GB NIC (PCIe v4.0)
#   NIC:  Dual-port Mellanox ConnectX-5 Ex 100 GB NIC (PCIe v4.0)

# ------
# Wisconsin cluster (as of 04/2022)
# ------
#   - c220g1: 90 nodes (Haswell, 16 core, 3 disks)
#   CPU:  Two Intel E5-2630 v3 8-core CPUs at 2.40 GHz (Haswell w/ EM64T)
#   RAM:  128GB ECC Memory (8x 16 GB DDR4 1866 MHz dual rank RDIMMs)
#   Disk: Two 1.2 TB 10K RPM 6G SAS SFF HDDs
#   Disk: One Intel DC S3500 480 GB 6G SATA SSDs
#   NIC:  Dual-port Intel X520-DA2 10Gb NIC (PCIe v3.0, 8 lanes)
#   NIC:  Onboard Intel i350 1Gb

#   - c240g1: 10 nodes (Haswell, 16 core, 14 disks)
#   CPU:  Two Intel E5-2630 v3 8-core CPUs at 2.40 GHz (Haswell w/ EM64T)
#   MEM:  128GB ECC Memory (8x 16 GB DDR4 1866 MHz dual rank RDIMMs)
#   DISK: Two Intel DC S3500 480 GB 6G SATA SSDs
#   DISK: Twelve 3 TB 3.5" HDDs donated by Seagate
#   NIC:  Dual-port Intel X520-DA2 10Gb NIC (PCIe v3.0, 8 lanes)
#   NIC:  Onboard Intel i350 1Gb

#   - c220g2: 163 nodes (Haswell, 20 core, 3 disks)
#   CPU:  Two Intel E5-2660 v3 10-core CPUs at 2.60 GHz (Haswell EP)
#   MEM:  160GB ECC Memory (10x 16 GB DDR4 2133 MHz dual rank RDIMMs)
#   DISK: One Intel DC S3500 480 GB 6G SATA SSDs
#   DISK: Two 1.2 TB 10K RPM 6G SAS SFF HDDs
#   NIC:  Dual-port Intel X520 10Gb NIC (PCIe v3.0, 8 lanes
#   NIC:  Onboard Intel i350 1Gb

#   - c240g2: 4 nodes (Haswell, 20 core, 8 disks)
#   CPU:  Two Intel E5-2660 v3 10-core CPUs at 2.60 GHz (Haswell EP)
#   MEM:  160GB ECC Memory (10x 16 GB DDR4 2133 MHz dual rank RDIMMs)
#   DISK: Two Intel DC S3500 480 GB 6G SATA SSDs
#   DISK: Two 1TB HDDs
#   DISK:  Four 3TB HDDs
#   NIC:  Dual-port Intel X520 10Gb NIC (PCIe v3.0, 8 lanes
#   NIC:  Onboard Intel i350 1Gb

#   - c220g5: 224 nodes (Intel Skylake, 20 core, 2 disks)
#   CPU:  Two Intel Xeon Silver 4114 10-core CPUs at 2.20 GHz
#   MEM:  192GB ECC DDR4-2666 Memory
#   DISK: One 1 TB 7200 RPM 6G SAS HDs
#   DISK: One Intel DC S3500 480 GB 6G SATA SSD
#   NIC:  Dual-port Intel X520-DA2 10Gb NIC (PCIe v3.0, 8 lanes)
#   NIC:  Onboard Intel i350 1Gb

#   - c240g5: 32 nodes (Intel Skylake, 20 core, 2 disks, GPU)
#   CPU:  Two Intel Xeon Silver 4114 10-core CPUs at 2.20 GHz
#   MEM:  192GB ECC DDR4-2666 Memory
#   DISK: One 1 TB 7200 RPM 6G SAS HDs
#   DISK: One Intel DC S3500 480 GB 6G SATA SSD
#   GPU:  One NVIDIA 12GB PCI P100 GPU
#   NIC:  Dual-port Intel X520-DA2 10Gb NIC (PCIe v3.0, 8 lanes)
#   NIC:  Onboard Intel i350 1Gb

#   - c4130: 4 nodes (Intel Broadwell, 16 core, 2 disks, 4 GPUs)
#   CPU:  Two Intel Xeon E5-2667 8-core CPUs at 3.20 GHz
#   MEM:  128GB ECC Memory
#   DISK: Two 960 GB 6G SATA SSD
#   GPU:  Four NVIDIA 16GB Tesla V100 SMX2 GPUs