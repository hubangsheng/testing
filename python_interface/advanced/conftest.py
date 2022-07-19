# __author:lenovo
# date:2022/7/19

global_env = {}


# hook 函数，是添加命令行参数使用
def pytest_addoption(parser):
    # group 将下面所有的 option都展示在这个group下
    mygroup = parser.getgroup("hogwarts")
    # 注册一个命令行选项
    mygroup.addoption("--env",
                      # 参数默认值
                      default='test',
                      # 存储的变量
                      dest='env',
                      # 参数的描述信息
                      help="设置接口自动化测试默认的环境"
                      )


# 获取设置的命令行参数
def pytest_configure(config):
    default_ev = config.getoption("--env")
    tmp = {"env": default_ev}
    global_env.update(tmp)
