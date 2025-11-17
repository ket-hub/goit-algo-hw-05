from typing import Callable
import re 

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text) -> str:
    for match in re.findall('\s+\d+.\d+\s+', text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

print(sum_profit(text, generator_numbers))     