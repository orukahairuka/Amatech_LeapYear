# 閏年を判定するプログラム

# ユーザーに西暦年を入力してもらう
year = int(input("西暦年を入力してください: "))

# 閏年の条件をチェック
if year % 4 == 0:  # 4で割り切れるか？
    if year % 100 == 0:  # 100で割り切れるか？
        if year % 400 == 0:  # 400で割り切れるか？
            print(f"{year}年は閏年です。")
        else:
            print(f"{year}年は閏年ではありません。")
    else:
        print(f"{year}年は閏年です。")
else:
    print(f"{year}年は閏年ではありません。")
