import yaml


def main():
    with open("config_mine_board.yaml", encoding="utf-8") as f:
        data = yaml.load(f)

    y = data["parsers"][0]["yaml"]["mix-rule-providers"]
    for i in y:
        y[i]["url"] = "https://raw.githubusercontent.com/xinghui233/clashrule/myrules/rules/clash/%s.txt" % i
        print(data["parsers"][0]["yaml"]["mix-rule-providers"][i]["url"])

    with open("clash_config.yaml", "w", encoding="utf-8") as f:
        # FXX 生成的yaml文件code部分为字符 需手动修改
        #   生成的文件无注释
        yaml.dump(data, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)


if __name__ == "__main__":
    main()
