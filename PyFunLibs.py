#!/usr/bin/env python
"""
SuperLib Ultimate Complete - 全功能整合版

功能模块：
    1. 随机数生成（基于线性同余算法）
    2. 长度检测（内置 len）
    3. 数学运算（加、减、乘、除、幂、平方根、阶乘、正弦、余弦，正弦余弦使用泰勒级数展开）
    4. 字符串相似度比较（Levenshtein 编辑距离及相似度比率）
    5. 多种排序算法：
         - 冒泡排序、快速排序、插入排序、选择排序、归并排序、
           堆排序、希尔排序、计数排序、基数排序、侏儒排序、梳排序
         - **新增：交换算法（列表逆序）**
    6. 彩色输出（利用 ANSI 转义码实现彩色文本）
    7. 系统信息获取：
         - HWID（基于当前工作目录、平台和 Python 版本生成简易标识）
         - Cookies（模拟返回固定字符串）
    8. 延迟函数（忙等待实现）
    9. CMD 命令行界面：通过菜单测试各项功能
    10. **新增扩展功能**：
         - \nt 为换行并空格
         - %winver 为读取 Windows 版本
         - %verx 为读取 Windows 版本位数
         - %getc: 读取指定盘符（如 C:）的剩余空间（单位 G）
         - %getfps: 读取 FPS 帧率
         - printf("") 更好的输出函数（会自动替换上述标记）
         - **新增宏支持：使用 "$" 开头的宏进行替换，可通过 define_macro 定义自定义宏**
         
新增扩展功能部分允许调用内置模块 re、platform 与 ctypes。
"""
#==============================================================================================#
'''English'''
'''SuperLib Ultimate Complete – Main Features

Random Number Generation

Uses a Linear Congruential Generator (LCG) to produce pseudo-random numbers.

Provides functions to generate a random float between 0 and 1 and random integers within a specified range.

Length Check

Offers a simple function to check the length of strings, lists, or any object using Python’s built-in len function.

Mathematical Operations

Basic arithmetic: addition, subtraction, multiplication, and division.

Advanced operations: exponentiation, square root, factorial, sine, and cosine (the latter two implemented with Taylor series approximations).

String Similarity Comparison

Implements the Levenshtein distance algorithm to compare two strings.

Provides a similarity ratio function based on the edit distance.

Sorting Algorithms

Contains various sorting methods including:

Bubble Sort, Quick Sort, Insertion Sort, Selection Sort, Merge Sort, Heap Sort, Shell Sort, Counting Sort, Radix Sort, Gnome Sort, and Comb Sort.

Additional “Swap” Algorithm: A reverse (swap) function that reverses the order of elements in a list (e.g., turns [1,2,3,4,5,6,7] into [7,6,5,4,3,2,1]).

Colorful Output

Uses ANSI escape codes to display colored text in the terminal.

System Information Retrieval

Provides a method to generate a simple HWID based on the current working directory, platform, and Python version.

Simulates cookie retrieval by returning a fixed string.

Delay Function

Implements a busy-waiting delay function (with limited precision) for timing purposes.

Command-Line Interface (CMD)

Offers an interactive menu to test and demonstrate all the library’s functionalities.

Extended Features with Special Markers

Supports special markers in strings for dynamic content replacement:

\nt converts to a newline followed by a space.

%winver is replaced with the Windows version.

%verx is replaced with the Windows architecture (32-bit or 64-bit).

%getc: followed by a drive letter (e.g., %getc:C:) returns the free disk space (in gigabytes) of that drive.

%getfps: is replaced with a placeholder FPS value (e.g., 60).

An enhanced printf() function processes these markers before printing.

Macro Support

Allows the definition of macros that start with the $ symbol.

Built-in macros (like $winver, $verx, $getfps, etc.) are available, and users can define custom macros using the define_macro() function.

These macros are automatically replaced in strings processed by the enhanced printf().

English Translation of the Library's Content:

SuperLib Ultimate Complete is an extensive and self-contained library implemented in Python that provides a wide range of functionalities without relying on external packages (except for a few built-in modules such as sys, os, re, platform, and ctypes). The library includes:

Random Number Generation:
Using a Linear Congruential Generator, it can produce both floating-point numbers (between 0 and 1) and integers within a specified range.

Length Checking:
A simple function is available to determine the length of any object that supports the len function.

Mathematical Operations:
The library supports basic arithmetic operations as well as advanced calculations like exponentiation, square roots, factorials, and trigonometric functions (sine and cosine, calculated using Taylor series).

String Similarity:
It features an implementation of the Levenshtein distance algorithm to measure how similar two strings are, and computes a similarity ratio based on this distance.

Sorting Algorithms:
Multiple sorting techniques are implemented, including Bubble, Quick, Insertion, Selection, Merge, Heap, Shell, Counting, Radix, Gnome, and Comb Sorts. In addition, a reverse (swap) algorithm is provided to reverse the order of elements in a list.

Colorful Terminal Output:
ANSI escape codes are used to produce colored text output for enhanced terminal display.

System Information:
The library can generate a simple hardware ID (HWID) from the current directory, operating system, and Python version, and simulates retrieving cookies by returning a preset string.

Delay Function:
A busy-waiting delay function is available for simple timing tasks.

Command-Line Interface (CMD):
An interactive menu allows users to test and experience each of the library's functions.

Extended Features and Macro Support:
The library can replace special markers within strings (e.g., markers for newline with space, Windows version, system architecture, disk free space, FPS value) through an enhanced printf() function. It also supports user-defined macros that begin with the $ character, allowing dynamic text substitution within output strings.

This comprehensive library is ideal for educational purposes and demonstrations, offering a variety of algorithms and techniques all contained within a single, self-sufficient Python module.'''

