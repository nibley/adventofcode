from itertools import product as cartesian_product
# combinations

def fight(player_moves, enable_narration=False):
    fight_hp = player_hp
    fight_mp = player_mp
    fight_shield = lambda: 0 if effect_timers['Shield'] == 0 else 7

    fight_boss_hp = boss_hp

    effect_timers = {
        'Shield': 0,
        'Poison': 0,
        'Recharge': 0,
    }

    def narrate(message='', override=False):
        override = False
        if not (enable_narration or override):
            return
        print(message)
    inflect_word_point = lambda: 'point' if fight_hp == 1 else 'points'

    player_turn = True
    while True:
        turn_shield = fight_shield()
        narrate(f'-- {'Player' if player_turn else 'Boss'} turn --')
        narrate(f'- Player has {fight_hp} hit {inflect_word_point()}, {turn_shield} armor, {fight_mp} mana')
        narrate(f'- Boss has {fight_boss_hp} hit points')

        for effect in effects:
            timer = effect_timers[effect]
            if timer == 0:
                continue
            timer -= 1
            effect_timers[effect] = timer
            narrate(effect_messages[effect](timer))

            if effect == 'Shield':
                if timer == 0:
                    narrate('Shield wears off, decreasing armor by 7.')
            elif effect == 'Poison':
                if timer == 0:
                    narrate('Poison wears off.')
                fight_boss_hp -= 3
            elif effect == 'Recharge':
                if timer == 0:
                    narrate('Recharge wears off.')
                fight_mp += 101

        # 'This kills the boss, and the player wins.'

        if fight_boss_hp <= 0:
            narrate('WIN (by effect kill)', True)
            return True

        if player_turn:
            if not len(player_moves):
                narrate('LOSE (ran out of given moves)', True)
                return False
            spell = player_moves[0]
            player_moves = player_moves[1:]
            narrate(spell_messages[spell])
            
            fight_mp -= spell_costs[spell]
            if fight_mp < 0:
                # this is because of passing a moves list
                # instructions say being stuck also loses

                narrate('LOSE (tried too-expensive spell)', True)
                return False

            if spell in effects:
                if effect_timers[spell] == 0:
                    effect_timers[spell] = effect_timers_initial[spell]
                else:
                    narrate('LOSE (tried to double an effect)', True)
                    return False
            elif spell == 'Magic Missile':
                fight_boss_hp -= 4
            elif spell == 'Drain':
                fight_boss_hp -= 2
                fight_hp += 2
            
            if fight_boss_hp <= 0:
                narrate('WIN (by kill)')
                return True
        else: # boss turn
            if turn_shield == 0:
                turn_player_damage = boss_damage
                narrate(f'Boss attacks for {boss_damage} damage!')
            else:
                turn_player_damage = boss_damage - turn_shield
                narrate(f'Boss attacks for {boss_damage} - {turn_shield} = {turn_player_damage} damage!')
            fight_hp -= turn_player_damage

            if fight_hp <= 0:
                narrate('LOSE (by kill)', True)
                return False

        player_turn = not player_turn
        narrate()

spells = [
    'Magic Missile',
    'Drain',
    'Shield',
    'Poison',
    'Recharge',
]
spell_costs = {
    'Magic Missile': 53,
    'Drain': 73,
    'Shield': 113,
    'Poison': 173,
    'Recharge': 229,
}
effects = [
    'Shield',
    'Poison',
    'Recharge',
]
effect_timers_initial = {
    'Shield': 6,
    'Poison': 6,
    'Recharge': 5,
}
effect_messages = {
    'Shield': lambda timer: f'Shield\'s timer is now {timer}.',
    'Poison': lambda timer: f'Poison deals 3 damage; its timer is now {timer}.',
    'Recharge': lambda timer: f'Recharge provides 101 mana; its timer is now {timer}.',
}
spell_messages = {
    'Magic Missile': 'Player casts Magic Missile, dealing 4 damage.',
    'Drain': 'Player casts Drain, dealing 2 damage, and healing 2 hit points.',
    'Shield': 'Player casts Shield, increasing armor by 7.',
    'Poison': 'Player casts Poison.',
    'Recharge': 'Player casts Recharge.',
}

player_hp = 10
player_mp = 250

# test 1
# boss_damage = 8
# boss_hp = 13
# player_moves = ['Poison', 'Magic Missile']
# fight(player_moves, True)

# test 2
# boss_damage = 8
# boss_hp = 14
# player_moves = ['Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile']
# fight(player_moves, True)

boss_hp = int(input().split(' ')[-1])
boss_damage = int(input().split(' ')[-1])

num_moves = 12
# no dice 12 and under
move_lists = cartesian_product(*([spells] * num_moves))
win_costs = {}
for move_list in move_lists:
    # print(move_list)

    result = fight(move_list)
    if result:
        win_costs[move_list] = 0
    
    # print()

if not win_costs:
    print('no wins')
for move_list, win_cost in win_costs.items():
    print(move_list)

# best_moves, best_cost = sorted(win_costs.items(), key=lambda item: item[1])[0]
# print(best_moves)
# print(best_cost)
