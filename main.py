import random
import os
import hangman_art
import hangman_words

# 清理屏幕的方法
def clear():
    os.system('cls')


# 随机选取单词
chosen_word = random.choice(hangman_words.word_list)
# 生成答案单词列表
display = ["_" for _ in range(len(chosen_word))]
# 显示游戏LOGO
print(hangman_art.logo)
# 用于测试
# print(f"the solution is {chosen_word}")

lives = 6
is_game_continue = True

while is_game_continue:
    guess = input("guess a letter: ").lower()
    # 每一回合情侣屏幕
    clear()

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess

    # 猜错情况 生命-1
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word")
    # 重复输入， 提示已经输入过一样的字母
    elif guess in display:
        print(f"{guess} is already in the word")

    # 显示单词回答情况
    print(display)
    # 显示游戏图片效果
    print(hangman_art.stages[lives])

    # 如果"_" 不在列表里，说明完成所有结果，游戏结束
    if "_" not in display:
        is_game_continue = False
        print("You win.")
    # 当生命 == 0 游戏结束
    elif lives == 0:
        is_game_continue = False
        print("You lose.")
