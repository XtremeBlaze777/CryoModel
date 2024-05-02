L1=65536
L2=262144
MM=16

rm hit_miss.out
for temp in 4 77 300
do
    sed -i 's/-size (bytes) .*/-size (bytes) '$L1'/' configs/cache-sram_miss.cfg
    python3.8 memory_model.py configs/cache-sram_miss.cfg $temp 22 1 0.4 $L1 cache >> hit_miss.out

    sed -i 's/-size (bytes) .*/-size (bytes) '$L2'/' configs/cache-sram_miss.cfg
    python3.8 memory_model.py configs/cache-sram_miss.cfg $temp 22 1 0.4 $L2 cache >> hit_miss.out

    sed -i 's/-size (Gb) .*/-size (Gb) '$MM'/' configs/cache-sram_miss.cfg
    python3.8 memory_model.py configs/DRAM_miss.cfg $temp 22 1 0.4 $MM dram 1.2 0.4 >> hit_miss.out
done