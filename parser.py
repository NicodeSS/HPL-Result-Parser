import numpy as np
import pandas as pd
import re
import sys

if len(sys.argv) != 2:
    print("Error: no input file.")
    exit(1)

input_filename = sys.argv[1]
output_filename = "result.csv"


data = {
    "T/V": [],
    "N": [],
    "NB": [],
    "P": [],
    "Q": [],
    "Time": [],
    "Gflops": []
}
result_count = []
maxn = 0
maxv = 1e-09
regex_rule = r'^(WR[0-9A-Z]*)\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)\s+([0-9.]+)\s+([0-9e+.-]+)$'
with open(input_filename) as f:
    txt = f.readlines()
    for line in txt:
        matchRes = re.match(regex_rule, line)
        if matchRes:
            tv = matchRes.group(1)
            n = matchRes.group(2)
            nb = matchRes.group(3)
            p = matchRes.group(4)
            q = matchRes.group(5)
            time = matchRes.group(6)
            gflops = matchRes.group(7)
            # print(tv, n, nb, p, q, time, gflops)
            data["T/V"].append(tv)
            data["N"].append(int(n))
            data["NB"].append(int(nb))
            data["P"].append(int(p))
            data["Q"].append(int(q))
            data["Time"].append(float(time))
            data["Gflops"].append(float(gflops))
            if float(gflops) > maxv:
                maxn = len(data["Gflops"])-1
                maxv = float(gflops)

data["T/V"].insert(0, "Best:" + str(maxn+1) + "(" + data["T/V"][maxn]+")")
data["N"].insert(0, data["N"][maxn])
data["NB"].insert(0, data["NB"][maxn])
data["P"].insert(0, data["P"][maxn])
data["Q"].insert(0, data["Q"][maxn])
data["Time"].insert(0, data["Time"][maxn])
data["Gflops"].insert(0, data["Gflops"][maxn])
maxn += 1

print("Best Data:\n", data["T/V"][maxn], data["N"][maxn], data["NB"][maxn],
      data["P"][maxn], data["Q"][maxn], data["Time"][maxn], data["Gflops"][maxn])
print("Best Data Time: ", data["Time"][maxn])
print("Best Data GFlops: ", data["Gflops"][maxn], "GFlops")

df = pd.DataFrame(data)
df.to_csv(output_filename)
