import http.server
from urllib.parse import urlparse
from urllib.parse import parse_qs
from FileIO import readSettingFile
from FileIO import saveSettingAsFile

from LightControl import LightSetting
from WaterControl import WaterSetting
from threading import Lock

#8082포트 이용
#엽록소(전구 색상용)

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        message_parts=['query:{0:s}'.format(parsed_path.query)]

        message='<br>'.join(message_parts)
        self.send_response(200) #응답코드
        self.end_headers() #헤더가 본문을 구분
        self.wfile.write(message.encode('utf-8'))

        print(u"[8082 port for chlorophyll START: Received GET for %s with query %s" % (self.path, parsed_path.query))
        
        global lightSetting
        lightSetting = LightSetting.LightSetting()

        global waterSetting
        waterSetting = WaterSetting.WaterSetting()
        
        if(self.path[2:9] == "goalLux"):
            #Query문이 ?goalLux='숫자'일 때
            s = self.path
            print(parse_qs(s[2:]))
            dict_a = parse_qs(s[2:])
            goalLux = int(dict_a["goalLux"][0])
            print(goalLux)

            readSettingFile(lightSetting, waterSetting)
            lightSetting.changeGoalLux2(goalLux)

            saveSettingAsFile(lightSetting, waterSetting)

            return None

        if(self.path[2:13] == "chlorophyll"):
            #Query문이 ?chlorophyll='A'일 때
            s = self.path
            print(parse_qs(s[2:]))
            dict_a = parse_qs(s[2:])
            chlorophyll = dict_a["chlorophyll"][0]
            print(chlorophyll)

            readSettingFile(lightSetting, waterSetting)
            lightSetting.changeChlorophyll2(chlorophyll)

            saveSettingAsFile(lightSetting, waterSetting)
            return None

        if(self.path[2:17] == "allowingOfAUser"):
            #Query문이 ?allowingOfAUser=true일 때
            s = self.path
            print(parse_qs(s[2:]))
            dict_a = parse_qs(s[2:])
            allowingOfAUser = (dict_a["allowingOfAUser"][0]) == 'true'
            print(allowingOfAUser)

            readSettingFile(lightSetting, waterSetting)
            lightSetting.changeAllowingOfAUser2(allowingOfAUser)

            saveSettingAsFile(lightSetting, waterSetting)
            return None
            
        return None


s = http.server.HTTPServer(('',8082),MyHandler)
s.serve_forever()
