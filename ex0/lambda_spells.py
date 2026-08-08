#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/03 12:18:08 by horarivo            #+#    #+#            #
#   Updated: 2026/08/03 12:36:55 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any


def artifact_sorter(
        artifacts: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    artifact_sorted = sorted(
        artifacts,
        key=lambda x: x.get("power", 0),
        reverse=True
    )
    return artifact_sorted


def power_filter(
        mages: list[dict[str, Any]],
        min_power: int
) -> list[dict[str, Any]]:
    filtered = list(filter(
        lambda x: x.get("power", 0) >= min_power,
        mages
                    ))
    return filtered


def spell_transformer(spells: list[str]) -> list[str]:
    result = list(map(lambda spell: f"* {spell} *", spells))
    return result


def mage_stats(mage: list[dict[str, Any]]) -> dict[str, Any]:
    max_power = max(map(lambda x: x.get("power", 0), mage))
    min_power = min(map(lambda x: x.get("power", 0), mage))
    avg_power = round(
        sum(list(map(
            lambda x: x.get("power", 0), mage
        ))) / len(mage),
        2
    )
    return {
        "max_power": max_power,
        "min_power": min_power,
        "average": avg_power
    }


if __name__ == "__main__":
    artifact: list[dict[str, Any]] = [
                    {"name": "Fire Staff", "power": 95, "type": "Staff"},
                    {"name": "Crystal Orb", "power": 85, "type": "Crystal"}
            ]
    mage: list[dict[str, Any]] = [
                    {"name": "Fire Staff", "power": 95, "element": "Staff"},
                    {"name": "Crystal Orb", "power": 85, "element": "Crystal"},
                    {"name": "Wizard"}
                ]
    spells: list[str] = ["fireball", "heal", "shield"]

    artifact_sorted = artifact_sorter(artifact)
    filtered = power_filter(mage, 20)
    result = spell_transformer(spells)
    dic_result = mage_stats(artifact)

    print("Testing artifact sorter...")

    print(
        f"{artifact_sorted[0]['name']} ({artifact_sorted[0]['power']} power) "
        f"comes before {artifact_sorted[1]['name']}"
        f"({artifact_sorted[1]['power']} power)"
    )
    print()
    print("Testing spell transformer...")
    print(*result)
    print()
    print("Result:", dic_result)
