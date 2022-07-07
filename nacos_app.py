# 导入本地配置dict
# 导入sdk
from config import nacos, myConfig


def start():
    # 创建初始nacos连接对象
    nacosServer = nacos.nacos(ip=myConfig.nacosIp, port=myConfig.nacosPort)

    # 将本地配置注入到nacos对象中即可获取远程配置，并监听配置变化实时变更
    # nacosServer.config(dataId="python.json",group="dev",tenant="public",myConfig=myConfig.GlobalConfig)
    # 配置服务注册的参数
    nacosServer.registerService(serviceIp=myConfig.ip, servicePort=myConfig.port, serviceName="exApi-service",
                                namespaceId="", groupName="DEFAULT_GROUP")
    # 开启监听配置的线程和服务注册心跳进程的健康检查进程
    nacosServer.healthyCheck()


if __name__ == '__main__':
    start()
