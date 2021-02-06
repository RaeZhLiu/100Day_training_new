"""
移动号段：
134 135 136 137 138 139 147 148 150 151 152 157 158 159 172 178 182 183 184 187 188 195 198
联通号段：
130 131 132 145 146 155 156 166 167 171 175 176 185 186 196
电信号段：
133 149 153 173 174 177 180 181 189 191 193 199
虚拟运营商:
162 165 167 170 171

要求：从一段文字中提取出国内手机号码
"""
import re


def extract():
    # 将正则表达式编译为一个Pattern对象
    pattern = re.compile(r'(?<=\D)(13[4-9]\d{8}|14[78]\d{8}|15[0-27-9]\d{8}|17[28]\d{8}|18[2-47-8]\d{8}\d{8}|19[58]\d{8})(?=\D)')
    sentence = "重要的事情说8130123456789遍，我的手机号是17860631401这个靓号，" \
               "不是15600998765，也是110或119，王大锤的手机号才是15800998765。"

    mylist = pattern.findall(sentence)
    print(mylist)
    print("============分隔线==============")
    for tmp in pattern.finditer(sentence):
        print(tmp.group())
    print("============分隔线==============")

    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, pos=m.end())
    # print("============分隔线==============")
    # match方法是匹配头部，如果从指定位置开始就不符合则返回None
    # m1 = pattern.match(sentence)
    # while m1:
    #     print(m1.group())
    #     m1 = pattern.match(sentence, pos=m1.end())


if __name__ == '__main__':
    extract()