import sys
import os

# =======================
# 彩色输出功能
# =======================
class ColorOutput:
    COLORS = {
        'reset': "\033[0m",
        'red': "\033[31m",
        'green': "\033[32m",
        'yellow': "\033[33m",
        'blue': "\033[34m",
        'magenta': "\033[35m",
        'cyan': "\033[36m",
        'white': "\033[37m",
        'bold': "\033[1m"
    }
    
    @staticmethod
    def colored_text(text, color):
        color_code = ColorOutput.COLORS.get(color.lower(), ColorOutput.COLORS['reset'])
        return f"{color_code}{text}{ColorOutput.COLORS['reset']}"
    
    @staticmethod
    def print_colored(text, color):
        sys.stdout.write(ColorOutput.colored_text(text, color) + "\n")
        sys.stdout.flush()

# =======================
# 系统信息获取
# =======================
class SystemInfo:
    @staticmethod
    def get_hwid():
        """
        获取简易硬件标识：利用当前工作目录、系统平台和 Python 版本生成一个简单哈希值（仅作示例）
        """
        info = os.getcwd() + os.sep + sys.platform + sys.version
        hwid = 0
        for ch in info:
            hwid = (hwid * 31 + ord(ch)) & 0xFFFFFFFF
        return hex(hwid)
    
    @staticmethod
    def get_cookies():
        """
        模拟获取 Cookies 信息（由于只允许使用 sys 与 os，无网络支持，此处返回固定字符串）
        """
        return "cookie1=value1; cookie2=value2;"

# =======================
# 随机数生成（基于线性同余算法）
# =======================
class RandomGenerator:
    def __init__(self, seed=None):
        if seed is None:
            # 使用 os.urandom 随机生成一个初始种子
            seed = int.from_bytes(os.urandom(4), 'little')
        self.seed = seed

    def random(self):
        """
        返回 0~1 之间的伪随机浮点数
        常数：a=1103515245, c=12345, m=2^31
        """
        self.seed = (1103515245 * self.seed + 12345) & 0x7FFFFFFF
        return self.seed / 0x80000000

    def randint(self, a, b):
        """
        返回 [a, b] 范围内的随机整数
        """
        return a + int(self.random() * (b - a + 1))

# =======================
# 长度检测函数
# =======================
def check_length(x):
    return len(x)

# =======================
# 数学运算（Calculator）
# =======================
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b

    @staticmethod
    def power(a, b):
        result = 1
        for _ in range(b):
            result *= a
        return result

    @staticmethod
    def sqrt(x, tolerance=1e-10):
        if x < 0:
            raise ValueError("负数无平方根")
        guess = x if x != 0 else 1
        while abs(guess * guess - x) > tolerance:
            guess = (guess + x / guess) / 2
        return guess

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("负数没有阶乘")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def sin(x, terms=10):
        result = 0
        for n in range(terms):
            power_term = Calculator.power(x, 2 * n + 1)
            fact = Calculator.factorial(2 * n + 1)
            term = power_term / fact
            if n % 2 == 1:
                term = -term
            result += term
        return result

    @staticmethod
    def cos(x, terms=10):
        result = 0
        for n in range(terms):
            power_term = Calculator.power(x, 2 * n)
            fact = Calculator.factorial(2 * n)
            term = power_term / fact
            if n % 2 == 1:
                term = -term
            result += term
        return result

