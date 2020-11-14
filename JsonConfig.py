# coding:utf-8
import json
import os

'''
Copyright Github@superjavascrip Bilibili@兰格如同
Version : 4.0
'''


class JsonConfig(object):
    def __init__(self, ConfigFileName):
        self.ConfigFileDir = "Config" + "/" + ConfigFileName + ".json"
        return

    def NewConfig(self, configList, configName):
        config = open(self.ConfigFileDir, "r+").read()
        json_dict = json.loads(config)
        json_dict[configName] = configList
        open(self.ConfigFileDir, "w+").write(json.dumps(json_dict, sort_keys=True, indent=4, separators=(',', ': ')))

    def RemoveConfig(self, configName):
        config = open(self.ConfigFileDir, "r+").read()
        json_dict = json.loads(config)
        if configName in json_dict:
            json_dict.pop(configName)
        else:
            print("没有此config，请检查输入是否正确。")

    def ReturnConfig(self, configName):
        config = open(self.ConfigFileDir, "r+").read()
        config_dict = json.loads(config)
        return config_dict[configName]

    def ImportConfig(self, configFile):
        if os.path.exists(configFile) and os.path.isfile(configFile) and configFile.endswith(".json"):
            config = open(configFile, "r+").read()
            json_dict = json.loads(config)
            for k in json_dict:
                self.NewConfig(json_dict[k], k)
        else:
            print("没有此文件或文件后缀名错误")

    def ExportConfig(self, configNameList, configFileName):
        configFileName = configFileName + ".json"
        exportConfigFile = open("ExportConfig/{}".format(configFileName), "w+")
        config = open(self.ConfigFileDir, "r+").read()
        config_dict = json.loads(config)
        export_config_dict = {}
        if len(configNameList) == 1:
            for v in configNameList:
                export_config_dict[v] = config_dict[v]
        exportConfigFile.write(json.dumps(export_config_dict, sort_keys=True, indent=4, separators=(',', ': ')))
