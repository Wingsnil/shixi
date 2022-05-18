import sys
import os
import os.path

from html.parser import HTMLParser


# 定义HTMLParser的子类,用以复写HTMLParser中的方法
class MyHTMLParser(HTMLParser):
    # 构造方法,定义data数组用来存储html中的数据
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = ''
        self.flag = False
        # self.index = 0

    # 覆盖starttag方法,可以进行一些打印操作
    def handle_starttag(self, tag, attrs):
        # pass
        # print("遇到起始标签:{} 开始处理:{}".format(tag, tag))
        # if tag == 'tr':
        #    self.index = 0
        if tag == 'div':
            for k, v in attrs:  # 遍历div的所有属性以及其值
                if k == 'class' and v == 'cell':  # 确定进入了<div class='cell'>
                    # self.index = self.index + 1
                    self.flag = True
                    self.data = self.data + '"'
                    return

    # 覆盖endtag方法
    def handle_endtag(self, tag):
        # pass
        # print("遇到结束标签:{} 开始处理:{}".format(tag, tag))
        if self.flag == True:
            self.data = self.data + '",'
            self.flag = False
            return
        # 遇到tr结束,增加一个回车
        if tag == 'tr':
            self.data = self.data + '\n'

    # 覆盖handle_data方法,用来处理获取的html数据,这里保存在data数组
    def handle_data(self, data):
        # pass
        # print("遇到数据:{} 开始处理:{}".format(data, data))
        if (self.flag == True):
            data = data.replace('\n', '')  # 替换字段中的回车
            data = data.replace('  ', '')  # 替换字段中的连续两个空格
            self.data = self.data + data


def read_file(filename):
    fp = open(filename, 'r', encoding='utf-8')
    content = fp.read()
    fp.close()
    return content


def write_file(filename, content):
    fp = open(filename, 'a+', encoding='utf-8')
    fp.write(content)
    fp.close()


def main():
    csv_file = 'xinguanyiqing.csv'
    write_file(csv_file, '"地区","新增","现有","累计","治愈","死亡"\n')

    parser = MyHTMLParser()
        html_file = './123.html'
        print(html_file)
        content = read_file(html_file)
        parser.feed(content)
        # 对解析后的数据进行相应操作
        write_file(csv_file, parser.data)
        parser.close()


main()