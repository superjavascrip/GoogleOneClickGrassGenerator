# coding:utf-8

import sys

import GoogleGrassGenerator as GoogleGrassGenerator
import argparse

'''
Copyright Github@superjavascrip Bilibili@兰格如同
Version : 4.0
'''
GoogleGrassGenerator = GoogleGrassGenerator.GoogleGrassGenerator("Config")
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="输入需要生草的txt文件(不输入进入交互翻译模式)", type=str)
parser.add_argument("-o", help="输出的txt文件名(默认output.txt)", type=str, default="output.txt")
parser.add_argument("-f", help="需要生草的次数(默认20次)", type=int, default=20)
parser.add_argument("-c", help="使用的config(有此属性-f属性会变成使用几次config翻译)", type=str)
args = parser.parse_args()
if args.i is None:
    input_text = input("请输入需要生草的文字")
    input_frequency = input("请输入需要生草的次数")
    input_config = input("使用哪个config文件(/Config/目录下，不输入不使用，输入后次数变为使用config文件的次数)")
    if input_text is None or input_text == "":
        print("请输入文字！！！")
        sys.exit(0)
    if input_frequency is None or input_frequency == "":
        input_frequency = 20
    if input_config is None or input_config == "":
        print(GoogleGrassGenerator.getRandomGrass(input_text, int(input_frequency)))
    elif input_config is not None or input_config != "":
        print(None)
elif args.i is not None:
    if args.c is not None or args.c != "":
        GoogleGrassGenerator.outputRandomGrassTxt(args.i, args.o, args.f)
    else:
        GoogleGrassGenerator.outputConfigGrass(args.i, args.o, args.f, args.c)
