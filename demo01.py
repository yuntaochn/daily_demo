# 实现部分文本替换
import os 
from pathlib import Path


path = Path("./thirdparty/")
files = path.rglob("*.cmake")

cur_path = str(Path.cwd())       # 新的当前目录 
print(cur_path)

i = 0
for f in files:
    with open(f, "r") as tmp, open("%s.bak"%f, "w") as tmp2:
        lines = tmp.readlines()
        for line in lines:
            if ("/home/efort/source/agentcpp" in line):
            # if ("RELATIVE" in line):
                print("****",  f, "\n\t", line)
                line = line.replace("/home/efort/Downloads/agentcpp", "${PROJECT_SOURCE_DIR}")
            tmp2.write(line)
    os.remove(f)
    os.rename("%s.bak"%f, f)
