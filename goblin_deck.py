slash = "+1 attack"
buddy_attack = "+0 attack, +3 played as a supporting attack"
block = "+1 defense against melee"

# if you use these within the same circle, 
pot_shot = "+2 attack, 1 dmg. Target may drop prone to avoid."
snipe = "+2 attack, 1 dmg"
covering_fire = "Interrupt. Give enemy -1. Ignores cover."

scamper = "move, then stealth at +2"
hide = "stealth at +2"


# deck = [buddy_attack]*2 + [slash] + [block]*2 + [snipe] + [pot_shot]*2 + [covering_fire]*2 + [scamper]*2 + [hide]*3

deck = ['Power Attack'] + 2*['Clobber'] + 2*['Headbutt'] + 3*['Shield Block']\
   + 2*['Shield Bash'] + ['Grim Resolve'] + 2*['Toughness'] + 2*['Weapon Skill']



from random import shuffle
shuffle(deck)

print(deck[:4])

