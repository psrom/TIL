# def plus(x, y):
#     result = x + y
#     return result

# plus(x = 4, y = 5)
# out: 9

# 들여쓰기 주의할 것
# return 명시!!!

# ==========================================
import pandas as pd

def udf_sum(x, y):
    result = x + y
    return result

udf_sum(pd.Series([2, 4, 6]), 4)
# Out
# 0 6
# 1 8
# 2 10

def udf_sum2(x, y):
    result = x.sum() + y
    return result

udf_sum2(pd.Series([2, 4, 6]), 4)
# Out: 16

def udf_mean1(x):
    result = round(x.mean(), 3)
    return result

print(udf_mean1(pd.Series([4, 6, 8])))
# Out : 6.0

def udf_mean2(x, digit):
    result = round(x.mean(), digit)
    return result

def udf_mean3(x, digit=3):
    result = round(x.mean(), digit)
    return result
# =======================================================
# Quiz

# 1. 입력 객체의 원소를 모두 제곱한 후 그 원소를 더한 다음
# 제곱근을 취하는 사용자 정의 함수를 만들었을 때 해당 사용자 정의 함수에
# [3, 5, 9, 20]를 입력으로 하는 경우 그 출력값은? 22.693611

def udf_euc(x):
    result = x.pow(2).sum() ** 0.5
    # result = (x ** 2).sum() ** 0.5
    return result

udf_euc(pd.Series([3, 5, 9, 20]))
# Out: 22.69361143

# =======================================================
# 2. 표준화 사용자 정의 함수를 만들고 [-4, 5, 7, 9]를
# 입력한 경우 여기서 입력한 7은 몇으로 반환되는가? 0.48

def nor_std(x):
    result = (x - x.mean()) / x.std()
    return result

nor_std(pd.Series([-4, 5, 7, 9]))
# Out: 0.48 

# =======================================================
# 3. MinMax 정규화 사용자 정의 함수를 만들고 [-4, 5, 7, 9]를
# 입력한 경우 여기서 입력한 7은 몇으로 반환되는가? 0.85

def nor_minmax(x):
    result = (x - x.min()) / (x.max() - x.min())
    return result

nor_minmax(pd.Series([-4, 5, 7, 9]))