# =======================
# 字符串相似度比较
# =======================
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + cost)
    return dp[m][n]

def similarity_ratio(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 1.0
    dist = levenshtein_distance(s1, s2)
    return 1 - dist / max(len(s1), len(s2))

# =======================
# 各种排序算法（Sorter）
# =======================
class Sorter:
    @staticmethod
    def bubble(arr):
        n = len(arr)
        sorted_arr = arr[:]
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_arr[j] > sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
        return sorted_arr

    @staticmethod
    def quick(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return Sorter.quick(less) + [pivot] + Sorter.quick(greater)

    @staticmethod
    def insertion(arr):
        sorted_arr = arr[:]
        for i in range(1, len(sorted_arr)):
            key = sorted_arr[i]
            j = i - 1
            while j >= 0 and sorted_arr[j] > key:
                sorted_arr[j + 1] = sorted_arr[j]
                j -= 1
            sorted_arr[j + 1] = key
        return sorted_arr

    @staticmethod
    def selection(arr):
        sorted_arr = arr[:]
        n = len(sorted_arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if sorted_arr[j] < sorted_arr[min_index]:
                    min_index = j
            sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]
        return sorted_arr

    @staticmethod
    def merge(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = Sorter.merge(arr[:mid])
        right = Sorter.merge(arr[mid:])
        return Sorter._merge(left, right)

    @staticmethod
    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def heap(arr):
        sorted_arr = arr[:]
        n = len(sorted_arr)
        for i in range(n // 2 - 1, -1, -1):
            Sorter._heapify(sorted_arr, n, i)
        for i in range(n - 1, 0, -1):
            sorted_arr[0], sorted_arr[i] = sorted_arr[i], sorted_arr[0]
            Sorter._heapify(sorted_arr, i, 0)
        return sorted_arr

    @staticmethod
    def _heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Sorter._heapify(arr, n, largest)

    @staticmethod
    def shell(arr):
        sorted_arr = arr[:]
        n = len(sorted_arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = sorted_arr[i]
                j = i
                while j >= gap and sorted_arr[j - gap] > temp:
                    sorted_arr[j] = sorted_arr[j - gap]
                    j -= gap
                sorted_arr[j] = temp
            gap //= 2
        return sorted_arr

    @staticmethod
    def counting(arr):
        if not arr:
            return []
        max_val = max(arr)
        count = [0] * (max_val + 1)
        for num in arr:
            count[num] += 1
        result = []
        for i, c in enumerate(count):
            result.extend([i] * c)
        return result

    @staticmethod
    def radix(arr):
        if not arr:
            return []
        max_val = max(arr)
        exp = 1
        result = arr[:]
        while max_val // exp > 0:
            result = Sorter._counting_sort_radix(result, exp)
            exp *= 10
        return result

    @staticmethod
    def _counting_sort_radix(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        return output

    @staticmethod
    def gnome(arr):
        sorted_arr = arr[:]
        i = 0
        while i < len(sorted_arr):
            if i == 0 or sorted_arr[i] >= sorted_arr[i - 1]:
                i += 1
            else:
                sorted_arr[i], sorted_arr[i - 1] = sorted_arr[i - 1], sorted_arr[i]
                i -= 1
        return sorted_arr

    @staticmethod
    def comb(arr):
        sorted_arr = arr[:]
        gap = len(sorted_arr)
        shrink = 1.3
        sorted_flag = False
        while not sorted_flag:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_flag = True
            i = 0
            while i + gap < len(sorted_arr):
                if sorted_arr[i] > sorted_arr[i + gap]:
                    sorted_arr[i], sorted_arr[i + gap] = sorted_arr[i + gap], sorted_arr[i]
                    sorted_flag = False
                i += 1
        return sorted_arr

    # =======================
    # 新增：交换算法（列表逆序）
    # =======================
    @staticmethod
    def reverse(arr):
        """
        将列表中的元素顺序反转，不删除原有代码
        例如: [1, 2, 3, 4, 5, 6, 7] 交换后返回 [7, 6, 5, 4, 3, 2, 1]
        """
        reversed_arr = arr[:]
        left, right = 0, len(reversed_arr) - 1
        while left < right:
            reversed_arr[left], reversed_arr[right] = reversed_arr[right], reversed_arr[left]
            left += 1
            right -= 1
        return reversed_arr

# =======================
# 延迟函数（忙等待实现）
# =======================
def delay(seconds):
    iterations = int(seconds * 10**7)
    dummy = 0
    for _ in range(iterations):
        dummy += 1

# =======================
# 输入/输出封装
# =======================
def output(message):
    sys.stdout.write(str(message) + "\n")
    sys.stdout.flush()

def user_input(prompt=""):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.readline().strip()

# =======================
# CMD 命令行界面 - 排序测试
# =======================
def cmd_sorting():
    output("欢迎进入排序命令行界面！")
    sorting_methods = {
        '1': ('冒泡排序', Sorter.bubble),
        '2': ('快速排序', Sorter.quick),
        '3': ('插入排序', Sorter.insertion),
        '4': ('选择排序', Sorter.selection),
        '5': ('归并排序', Sorter.merge),
        '6': ('堆排序', Sorter.heap),
        '7': ('希尔排序', Sorter.shell),
        '8': ('计数排序', Sorter.counting),
        '9': ('基数排序', Sorter.radix),
        '10': ('侏儒排序', Sorter.gnome),
        '11': ('梳排序', Sorter.comb),
        '12': ('交换算法(列表逆序)', Sorter.reverse)
    }
    output("请选择排序算法：")
    for key in sorted(sorting_methods.keys(), key=lambda x: int(x)):
        output(f"{key}. {sorting_methods[key][0]}")
    choice = user_input("请输入选项编号：")
    if choice not in sorting_methods:
        output("无效选择，退出排序命令行。")
        return
    method_name, method_func = sorting_methods[choice]
    output(f"你选择了：{method_name}")
    arr_str = user_input("请输入一组数字（以空格分隔）：")
    try:
        arr = [int(x) for x in arr_str.split()]
    except:
        output("输入格式错误，必须为数字。")
        return
    sorted_arr = method_func(arr)
    output("排序前数组：" + str(arr))
    output("排序后数组：" + str(sorted_arr))

# =======================
# 新扩展功能：新命令标记解析及 printf 改进
# =======================
import re
import platform
import ctypes

def get_winver():
    """
    返回 Windows 系统版本，如果非 Windows 则返回 '非Windows'
    """
    if sys.platform.startswith("win"):
        ver, csd, ptype, build = platform.win32_ver()
        return ver if ver else "未知"
    return "非Windows"

def get_verx():
    """
    返回 Windows 系统位数，如 '64bit' 或 '32bit'，非 Windows 时返回空字符串
    """
    if sys.platform.startswith("win"):
        arch, _ = platform.architecture()
        return arch
    return ""

def getc(drive="C:"):
    """
    读取指定盘符的剩余空间（单位：G），仅适用于 Windows 系统
    """
    if not sys.platform.startswith("win"):
        return "仅限Windows"
    free_bytes = ctypes.c_ulonglong(0)
    total_bytes = ctypes.c_ulonglong(0)
    total_free_bytes = ctypes.c_ulonglong(0)
    ret = ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive), ctypes.byref(free_bytes), ctypes.byref(total_bytes), ctypes.byref(total_free_bytes))
    if ret == 0:
        return "未知"
    else:
        return f"{free_bytes.value / (1024**3):.2f}G"

def get_fps():
    """
    返回 FPS 帧率，占位值（例如 60）
    """
    return 60

def printf(format_string):
    """
    改进版输出函数，对输入字符串中的特殊标记进行替换：
      - \nt 替换为换行并加空格
      - %winver 替换为 Windows 版本
      - %verx 替换为 Windows 位数
      - %getfps: 替换为 FPS 帧率
      - %getc:后跟盘符（如 %getc:C:）替换为该盘剩余空间
      - **新增：支持以 "$" 开头的宏替换，可通过 define_macro 定义或使用内置宏**
    替换完成后调用原有 output 函数输出结果
    """
    result = format_string
    # 替换 \nt 为换行加空格
    result = result.replace(r"\nt", "\n ")
    # 替换 %winver
    result = result.replace("%winver", get_winver())
    # 替换 %verx
    result = result.replace("%verx", get_verx())
    # 替换 %getfps:
    result = result.replace("%getfps:", str(get_fps()))
    # 替换 %getc: 后跟盘符，如 %getc:C:
    def replace_getc(match):
        drive = match.group(1)
        return getc(drive)
    result = re.sub(r"%getc:([A-Za-z]:)", replace_getc, result)
    
    # ---------------------------
    # 新增宏替换：以 "$" 开头的宏
    # ---------------------------
    # 全局宏字典（预设内置宏）
    global _macros
    try:
        _macros
    except NameError:
        _macros = {
            "winver": get_winver(),
            "verx": get_verx(),
            "getfps": str(get_fps())
        }
    # 替换形如 $宏名 的内容
    def replace_macro(match):
        key = match.group(1)
        return _macros.get(key, match.group(0))
    result = re.sub(r"\$(\w+)", replace_macro, result)
    # 替换 $getc: 后跟盘符，如 $getc:C:
    def replace_getc_macro(match):
        drive = match.group(1)
        return getc(drive)
    result = re.sub(r"\$getc:([A-Za-z]:)", replace_getc_macro, result)
    output(result)

def define_macro(name, value):
    """
    定义或更新宏，名称不包含 "$" 符号，宏可用于 printf 中 "$宏名" 替换
    """
    global _macros
    try:
        _macros
    except NameError:
        _macros = {}
    _macros[name] = str(value)

# =======================
# 主 CMD 菜单
# =======================
def main_menu():
    while True:
        output("\n=== SuperLib Ultimate CMD ===")
        output("1. 数学运算测试")
        output("2. 随机数生成测试")
        output("3. 字符串长度检测")
        output("4. 相似度比较测试")
        output("5. 排序算法测试 (CMD)")
        output("6. 彩色输出测试")
        output("7. 系统信息测试 (HWID & Cookies)")
        output("8. 延迟函数测试")
        output("9. printf 测试 (新扩展功能)")
        output("10. 定义新宏 (例如: $name)")
        output("11. 退出")
        choice = user_input("请选择一个选项：")
        if choice == '1':
            output("【数学运算测试】")
            try:
                a = float(user_input("输入数字 a: "))
                b = float(user_input("输入数字 b: "))
            except Exception as e:
                output("输入错误：" + str(e))
                continue
            output(f"a + b = {Calculator.add(a, b)}")
            output(f"a - b = {Calculator.subtract(a, b)}")
            output(f"a * b = {Calculator.multiply(a, b)}")
            try:
                output(f"a / b = {Calculator.divide(a, b)}")
            except Exception as e:
                output("错误: " + str(e))
            output(f"a^b = {Calculator.power(a, int(b))}")
            output(f"sqrt(a) = {Calculator.sqrt(a)}")
            output(f"sin(a) ≈ {Calculator.sin(a)}")
            output(f"cos(a) ≈ {Calculator.cos(a)}")
        elif choice == '2':
            output("【随机数生成测试】")
            try:
                seed = int(user_input("输入种子（整数）："))
            except Exception as e:
                output("输入错误：" + str(e))
                continue
            rng = RandomGenerator(seed)
            output("生成的随机数（0~1）： " + str(rng.random()))
            try:
                lower = int(user_input("输入下界："))
                upper = int(user_input("输入上界："))
            except Exception as e:
                output("输入错误：" + str(e))
                continue
            output("生成的随机整数： " + str(rng.randint(lower, upper)))
        elif choice == '3':
            output("【字符串长度检测测试】")
            s = user_input("请输入字符串：")
            output("字符串长度为：" + str(check_length(s)))
        elif choice == '4':
            output("【相似度比较测试】")
            s1 = user_input("输入第一个字符串：")
            s2 = user_input("输入第二个字符串：")
            dist = levenshtein_distance(s1, s2)
            ratio = similarity_ratio(s1, s2)
            output(f"Levenshtein 距离：{dist}")
            output(f"相似度比率：{ratio:.2f}")
        elif choice == '5':
            cmd_sorting()
        elif choice == '6':
            output("【彩色输出测试】")
            ColorOutput.print_colored("这是红色文本", "red")
            ColorOutput.print_colored("这是绿色文本", "green")
            ColorOutput.print_colored("这是蓝色文本", "blue")
        elif choice == '7':
            output("【系统信息测试】")
            output("HWID: " + SystemInfo.get_hwid())
            output("Cookies: " + SystemInfo.get_cookies())
        elif choice == '8':
            output("【延迟函数测试】 开始延迟...")
            delay(1)
            output("延迟结束。")
        elif choice == '9':
            output("【printf 测试】")
            output("请输入测试字符串（支持 \\nt, %winver, %verx, %getc:盘符, %getfps:, 以及 $宏）：")
            test_str = user_input("")
            printf(test_str)
        elif choice == '10':
            output("【定义新宏】")
            macro_name = user_input("请输入宏名称（不含 $）：")
            macro_value = user_input("请输入宏值：")
            define_macro(macro_name, macro_value)
            output(f"已定义宏: ${macro_name} = {macro_value}")
        elif choice == '11':
            output("退出。")
            break
        else:
            output("无效选择，请重新输入。")

if __name__ == "__main__":
    main_menu()
