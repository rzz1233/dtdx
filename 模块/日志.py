import logging

logging.basicConfig(level=logging.INFO,
                    filename='11.log',
                    filemode='a',
                    encoding='utf-8',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 开始使用log功能
logging.info('这是 loggging info message')
logging.debug('这是 loggging debug message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')

# 日志记录分为不同的级别，代表了事件的重要性：
#
# DEBUG: 调试信息，通常用于开发阶段，记录详细的运行信息。
# INFO: 普通信息，记录系统的运行状态。
# WARNING: 警告信息，系统可能出现问题，但不影响运行。
# ERROR: 错误信息，系统功能受到了影响。
# CRITICAL: 严重错误，系统可能无法继续运行


import logging
# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO) # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a') # open的打开模式这里可以进行参考
fh.setLevel(logging.DEBUG) # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING) # 输出到console的log等级的开关
# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 第五步，将logger添加到handler里
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message ')
logger.critical('这是 logger critical message')
