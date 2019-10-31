from automator import Automator
import subprocess

if __name__ == '__main__':
    # 升级建筑列表, 实际升级是随机从这个列表中挑一个升级, 为空不升级
    # up_list = [(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5)]  # 雨露均沾
    # up_list = [(1,1),(1,1),(1,1),(4,3)] # 75%的概率1号升级1次， 25%的概率4号升级3次
    # up_list = [(8,1),(9,1)] # 这个号建筑升级1次， 那个号建筑升级1次
    up_list = [(2,1)] # 这个号建筑升级1次， 那个号建筑升级1次
    # 收货过滤列表
    # harvest_filter = [2,5,7] # 收取这些号建筑的货物
    harvest_filter = [1,2,3,4,5,6,7,8,9] # 收取这些号建筑的货物
    # harvest_filter = [5, 6, 9]
    # adb设备列表
    # Device1 = 'QV7039V30X'
    # Device2 = 'CB512BC4ZL'
    # Device1Net = '10.21.20.105'
    # Device2Net = '10.21.59.70'
    # MuMu = '127.0.0.1:7555'
    MuMu = '53aac21a'

    policy = True # 是否自动升级政策
    task = True # 是否自动完成任务
    speed_up = False # 是否自动重启加速刷火车
    in_shop = True # 是否自动进商店拆红包和相册 顺序是福气红包-多福红包-满福红包-相册，不管有没有足够的蓝星币，都点一轮 by scoful
    if b'connected' in subprocess.check_output('adb connect '+ MuMu):
        print("Successfully connected to MuMu.")
    instance = Automator(MuMu, up_list, harvest_filter,auto_policy=policy,auto_task=task,speedup=speed_up,auto_shop=in_shop)
    # 启动脚本。
    instance.start()
    
