import os


if __name__ == '__main__':
    lines = os.popen("ifconfig").readlines()
    configs = []
    config = []
    for line in lines:
        if line != "\n":
            config.append(line.strip())
        else:
            configs.append(config)
            config = []
    for config in configs:
        if config[0].startswith("venet0"):
            print(config[1].split(" ")[1])
