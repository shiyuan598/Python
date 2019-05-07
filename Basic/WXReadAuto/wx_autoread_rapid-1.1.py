from uiautomator import device as d
import time
import datetime
import random

# 点亮屏幕
def lightScreen():
    d.screen.on()

# 自动翻页，翻页后休息几秒钟
def autoSwipe():
    # 模拟阅读12-15秒钟
    total_time = 15
    read_time = random.randint(12, 15)
    time.sleep(read_time)
    print("阅读花费：", read_time, "秒")
    # 从（1000,500）到（30,500）
    d.swipe(1000, 500, 30, 500)  # 这里需要根据你的模拟器的具体坐标测试
    # 休息一段时间
    rest_time = total_time - read_time
    time.sleep(rest_time)
    print("休息" + str(rest_time) + "秒, 放松下眼睛呦~~~")

# 默认阅读300页，大约300*(15)/60 = 75分钟
if __name__ == '__main__':
    all_time = 300
    user_input_time = input("请输入需要阅读的页数(请输入正整数):")
    try:
        user_input_time = int(user_input_time)
        if (user_input_time > 0):
            print("您本次将阅读", user_input_time, "页，加油！")
            all_time = user_input_time
    except:
        print("您输入的值不合法， 将使用默认参数, 自动阅读300页")
        pass

    for i in range(all_time * 4):
        lightScreen()
        print("开始阅读...")
        autoSwipe()
        print("==>已经阅读", i + 1, "页，还有", all_time - i - 1, "页呦")
