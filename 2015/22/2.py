from dataclasses import dataclass, field
from copy import deepcopy
from math import inf

spell_costs = {
    'Magic Missile': 53,
    'Drain': 73,
    'Shield': 113,
    'Poison': 173,
    'Recharge': 229,
}
min_spell_cost = min(spell_costs.values())

effect_timers_initial = {
    'Shield': 6,
    'Poison': 6,
    'Recharge': 5,
}

player_hp_original = 50
player_mp_original = 500
boss_hp_original = int(input().split(' ')[-1])
boss_damage = int(input().split(' ')[-1])

@dataclass
class FightState:
    mana_spent: int = 0
    player_hp: int = player_hp_original
    player_mp: int = player_mp_original
    boss_hp: int = boss_hp_original
    effect_timers: dict = field(
        default_factory=lambda: {
            'Shield': 0,
            'Poison': 0,
            'Recharge': 0,
    })

def apply_effects(fight_state):
    for effect, effect_timer in fight_state.effect_timers.items():
        if effect_timer > 0:
            if effect == 'Poison':
                fight_state.boss_hp -= 3
            elif effect == 'Recharge':
                fight_state.player_mp += 101

    for effect, effect_timer in fight_state.effect_timers.items():
        if effect_timer > 0:
            fight_state.effect_timers[effect] -= 1

def fight(spell=None, previous_state=None):
    '''returns int mana cost for win,
    False for loss, and FightState for ongoing'''

    if previous_state is None: # we're just initializing
        return FightState()

    fight_state = deepcopy(previous_state)

    if fight_state.player_mp < min_spell_cost:
        return False

    # do player turn
    fight_state.player_hp -= 1
    if fight_state.player_hp <= 0:
        return False

    apply_effects(fight_state)

    mana_cost = spell_costs[spell]
    fight_state.player_mp -= mana_cost
    fight_state.mana_spent += mana_cost

    if spell in fight_state.effect_timers.keys():
        if fight_state.effect_timers[spell]:
            return False # can't double up on active effects
        else:
            fight_state.effect_timers[spell] = \
                effect_timers_initial[spell]
    elif spell == 'Magic Missile':
        fight_state.boss_hp -= 4
    elif spell == 'Drain':
        fight_state.boss_hp -= 2
        fight_state.player_hp += 2

    # do boss turn
    apply_effects(fight_state)
    if fight_state.boss_hp <= 0:
        return fight_state.mana_spent

    player_shield = 7 if fight_state.effect_timers['Shield'] else 0
    round_boss_damage = max(1, boss_damage - player_shield)
    fight_state.player_hp -= round_boss_damage

    if fight_state.player_hp <= 0:
        return False

    # round over
    return fight_state

class KilledBoss(Exception):
    pass

states_to_crawl = [fight()] # get initial fight state
victory_cost = None
try:
    while True:
        new_states_found = []
        for fight_state in states_to_crawl:
            for spell in spell_costs.keys():
                new_fight_state = fight(spell, fight_state)

                if type(new_fight_state) is int:
                    victory_cost = new_fight_state
                    raise KilledBoss()
                elif type(new_fight_state) is FightState:
                    new_states_found.append(new_fight_state)

        states_to_crawl = new_states_found
except KilledBoss:
    print(victory_cost)
