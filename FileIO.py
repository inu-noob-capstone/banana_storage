import json

#현재 setting들을 파일로 저장하기.
def saveSettingAsFile(lightSetting, waterSetting):
    lightFile = open('/root/Desktop/Capstone Design/banana-storage/ServerFiles/lightSetting.json', 'w', encoding='utf-8')
    json.dump(lightSetting.dict, lightFile, indent="\t")
    lightFile.close()

    waterFile = open('/root/Desktop/Capstone Design/banana-storage/ServerFiles/waterSetting.json', 'w', encoding='utf-8')
    json.dump(waterSetting.dict, waterFile, indent="\t")
    waterFile.close()
    
    '''with open('/root/Desktop/Capstone Design/banana-storage/ServerFiles/lightSetting.json', 'w', encoding='utf-8') as lightFile:
        json.dump(lightSetting.dict, lightFile, indent="\t")
        lightFile.close()

    with open('/root/Desktop/Capstone Design/banana-storage/ServerFiles/waterSetting.json', 'w', encoding='utf-8') as waterFile:
        json.dump(waterSetting.dict, waterFile, indent="\t")
        waterFile.close()'''

#파일에서 정보 읽어와서 setting에 적용하기.   
def readSettingFile(lightSetting, waterSetting):
    lightFile = open('/root/Desktop/Capstone Design/banana-storage/ServerFiles/lightSetting.json', 'r', encoding='UTF-8')
    lightSetting.dict = json.load(lightFile)
    lightFile.close()

    waterFile = open('/root/Desktop/Capstone Design/banana-storage/ServerFiles/waterSetting.json', 'r', encoding='UTF-8')
    waterSetting.dict = json.load(waterFile)
    waterFile.close()
    
    '''with open('/root/Desktop/Capstone Design/banana-storage/ServerFiles/lightSetting.json', 'r', encoding='UTF-8') as lightFile:
        lightSetting.dict = json.load(lightFile)
        lightFile.close()

    with open('/root/Desktop/Capstone Design/banana-storage/ServerFiles/waterSetting.json', 'r', encoding='UTF-8') as waterFile:
        waterSetting.dict = json.load(waterFile)
        waterFile.close()'''
