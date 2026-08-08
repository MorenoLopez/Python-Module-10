#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/03 12:18:25 by horarivo            #+#    #+#            #
#   Updated: 2026/08/07 12:30:53 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import wraps
from typing import Any, Callable
import time


def spell_timer(func: Callable[[], str]) -> Callable[[], str]:
    @wraps(func)
    def wrapper() -> str:
        print(f"Casting {func.__name__}")
        start = time.time()
        time.sleep(0.101)
        res = func()
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res
    return wrapper


def power_validator(
    min_power: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def validator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = int(kwargs["power"])
            elif args:
                if isinstance(args[0], MageGuild):
                    power = int(args[2])
                else:
                    power = int(args[0])
            else:
                power = 0
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return validator


def retry_spell(
    max_attempts: int
) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def speller(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i < max_attempts:
                        print(f"Spell failed, retrying..."
                              f" (attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return speller


class MageGuild:
    @staticmethod
    def validate_name(name: str) -> bool:
        if len(name) >= 3:
            for letter in name:
                if not (letter.isspace() or letter.isalpha()):
                    return False
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def fireball() -> str:
        return "Fireball cast!"

    @retry_spell(3)
    def spell(target: Any) -> str:
        example: list[str] = ["Goblin", "Gardian", "Dragon"]
        for item in example:
            if item == target:
                return f"{target} spelled!"
        raise Exception()

    print("Testing spell time...")
    print(fireball())

    print("\nTesting retry spell...")
    print(spell("Flaming"))
    print(spell("Dragon"))

    print("\nTesting MageGuild...")
    print(MageGuild.validate_name("Lightning"))
    print(MageGuild.validate_name("Darkness1"))
    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
