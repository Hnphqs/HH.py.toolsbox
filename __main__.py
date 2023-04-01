#Copyright HNPHQS
#App version: 1.0
#App name: HH.py.toolsbox





#-----导入需要的库
print("加载中...")
import time, sys, os #python标准库
from lib import requests, json #可能需要下载的库python3
app=18107
appname='HH.py.toolsbox'
appversion="1.0"
#-----卡密验证系统
print("请求中...")
def api(url,ok,out=False):
    try:
        response = requests.post(url)
    except OSError:
        print("请求失败!网络不通!")
        print("重新尝试...(有多次尝试无果,请尝试切换网络)")
        return api(url,ok,out)
    response = json.loads(response.content)
    if response['code']!=ok:
        if out==True:            
            raise ConnectionError(f"认证失败!{response['code']}错误")
        elif out==False:
            print("api调用失败")
    return response
kami=input('卡密：')
markcode=input('卡密绑定码(没有会自动创建一个)：')
t=time.time()
url = f'https://cute521.cn/api.php?api=kmlogon&app={app}&kami={kami}&t={t}&markcode={markcode}'
print("请求中...")
kamiapi=api(url,200,True)
print("卡密认证成功")
#-----获取账号
vip=kamiapi['msg']['vip']
print('------------------------------\n加载函数...')
print('获取参数...')
#-----调用api获取设备参数
sys=api("https://api.uomg.com/api/visitor.info?skey=774740085",1);system=sys["system"];ip=sys["ip"];netime=sys["time"]
print(f'''\
设备信息：
        系统：{system}
        ip：{ip}
        序列号：unknow
        网络时间：{netime}
        设备时间：{t}
        卡密：{kami}
        绑定码：{markcode}
        登录账号：{vip}''')
input("输入任意键继续")
#-----主体代码

def menu1():
    os.system("clear")
    menu='''\
            1.进入程序
            2.退出程序
            3.关于
            '''
    print(menu)
    chose=input("请输入: ")
    def chose1():
        menu1_1()
        menu1()
    def chose2():
        sys.exit(0)
    def chose3():
        os.system("clear")
        print(f'''\
                Copyright HNPHQS
                当前版本：{appversion}
                  HH.py.toolsbox是一个pyt
                hon工具箱,更多功能还在探
                索中...
                ''')
        input("按任意键返回")
        menu1()
    if chose=="1":
        chose1()
    elif chose=="2":
        chose2()
    elif chose=="3":
        chose3()
    else:
        print("非法输入!")
        menu1()
def menu1_1():
    os.system("clear")
    menu='''\
            1.和某人的qq建立对话

            '''
    print(menu)
    chose=input("请输入：")
    def chose1():
        os.system("clear")
        qid=(input("请对方输入qq号："))
        an=api(f"https://api.uomg.com/api/long2dwz?dwzapi=urlcn&url=https://api.uomg.com/api/qq.talk?qq={qid}",1)
        print(f"浏览器访问{an['ae_url']}自动跳转至qq与Ta对话")
        input("按任意键返回")
        menu1_1()
    if chose=="1":
        chose1()






if __name__=="__main__":
    menu1()
