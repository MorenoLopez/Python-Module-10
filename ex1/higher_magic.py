#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/03 12:18:13 by horarivo            #+#    #+#            #
#   Updated: 2026/08/03 12:30:07 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    if power <= 0:
        return f"Fireball hits {target}"
    return f"{power}"


def heal(target: str, power: int) -> str:
    if power <= 0:
        return f"Heals {target}"
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combiner(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combiner


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def multiply(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)
    return multiply


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def cast(target: str, power: int) -> str:
        cond = condition(target, power)
        if not cond:
            return "Spell fizzled"
        return spell(target, power)
    return cast


def spell_sequence(
        spells: list[Callable[[str, int], str]]
) -> Callable[[], list[str]]:
    def sequence() -> list[str]:
        try:
            result: list[str] = []
            for spell in spells:
                result.append(spell("Dragon", 20))
            return result
        except Exception:
            return []
    return sequence


def main() -> None:
    combined = spell_combiner(fireball, heal)
    print("Testing spell combiner...")
    print("Combiner spell result:",
          ", ".join(str(x) for x in combined("Dragons", -1)))

    multiplied = power_amplifier(fireball, 3)
    print("Testing power amplifier...")
    print("Original:", multiplied("Goblin", 1),
          ", Amplified:", multiplied("Goblin", 7))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
