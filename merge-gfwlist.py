import requests
import base64
import datetime

# 获取 gfwlist 文件内容（base64 编码的）
gfwlist_url = "https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
response = requests.get(gfwlist_url)
response.raise_for_status()
gfwlist_lines = response.text.splitlines()

# 获取个人维护的规则文件内容（标准字符串）
personal_rules_file = "personal_rules.txt"
with open(personal_rules_file, "r") as file:
    personal_rules_lines = file.readlines()

# 创建合并后的文件 autoproxy.txt
output_file = "autoproxy.txt"

descs = [
    "[AutoProxy 0.2.9]",
    "! Last Modified: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "! Expires: 24h",
    "! HomePage: https://github.com/anysoft/autoproxy",
    "! GitHub URL: https://raw.githubusercontent.com/anysoft/autoproxy/release/autoproxy.txt",

]

with open(output_file, "w") as file:
    # for item in descs:
    #     file.write(base64.b64encode(item.encode("utf-8")).decode("utf-8"))
    #     file.write("\n")
    # file.write("\n")

    # 写入 gfwlist 文件内容
    for line in gfwlist_lines:
        line = line.strip()
        decode_line = base64.b64decode(line).decode("utf-8")
        if decode_line.endswith("@cn"):
            continue
        file.write(decode_line + "\n")

    # 写入个人维护的规则文件内容
    for line in personal_rules_lines:
        # encoded_line = base64.b64encode(line.encode("utf-8")).decode("utf-8")
        file.write(line.strip() + "\n")
