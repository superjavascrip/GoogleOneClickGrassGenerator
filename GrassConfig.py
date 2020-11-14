import argparse

import JsonConfig as JsonConfig

'''
Copyright Github@superjavascrip Bilibili@兰格如同
Version : 4.0
'''

parser = argparse.ArgumentParser()
parser.add_argument("-r", help="要删除的config", type=str)
parser.add_argument("-a", help="要添加的config(必须是json文件)", type=str)
parser.add_argument("-e", help="要导出的config(多个用\",\"隔开)", type=str)
parser.add_argument("-n", help="要导出的config名字(默认ExportConfig.json)", type=str, default="ExportConfig.json")
args = parser.parse_args()
JsonConfig = JsonConfig.JsonConfig("Config")
if args.r is not None:
    JsonConfig.RemoveConfig(args.r)
if args.a is not None:
    JsonConfig.ImportConfig(args.a)
if args.e is not None:
    if "," in args.e:
        config_list = args.e.split(",")
        JsonConfig.ExportConfig(config_list, args.n)
    else:
        config_list = []
        config_list.append(args.e)
        JsonConfig.ExportConfig(config_list, args.n)
