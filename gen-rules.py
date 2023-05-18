import requests
import datetime

# 发起 HTTP GET 请求获取规则列表内容
response = requests.get("https://raw.githubusercontent.com/v2fly/domain-list-community/release/geolocation-!cn.txt")
response.raise_for_status()
rules = response.text.splitlines()

# 创建 autoproxy.txt 文件并写入规则列表内容
with open("autoproxy.txt", "w") as f:
    f.write("[AutoProxy 0.2.9]\n")
    f.write("! Last Modified: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("! Expires: 24h\n")
    f.write("! HomePage: https://github.com/anysoft/autoproxy\n")
    f.write("! GitHub URL: https://raw.githubusercontent.com/anysoft/autoproxy/release/autoproxy.txt\n")
    f.write("\n")

    for rule in rules:
        if rule.endswith("@cn"):
            continue
        rule = rule.replace(":@ads", "")
        if rule.startswith("domain:"):
            f.write(rule.replace("domain:", "||", 1) + "\n")
        elif rule.startswith("full:"):
            f.write(rule.replace("full:", "|http://", 1) + "\n")
            f.write(rule.replace("full:", "|https://", 1) + "\n")
        elif rule.startswith("keyword:"):
            f.write(rule.replace("keyword:", "") + "\n")
        elif rule.startswith("regexp:"):
            f.write(rule.replace("regexp:", "/", 1) + "/" + "\n")
        else:
            print("Unknown format:", rule)
