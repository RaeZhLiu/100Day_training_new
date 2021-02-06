def main():
    num = int(input("Number of rows:"))
    # 定义空的二维数组
    yh = [[]] * num
    print("总行数", len(yh))

    for row in range(len(yh)):
        # 定义二维数组的行
        yh[row] = [None] * (row + 1)

        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col - 1] + yh[row - 1][col]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
