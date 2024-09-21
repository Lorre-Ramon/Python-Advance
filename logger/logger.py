import logging
import json

# with open("configs/global_configs.json", "r") as f:
#     global_config = json.load(f)

log_filepath = "log/developing_test.log"
logger = logging.getLogger("Richthofen")
logger.setLevel(logging.INFO)

# 创建控制台处理器并设置级别为INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# 创建文件处理器并设置级别为INFO
fh = logging.FileHandler(log_filepath)
fh.setLevel(logging.INFO)

# 创建格式化器并将其添加到处理器
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(ch)
logger.addHandler(fh)