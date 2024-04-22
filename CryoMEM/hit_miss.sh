#!/bin/bash
cd /root/CryoModel
. ./venv/bin/activate
cd CryoMEM

# python3.8 memory_model.py configs/cache-sram.cfg 77 22 1 0.4 8192 cache > /dev/null
# cachefile="configs/cache-sram.cfg.out"
# # grab the first line
# headers=$(head -n 1 $cachefile | cut -d, -f6-11)

# # grab elements 6-11 of the last line in this csv
# cacheline=$(tail -n 1 $cachefile | cut -d, -f6-11)

# python3.8 memory_model.py configs/DRAM.cfg 77 22 1 0.4 8192 dram 1.2 0.4 > /dev/null
# dramfile="configs/DRAM.cfg.out"
# # grab elements 6-11 of the last line in this csv
# dramline=$(tail -n 1 $dramfile | cut -d, -f6-11)

# echo $headers
# echo $cacheline
# echo $dramline

# # for each element in the lines, calculate 0.9*cache and 0.1*dram
# for i in $(seq 1 6); do
# 	cache=$(echo $cacheline | cut -d, -f$i)
# 	dram=$(echo $dramline | cut -d, -f$i)
# 	# echo "cache: $cache, dram: $dram"
# 	echo "0.9*$cache + 0.1*$dram" | bc
# done




# grid sweep
sizes=(2048 4096 8192 16384)
temps=(77 4 300)
associativities=(0 4 8)
technology=(0.22 32 45)
for temp in 77 4 300; do
	for size in 2048 4096 8192 16384; do
		sed -i 's/-size (bytes) .*/-size (bytes) '$size'/' configs/cache-sram_sed.cfg
		for assoc in 0 4 8; do
			sed -i 's/-associativity .*/-associativity '$assoc'/' configs/cache-sram_sed.cfg
			for tech in 22 32 45; do
				sed -i 's/-technology (u) .*/-technology (u) '0.0$tech'/' configs/cache-sram_sed.cfg
				python3.8 memory_model.py configs/cache-sram_sed.cfg $temp $tech 1 0.4 $size cache > /dev/null
				python3.8 memory_model.py configs/DRAM.cfg $temp $tech 1 0.4 $size dram 1.2 0.4 > /dev/null
			done
		done
	done
done
	