L1=0.215129
L2=0.365081
MM=4.04402 + 4.99923 + 1.32167

for rate in [x/10 for x in range(10)]:
    print(L1 + rate*(L2 + (rate*MM)))