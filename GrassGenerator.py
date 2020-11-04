# coding:utf-8
import os
import sys

import GoogleGrassGenerator as GoogleGrassGenerator
import argparse

'''
Copyright Github@superjavascrip Bilibili@兰格如同
Version : 2.0
'''
GoogleGrassGenerator = GoogleGrassGenerator.GoogleGrassGenerator()
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="输入需要生草的txt文件(不输入进入交互翻译模式)", type=str)
parser.add_argument("-o", help="输出的txt文件名(默认output.txt)", type=str, default="output.txt")
parser.add_argument("-f", help="需要生草的次数(默认20次)", type=int, default=20)
args = parser.parse_args()
if args.i is None:
    input_text = input("请输入需要生草的文字")
    input_frequency = input("请输入需要生草的次数")
    if input_text is None or input_text == "":
        print("请输入文字！！！")
        sys.exit(0)
    if input_frequency is None or input_frequency == "":
        input_frequency = 20
    print(GoogleGrassGenerator.getRandomGrass(input_text, int(input_frequency)))
elif args.i is not None:
    GoogleGrassGenerator.outputRandomGrassTxt(args.i, args.o, args.f)
