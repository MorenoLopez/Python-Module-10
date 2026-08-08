#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   functools_artifacts.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/03 12:18:00 by horarivo            #+#    #+#            #
#   Updated: 2026/08/07 12:24:10 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import (
    reduce,
    partial,
    lru_cache,
    singledispatch
)
from operator import add, mul
from typing import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int | None:
    operators: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }
    try:
        op = operators.get(operation)
        if op:
            if len(spells) == 0:
                return 0
            return reduce(op, spells)
        else:
            raise Exception()
    except Exception:
        print("Supported operations: 'add', 'multiply', 'max', 'min'")
        return None


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    fireball = partial(base_enchantment, 50, "fire")
    iceball = partial(base_enchantment, 50, "ice")
    waterball = partial(base_enchantment, 50, "water")
    return {
        "fire": fireball,
        "ice": iceball,
        "water": waterball
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[..., str]:
    @singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


def base_(power: int, element: str, target: str) -> str:
    return f"{target} products {element} with {power} HP"


if __name__ == "__main__":
    print("Testing spell reducer...")
    base: list[int] = [40, 10, 30, 20]
    print("Sum:", spell_reducer(base, "add"))
    print("Product:", spell_reducer(base, "multiply"))
    print("Max:", spell_reducer(base, "max"))
    print("Min:", spell_reducer(base, "min"))

    print("\nTesting partial enchanter...")
    enchanter = partial_enchanter(base_)
    print(enchanter["fire"]("Dragon"))
    print(enchanter["ice"]("Frozen"))
    print(enchanter["water"]("Goblin"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print(memoized_fibonacci.cache_info())
    print("Fib(15):", memoized_fibonacci(15))
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    result = spell_dispatcher()
    print(result(42))
    print(result("fireball"))
    print(result([1, True, "all"]))
    print(result(True))
