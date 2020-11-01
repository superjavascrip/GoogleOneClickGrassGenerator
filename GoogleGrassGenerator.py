# coding:utf-8
import random


class GoogleGrassGenerator:
    def __init__(self):
        from googletrans import Translator
        LANGUAGES = [
            "af",
            "sq",
            "am",
            "ar",
            "hy",
            "az",
            "eu",
            "be",
            "bn",
            "bs",
            "bg",
            "ca",
            "ceb",
            "ny",
            "zh-cn",
            "zh-tw",
            "co",
            "hr",
            "cs",
            "da",
            "nl",
            "en",
            "eo",
            "et",
            "tl",
            "fi",
            "fr",
            "fy",
            "gl",
            "ka",
            "de",
            "el",
            "gu",
            "ht",
            "ha",
            "haw",
            "iw",
            "he",
            "hi",
            "hmn",
            "hu",
            "is",
            "ig",
            "id",
            "ga",
            "it",
            "ja",
            "jw",
            "kn",
            "kk",
            "km",
            "ko",
            "ku",
            "ky",
            "lo",
            "la",
            "lv",
            "lt",
            "lb",
            "mk",
            "mg",
            "ms",
            "ml",
            "mt",
            "mi",
            "mr",
            "mn",
            "my",
            "ne",
            "no",
            "or",
            "ps",
            "fa",
            "pl",
            "pt",
            "pa",
            "ro",
            "ru",
            "sm",
            "gd",
            "sr",
            "st",
            "sn",
            "sd",
            "si",
            "sk",
            "sl",
            "so",
            "es",
            "su",
            "sw",
            "sv",
            "tg",
            "ta",
            "te",
            "th",
            "tr",
            "uk",
            "ur",
            "ug",
            "uz",
            "vi",
            "cy",
            "xh",
            "yi",
            "yo",
            "zu",
        ]
        self.LANGUAGES = LANGUAGES
        self.translator = Translator(service_urls=[
            'translate.google.cn'
        ])
        self.NumberOfLanguages = (len(self.LANGUAGES) - 1)

    def getRandomGrass(self, OriginalText, frequency):
        Text = OriginalText
        list = []
        for i in range(frequency):
            if i != 0:
                RandomLanguage = self.LANGUAGES[random.randint(0, self.NumberOfLanguages)]
                list.append(RandomLanguage)
                Text = self.translator.translate(Text, dest=RandomLanguage, src=list[i - 1]).text
            elif i == 0:
                list.append(self.translator.detect(Text).lang)
                RandomLanguage = self.LANGUAGES[random.randint(0, self.NumberOfLanguages)]
                Text = self.translator.translate(Text, dest=RandomLanguage,
                                                 src=self.translator.detect(Text).lang).text
        return self.translator.translate(Text, dest="zh-cn", src=list[frequency - 1]).text

    def outputRandomGrassTxt(self, inputTxt, outputTxt, frequency):
        inputText = open(inputTxt, "r", encoding="utf-8").read()
        RandomGrass = self.getRandomGrass(inputText, frequency)
        open(outputTxt, "w+", encoding="utf-8").write(RandomGrass)
