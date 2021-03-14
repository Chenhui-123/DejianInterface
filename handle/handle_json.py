import os
import sys
base_path=os.getcwd()
sys.path.append(base_path)
import json

class HandJson:
    def __init__(self):
        pass
    def read_json(self,file_name=None):
        if file_name==None:
            file_path=base_path+"/config/code_message.json"
        else:
            file_path=base_path+file_name
        with open(file_path,'r',encoding='UTF-8') as f:
            data=json.load(f)
            return data
    def get_value(self,key,file_name=None):
        data=self.read_json()
        return data.get(key)
handJson=HandJson()
if __name__=='__main__':
    handJson=HandJson()
    #print(handJson.get_value('/zybk/api/ad/adconfig?ip=111.194.219.35&timestamp=1613728431246&pluginVersion=148&zyeid=7264245f-c66f-4659-aa24-9bb6df37c4f4&usr=j35532181&rgt=7&p1=V3WygQ4dlCADADL64yvBGhkY&pc=10&p2=124008&p3=17136556&p4=501656&p5=12&p6=&p7=__3e932cc0f202a00f&p9=2&p12=&p16=vivo+Y51A&p21=3&p22=5.1.1&p25=17136556&p26=22&p28=&p30=__624900019789874&p31=__3e932cc0f202a00f','/config/code_message.json'))
    a=''
    if a=='':
        print("=======================")
               


