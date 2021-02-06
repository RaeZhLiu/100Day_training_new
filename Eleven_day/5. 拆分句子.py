import re


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月， 低头思故乡。'
    pattern = re.compile(r'[,.，。]')
    response_list = pattern.split(poem)
    while '' in response_list:
        response_list.remove('')

    for only in response_list:
        print(only)
    print(response_list)


if __name__ == '__main__':
    main()
