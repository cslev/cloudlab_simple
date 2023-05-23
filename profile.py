kube_description= \
"""
cslev: Some pure Ubuntu 20.04 VMs bootstrapped with docker and docker-compose capabilities
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
  key = str("beast_{}".format(i))
  node = request.RawPC(str(key))
  #node.hardware_type = "m400" ##ARM
  #node.hardware_type = "xl170" ##AMD64 - intel xeon
  node.hardware_type = "rs440" ##Mass cluster, Xeon Gold 6130 skylake (16 core each CPU)
  #node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:DEB8-64-STD' #<-- does not work
  #node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
  # node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
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

# ------
# Clemson cluster (as of 04/2022)
# ------
#   - c8220: 96 nodes (Ivy Bridge, 20 core)
#   CPU:  Two Intel E5-2660 v2 10-core CPUs at 2.20 GHz (Ivy Bridge)
#   MEM:  256GB ECC Memory (16x 16 GB DDR4 1600MT/s dual rank RDIMMs
#   DISK: Two 1 TB 7.2K RPM 3G SATA HDDs
#   NIC:  Dual-port Intel 10Gbe NIC (PCIe v3.0, 8 lanes
#   NIC:  Qlogic QLE 7340 40 Gb/s Infiniband HCA (PCIe v3.0, 8 lanes)
  
#   - c8220x: 4 nodes (Ivy Bridge, 20 core, 20 disks)
#   CPU:  Two Intel E5-2660 v2 10-core CPUs at 2.20 GHz (Ivy Bridge)
#   MEM:  256GB ECC Memory (16x 16 GB DDR4 1600MT/s dual rank RDIMMs
#   DISK: Eight 1 TB 7.2K RPM 3G SATA HDDs
#   DISK: Twelve 4 TB 7.2K RPM 3G SATA HDDs
#   NIC:  Dual-port Intel 10Gbe NIC (PCIe v3.0, 8 lanes
#   NIC:  Qlogic QLE 7340 40 Gb/s Infiniband HCA (PCIe v3.0, 8 lanes)
  
#   - c6320: 84 nodes (Haswell, 28 core)
#   CPU:  Two Intel E5-2683 v3 14-core CPUs at 2.00 GHz (Haswell)
#   MEM:  256GB ECC Memory
#   DISK: Two 1 TB 7.2K RPM 3G SATA HDDs
#   NIC:  Dual-port Intel 10Gbe NIC (X520)
#   NIC:  Qlogic QLE 7340 40 Gb/s Infiniband HCA (PCIe v3.0, 8 lanes)
  
#   - c4130: 2 nodes (Haswell, 28 core, two GPUs)
#   CPU:  Two Intel E5-2680 v3 12-core processors at 2.50 GHz (Haswell)
#   MEM:  256GB ECC Memory
#   DISK: Two 1 TB 7.2K RPM 3G SATA HDDs
#   GPU:  Two Tesla K40m GPUs
#   NIC:  Dual-port Intel 1Gbe NIC (i350)
#   NIC:  Dual-port Intel 10Gbe NIC (X710)
#   NIC:  Qlogic QLE 7340 40 Gb/s Infiniband HCA (PCIe v3.0, 8 lanes)

#   - dss7500: 2 nodes (Haswell, 12 core, 270TB disk)
#   CPU:  Two Intel E5-2620 v3 6-core CPUs at 2.40 GHz (Haswell)
#   MEM:  128GB ECC Memory
#   DISK: Two 120 GB 6Gbps SATA SSDs
#   DISK: 45 6 TB 7.2K RPM 6Gbps SATA HDDs
#   NIC:  Dual-port Intel 10Gbe NIC (X520)

#   - c6420: 72 nodes (Intel Skylake, 32 core, 2 disk)
#   CPU:  Two Sixteen-core Intel Xeon Gold 6142 CPUs at 2.6 GHz
#   MEM:  384GB ECC DDR4-2666 Memory
#   DISK: Two Seagate 1TB 7200 RPM 6G SATA HDs
#   NIC:  Dual-port Intel X710 10Gbe NIC

#   - ibm8335: 6 nodes (POWER8NVL, 20 core, 256GB RAM, 1 GPU)
#   CPU:  Two ten-core (8 threads/core) IBM POWER8NVL CPUs at 2.86 GHz
#   MEM:  256GB 1600MHz DDR4 memory
#   DISK: Two Seagate 1TB 7200 RPM 6G SATA HDDs (ST1000NX0313)
#   GPU: Two NVIDIA GP100GL (Tesla P100 SMX2 16GB)
#   NIC:  One Broadcom NetXtreme II BCM57800 1/10 GbE NIC
#   FPGA:  One ADM-PCIE-KU3 (Xilinx Kintex UltraScale)

#   - r7525: 15 nodes (AMD EPYC Rome, 64 core, 512GB RAM, 2 x GPU)
#   CPU:  Two 32-core AMD 7542 at 2.9GHz
#   MEM:  512GB ECC Memory (16x 32 GB 3200MHz DDR4)
#   DISK: One 2TB 7200 RPM 6G SATA HDD
#   GPU:  Two NVIDIA GV100GL (Tesla V100S PCIe 32GB)
#   NIC:  Dual-port Mellanox ConnectX-5 25 Gb NIC (PCIe v4.0)
#   NIC:  Dual-port Mellanox BlueField2 100 Gb SmartNIC

# ------
# Apt cluster (as of 04/2022)
# ------
#   - r320: 128 nodes (Sandy Bridge, 8 cores)
#   CPU:  1x Xeon E5-2450 processor (8 cores, 2.1Ghz)
#   MEM:  16GB Memory (4 x 2GB RDIMMs, 1.6Ghz)
#   DISK: 4 x 500GB 7.2K SATA Drives (RAID5)
#   NIC:  1GbE Dual port embedded NIC (Broadcom)
#   NIC:  1 x Mellanox MX354A Dual port FDR CX3 adapter w/1 x QSA adapter

#   - c6220: 64 nodes (Ivy Bridge, 16 cores)
#   CPU:  2 x Xeon E5-2650v2 processors (8 cores each, 2.6Ghz)
#   MEM:  64GB Memory (8 x 8GB DDR-3 RDIMMs, 1.86Ghz)
#   DISK: 2 x 1TB SATA 3.5 7.2K rpm hard drives
#   NIC:  4 x 1GbE embedded Ethernet Ports (Broadcom)
#   NIC:  1 x Intel X520 PCIe Dual port 10Gb Ethernet NIC
#   NIC:  1 x Mellanox FDR CX3 Single port mezz card

# ------
# Mass cluster (as of 04/2022)
# ------
#   - rs440: 5 nodes (Skylake, 32 cores)
#   CPU:  2 x Xeon Gold 6130 processors (16 cores each, 2.1Ghz)
#   MEM:  192GB Memory (12 x 16GB RDIMMs)
#   DISK: 1 x 240GB SATA SSD drives
#   NIC:  2 x 10GbE embedded Ethernet Ports (Broadcom 57412)

#   - rs620: 11 nodes (Sandy Bridge, 16 or 20 cores)
#   CPU:  2 x Xeon processors (8-10 cores each, 2.2Ghz or more)
#   MEM:  128-384GB Memory (most have 256GB)
#   DISK: 1 x 900GB 10K SAS Drive
#   NIC:  1GbE Quad port embedded NIC (Intel)
#   NIC:  1 x Solarflare Dual port SFC9120 10G Ethernet NIC

#   - rs630: 28 nodes (Haswell, 20 cores)
#   CPU:  2 x Xeon E5-2660 v3 processors (10 cores each, 2.6Ghz or more)
#   MEM:  256GB Memory (16 x 16GB DDR4 DIMMs)
#   DISK: 1 x 900GB 10K SAS Drive
#   NIC:  1GbE Quad port embedded NIC (Intel)
#   NIC:  1 x Solarflare Dual port SFC9120 10G Ethernet NIC

# ------
# OneLab cluster (as of 04/2022)
# ------
#   - m400: 45 nodes (64-bit ARM)
#   CPU:  Eight 64-bit ARMv8 (Atlas/A57) cores at 2.4 GHz (APM X-GENE)
#   MEM:  64GB ECC Memory (8x 8 GB DDR3-1600 SO-DIMMs)
#   DISK: 120 GB of flash (SATA3 / M.2, Micron M500)
#   NIC:  Dual-port Mellanox ConnectX-3 10 GB NIC (PCIe v3.0, 8 lanes