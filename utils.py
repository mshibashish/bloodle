from typing import List


def monkey_lists(monkey_type: str) -> List:
    primary_monkeys = [
        "Dart Monkey",
        "Boomerang Monkey",
        "Bomb Shooter",
        "Tack Shooter",
        "Ice Monkey",
        "Glue Gunner"
    ]
    military_monkeys = [
        "Sniper Monkey",
        "Monkey Sub",
        "Monkey Buccaneer",
        "Monkey Ace",
        "Heli Pilot",
        "Mortar Monkey",
        "Dartling Gunner"
    ]
    magic_monkeys = [
        "Wizard Monkey",
        "Super Monkey",
        "Ninja Monkey",
        "Alchemist",
        "Druid"
    ]
    support_monkeys = [
        "Banana Farm",
        "Spike Factory",
        "Monkey Village",
        "Engineer Monkey"
    ]

    return eval(monkey_type)
