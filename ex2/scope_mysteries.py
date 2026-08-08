#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   scope_mysteries.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/03 12:18:17 by horarivo            #+#    #+#            #
#   Updated: 2026/08/03 12:18:18 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def description(item: str) -> str:
        return f"{enchantment_type} {item}"
    return description


def memory_vault() -> dict[str, Callable[..., object]]:
    memory: dict[str, int | str] = {}

    def store(key: str, value: int | str) -> None:
        memory[key] = value
        return

    def recall(key: str) -> int | str:
        if key in memory.keys():
            return memory[key]
        else:
            return "Memory not found"
    return {
            "store": store,
            "recall": recall
            }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())
    print()

    print("Testing spell accumulator...")
    base: int = 100
    spell = spell_accumulator(base)
    print(f"Base {base}, add 20:", spell(20))
    print(f"Base {base}, add 30:", spell(30))
    print()

    print("Testing enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    enchantement = enchantment_factory("Frozen")
    print(enchantment("Shield"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))
