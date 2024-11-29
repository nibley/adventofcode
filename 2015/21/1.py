from itertools import combinations

weapon_names = [
    'Dagger',
    'Shortsword',
    'Warhammer',
    'Longsword',
    'Greataxe'
]

armor_names = [
    'Leather',
    'Chainmail',
    'Splintmail',
    'Bandedmail',
    'Platemail'
]

ring_names = [
    'Damage +1',
    'Damage +2',
    'Damage +3',
    'Defense +1',
    'Defense +2',
    'Defense +3'
]

store = {
    'Dagger': {    'cost': 8,   'damage': 4, 'armor': 0},
    'Shortsword': {'cost': 10,  'damage': 5, 'armor': 0},
    'Warhammer': { 'cost': 25,  'damage': 6, 'armor': 0},
    'Longsword': { 'cost': 40,  'damage': 7, 'armor': 0},
    'Greataxe': {  'cost': 74,  'damage': 8, 'armor': 0},
    'Leather': {   'cost': 13,  'damage': 0, 'armor': 1},
    'Chainmail': { 'cost': 31,  'damage': 0, 'armor': 2},
    'Splintmail': {'cost': 53,  'damage': 0, 'armor': 3},
    'Bandedmail': {'cost': 75,  'damage': 0, 'armor': 4},
    'Platemail': { 'cost': 102, 'damage': 0, 'armor': 5},
    'Damage +1': { 'cost': 25,  'damage': 1, 'armor': 0},
    'Damage +2': { 'cost': 50,  'damage': 2, 'armor': 0},
    'Damage +3': { 'cost': 100, 'damage': 3, 'armor': 0},
    'Defense +1': {'cost': 20,  'damage': 0, 'armor': 1},
    'Defense +2': {'cost': 40,  'damage': 0, 'armor': 2},
    'Defense +3': {'cost': 80,  'damage': 0, 'armor': 3},
}

def fight(inventory):
    fight_hp = player_hp
    fight_damage = sum([store[item]['damage'] for item in inventory])
    fight_armor = sum([store[item]['armor'] for item in inventory])

    fight_boss_hp = boss_hp

    player_attack = max(1, fight_damage - boss_armor)
    boss_attack = max(1, boss_damage - fight_armor)

    while fight_hp > 0 and fight_boss_hp > 0:
        fight_boss_hp -= player_attack
        if fight_boss_hp <= 0:
            break

        fight_hp -= boss_attack

    return fight_hp > 0

player_hp = 100

get_boss_stat = lambda: int(input().split()[-1])
boss_hp = get_boss_stat()
boss_damage = get_boss_stat()
boss_armor = get_boss_stat()

inventories = tuple(
    weapon_inventory + armor_inventory + ring_inventory
    for weapon_inventory in combinations(weapon_names, 1)
    for armor_inventory in (
        *combinations(armor_names, 1),
        ()
    )
    for ring_inventory in (
        *combinations(ring_names, 1),
        *combinations(ring_names, 2),
        ()
    )
)

print(
    min(
        sum( store[item]['cost'] for item in inventory )
        for inventory in inventories
        if fight(inventory)
    )
)
