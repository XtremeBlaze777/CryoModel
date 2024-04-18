#!/bin/bash
cd /root/CryoModel
. ./venv/bin/activate
cd CryoMEM

python3.8 memory_model.py configs/cache-sram.cfg 77 22 1 0.4 8192 cache > /dev/null
cachefile="configs/cache-sram.cfg.out"
# grab the first line
headers=$(head -n 1 $cachefile | cut -d, -f6-11)

# grab elements 6-11 of the last line in this csv
cacheline=$(tail -n 1 $cachefile | cut -d, -f6-11)

python3.8 memory_model.py configs/DRAM.cfg 77 22 1 0.4 8192 dram 1.2 0.4 > /dev/null
dramfile="configs/DRAM.cfg.out"
# grab elements 6-11 of the last line in this csv
dramline=$(tail -n 1 $dramfile | cut -d, -f6-11)

echo $headers
echo $cacheline
echo $dramline

# for each element in the lines, calculate 0.9*cache and 0.1*dram
for i in $(seq 1 6); do
	cache=$(echo $cacheline | cut -d, -f$i)
	dram=$(echo $dramline | cut -d, -f$i)
	# echo "cache: $cache, dram: $dram"
	echo "0.9*$cache + 0.1*$dram" | bc
done