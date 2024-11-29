from dataclasses import dataclass, field
from copy import deepcopy

spell_costs = {
    'Magic Missile': 53,
    'Drain': 73,
    'Shield': 113,
    'Poison': 173,
    'Recharge': 229
}
min_spell_cost = min(spell_costs.values())

effect_timers_initial = {
    'Shield': 6,
    'Poison': 6,
    'Recharge': 5
}

player_hp_original = 50
player_mp_original = 500

get_boss_stat = lambda: int(input().split()[-1])
boss_hp_original = get_boss_stat()
boss_damage = get_boss_stat()

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
            'Recharge': 0
        }
    )

def apply_effects(fight_state):
    effect_timers = fight_state.effect_timers

    for effect, effect_timer in effect_timers.items():
        if effect_timer > 0:
            if effect == 'Poison':
                fight_state.boss_hp -= 3
            elif effect == 'Recharge':
                fight_state.player_mp += 101

    for effect, effect_timer in effect_timers.items():
        if effect_timer > 0:
            effect_timers[effect] -= 1

def simulate_turn(spell=None, previous_state=None):
    '''returns int mana cost for win,
    False for loss,
    and FightState for ongoing'''

    if previous_state is None:
        # we're just initializing
        return FightState()

    fight_state = deepcopy(previous_state)

    if fight_state.player_mp < min_spell_cost:
        return False

    # do player turn
    fight_state.player_hp -= 1
    if not fight_state.player_hp > 0:
        return False

    apply_effects(fight_state)

    mana_cost = spell_costs[spell]
    fight_state.player_mp -= mana_cost
    fight_state.mana_spent += mana_cost

    effect_timers = fight_state.effect_timers
    if spell in effect_timers_initial:
        if effect_timers[spell]:
            # can't double up on active effects
            return False
        else:
            effect_timers[spell] = effect_timers_initial[spell]
    elif spell == 'Magic Missile':
        fight_state.boss_hp -= 4
    elif spell == 'Drain':
        fight_state.boss_hp -= 2
        fight_state.player_hp += 2

    # do boss turn
    apply_effects(fight_state)
    if not fight_state.boss_hp > 0:
        return fight_state.mana_spent

    player_shield = 7 if effect_timers['Shield'] else 0
    fight_state.player_hp -= max(1, boss_damage - player_shield)

    if not fight_state.player_hp > 0:
        return False

    # round over but fight continuing
    return fight_state

states_to_crawl = [simulate_turn()] # get initial fight state
victory_cost = None
while victory_cost is None and states_to_crawl:
    new_states_found = []
    for fight_state in states_to_crawl:
        for spell in spell_costs:
            new_fight_state = simulate_turn(spell, fight_state)

            if type(new_fight_state) is int:
                victory_cost = new_fight_state
                break
            elif type(new_fight_state) is FightState:
                new_states_found.append(new_fight_state)

        if victory_cost is not None:
            break

    states_to_crawl = new_states_found

print(victory_cost)
