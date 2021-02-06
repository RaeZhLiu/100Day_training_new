import re


def main():
    sentence = "你丫是傻叉吗? 我操你大爷的. Fuck you."
    pattern = re.compile(r'[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', flags=re.IGNORECASE)
    purified = pattern.sub('*', sentence)

    print(purified)


if __name__ == '__main__':
    main()
