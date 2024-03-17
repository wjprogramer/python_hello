# This is a sample Python script.
import random
from collections import deque

# `import` intro: https://docs.python.org/zh-tw/3.12/tutorial/modules.html
from src.sample_1 import hello_world


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def foo_1(foo1=5):
    print(foo1)


# 費式數列
def fibonacci(nn):
    aa, b = 0, 1  # 多重賦值
    print('Fibonacci:', end=' ')
    while aa < nn:
        print(aa, end=' ')
        aa, b = b, aa + b  # 示範了等號的右項運算 (expression) 會先被計算 (evaluate)，賦值再發生。右項的運算式由左至右依序被計算。
    print()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    hello_world('PyCharm')

    # Number -----------------------------------------------------------------------------------------------------------
    num1 = 7 ** 3  # 343
    num2 = -3 ** 2  # -(3**2) = -9

    # String -----------------------------------------------------------------------------------------------------------
    str1 = r'C:\some\name'
    str2 = 10 * '*' + '=' 'x'
    str3 = 'xxx'[0] + 'xxx'[-2]
    len('Python')  # Length of a string
    segment_long_text = ('Put several strings within parentheses '
                         'to have them joined together.')

    ## Slicing 切片
    str4 = 'Python'[0:2]  # 'Py'
    str5 = 'Python'[2:5]  # 'tho'
    str6 = 'Python'[:2]  # 'Py'
    str7 = 'Python'[2:]  # 'thon

    # List -------------------------------------------------------------------------------------------------------------
    squares = [1, 4, 9, 16, 25]
    list_elem1 = squares[0]  # 1
    list_elem2 = squares[-1]  # 25
    list_slicing_1 = squares[-3:]  # [9, 16, 25]
    list_1 = [1, 2, 3] + [4, 5, 6]  # [1, 2, 3, 4, 5, 6]
    list_1.append(7)
    list_1.insert(1, 99)
    len(list_1)
    list_nested = [1, 2, 3, [4, 5, 6]]
    list_nested_elem = list_nested[3][0]  # 4
    ## Other methods: list.remove(), list.pop(), list.clear(), list.index(), list.count(), list.sort(), list.reverse()

    ## Reference
    rgb = ['red', 'green', 'blue']
    rgba = rgb
    rgb_is_same = id(rgb) == id(rgba)  # True

    ## Reference 2
    list_2 = list_1[:]  # `Slicing` creates a new list (ref is different)

    ## Slice
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']  # replace some values
    ### result: ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    letters[2:5] = []  # now remove them
    ### result: ['a', 'b', 'f', 'g']
    letters[:] = []  # clear the list by replacing all the elements with an empty list
    ### result: []

    ## Queue
    queue_1 = deque(["Eric", "John", "Michael"])
    queue_1.append("Terry")  # Terry arrives
    queue_1.append("Graham")  # Graham arrives
    queue_1.popleft()  # The first to arrive now leaves
    ### result: 'Eric'
    queue_1.popleft()  # The second to arrive now leaves
    ### result: 'John'
    ### queue_1: deque(['Michael', 'Terry', 'Graham'])  # Remaining queue in order of arrival

    ## List Comprehensions（串列綜合運算）
    squares_1 = list(map(lambda x: x ** 2, range(10)))
    squares_2 = [x ** 2 for x in range(10)]

    ## del
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    ### result: [1, 66.25, 333, 333, 1234.5]
    del a[2:4]
    ### result: [1, 66.25, 1234.5]
    del a[:]
    ### result: []
    del a  # del 也可以用來刪除整個變數

    # For Loop ---------------------------------------------------------------------------------------------------------
    ## range
    print('range:', end=' ')
    for i in range(5):
        print(i, end=' ')  # 0 1 2 3 4

    list(range(5, 10))  # [5, 6, 7, 8, 9]
    list(range(0, 10, 3))  # [0, 3, 6, 9]
    list(range(-10, -100, -30))  # [-10, -40, -70]
    sum(range(4))  # 0 + 1 + 2 + 3 = 6

    ## List & For loop
    for letter in letters:
        len(letter)

    range_and_list_1 = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(range_and_list_1)):
        print(i, range_and_list_1[i])  # 0 Mary, 1 had, 2 a, 3 little, 4 lamb

    ## continue & break in for loop
    for n in range(2, 10):
        for xx in range(2, n):
            if n % xx == 0:
                print(n, 'equals', xx, '*', n // xx)
                break
        else:  # 注意這個 else 是屬於 for 迴圈的，而不是 if 的
            # loop fell through without finding a factor
            print(n, 'is a prime number')

    ### result:
    ###     2 is a prime number
    ###     3 is a prime number
    ###     4 equals 2 * 2
    ###     5 is a prime number
    ###     6 equals 2 * 3
    ###     7 is a prime number
    ###     8 equals 2 * 4
    ###     9 equals 3 * 3

    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)

    ## pass (三種使用的情境)

    ### 陳述式不執行任何動作。它可用在語法上需要一個陳述式但程式不需要執行任何動作的時候
    ### while True:
    ###     pass # Busy-wait for keyboard interrupt (Ctrl+C)

    ### 經常用於建立簡單的 class
    class MyEmptyClass:
        pass

    ### 亦可作為一個函式或條件判斷主體的預留位置，在你撰寫新的程式碼時讓你保持在更抽象的思維層次。pass 會直接被忽略：
    def initlog():
        pass  # Remember to implement this!


    # While loop -------------------------------------------------------------------------------------------------------
    fibonacci(10)

    # Flow Control -----------------------------------------------------------------------------------------------------
    flow_control_num = random.randrange(0, 10, 2)  # 0, 2, 4, 6, 8
    if flow_control_num <= 4:
        print('flow_control_num <= 4')
    elif flow_control_num <= 6:
        print('flow_control_num <= 6')
    else:
        print('flow_control_num > 6')

    # Dictionary -------------------------------------------------------------------------------------------------------
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  # {'sape': 4139, 'guido': 4127, 'jack': 4098}
    dict(sape=4139, guido=4127, jack=4098)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}
    dict_1 = {x: x ** 2 for x in (2, 4, 6)}  # {2: 4, 4: 16, 6: 36}

    ## 在疊代一個集合的同時修改該集合的內容，很難獲取想要的結果。比較直觀的替代方式，是疊代該集合的副本，或建立一個新的集合
    ### Strategy 1:  Iterate over a copy
    dict_users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    for user, status in dict_users.copy().items():
        if status == 'inactive':
            del dict_users[user]
    ### Strategy 2:  Create a new collection
    active_users = {}
    for user, status in dict_users.items():
        if status == 'active':
            active_users[user] = status

    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
    ### 0 tic
    ### 1 tac
    ### 2 toe

    ## 要同時對兩個以上的序列作迴圈，可以將其以成對的方式放入 zip() 函式：
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))
    ### What is your name?  It is lancelot.
    ### What is your quest?  It is the holy grail.
    ### What is your favorite color?  It is blue.

    for i in reversed(range(1, 10, 2)):
        print(i)

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for i in sorted(basket):  # 不會改變原本的序列
        print(i)
    for f in sorted(set(basket)):  # 使用 set() 來移除重複的元素
        print(f)

    # match (其他語言通常會稱 switch) & case ------------------------------------------------------------------------------
    def http_error(res_status):
        match res_status:
            case 400:
                return "Bad request"
            case 404:
                return "Not found"
            case 418:
                return "I'm a teapot"
            case 401 | 403 | 404:
                return "Not allowed"
            case _:
                return "Something's wrong with the internet"


    # 模式可以看起來像是拆解賦值 (unpacking assignment)，且可以用來連結變數：
    point = (1, 2)
    match point:
        case (0, 0):
            print("Origin")
        case (0, yValue):
            print(f"Y={yValue}")
        case (xx, 0):
            print(f"X={xx}")
        case (xx, yValue):
            print(f"X={xx}, Y={yValue}")
        case _:
            raise ValueError("Not a point")

    # 如果你要用 class 來結構化你的資料，你可以使用該 class 的名稱加上一個引數列表，類似一個建構式 (constructor)，
    # 但它能夠將屬性擷取到變數中：
    def where_is(p):
        match p:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=yValue2):
                print(f"Y={yValue2}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Somewhere else")
            case _:
                print("Not a point")

    # 以下的模式都是等價的
    Point(1, 2)
    Point(1, y=2)
    Point(x=1, y=2)
    Point(y=2, x=1)

    # Lambda -----------------------------------------------------------------------------------------------------------
    def make_increment(nnn):
        return lambda x: x + nnn


    f = make_increment(42)
    f(0)

    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    # result: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

    # Tuples & 序列 (Sequences) -----------------------------------------------------------------------------------------
    tuple1 = 12345, 54321, 'hello!'
    # tuple1[0] = 88888  # tuples are immutable
    print(tuple1[0])  # 12345
    nested_tuple_1 = tuple1, (1, 2, 3, 4, 5)
    tuple_2 = ([1, 2, 3], [4, 5, 6])  # but they can contain mutable objects
    tuple_elem1, tuple_elem2, tuple_elem3 = tuple1  # 序列拆解 sequence unpacking

    # Sets 集合 ---------------------------------------------------------------------------------------------------------
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print('orange' in basket)  # True
    set_1 = set('abracadabra')  # {'a', 'r', 'b', 'c', 'd'} (unique letters in set_1)
    set_2 = set('alacazam')  # {'a', 'l', 'm', 'c', 'z'} (unique letters in set_2)
    print(set_1 - set_2)  # letters in set_1 but not in set_2, result: {'r', 'b', 'd'}
    print(set_1 | set_2)  # letters in set_1 or set_2, result: {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    print(set_1 & set_2)  # letters in both set_1 and set_2, result: {'a', 'c'}
    print(set_1 ^ set_2)  # letters in set_1 or set_2 but not both, result: {'r', 'd', 'b', 'm', 'z', 'l'}


# region function arguments --------------------------------------------------------------------------------------------
# standard arguments
# ex: standard_arg(2)
# ex: standard_arg(arg=2)
def standard_arg(arg):
    print(arg)


# only positional arguments
# ex: pos_only_arg(3)
# cannot: pos_only_arg(arg=1)
def pos_only_arg(arg, /):
    print(arg)


# only keyword arguments
# ex: kwd_only_arg(arg=3)
# cannot: kwd_only_arg(1)
def kwd_only_arg(*, arg):
    print(arg)


# ex: combined_example(1, 2, kwd_only=3)
# ex: combined_example(1, standard=2, kwd_only=3)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# 任意引數列表 (Arbitrary Argument Lists)
def concat(*args, sep="/"):
    return sep.join(args)
# endregion


# region Documentation -------------------------------------------------------------------------------------------------
# 說明文件字串 (Documentation Strings)
def documentation_strings_demo():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    print(documentation_strings_demo.__doc__)  # 可以顯示 docstring: Do nothing, but document it. No, really, ...
    pass
# endregion
