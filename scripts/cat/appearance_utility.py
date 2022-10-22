from .pelts import *

# ---------------------------------------------------------------------------- #
#                               utility functions                              #
# ---------------------------------------------------------------------------- #

def plural_acc_names(accessory ,plural, singular):
    acc_display = accessory
    if accessory == 'maple leaf':
        if plural == True:
            acc_display = 'maple leaves'
        if singular == True:
            acc_display = 'maple leaf'
    elif accessory == 'holly':
        if plural == True:
            acc_display = 'holly berries'
        if singular == True:
            acc_display = 'holly berry'
    elif accessory == 'blue berries':
        if plural == True:
            acc_display = 'blueberries'
        if singular == True:
            acc_display = 'blueberry'
    elif accessory == 'forget me nots':
        if plural == True:
            acc_display = 'forget me nots'
        if singular == True:
            acc_display = 'forget me not flower'
    elif accessory == 'rye stalk':
        if plural == True:
            acc_display = 'rye stalks'
        if singular == True:
            acc_display = 'rye stalk'
    elif accessory == 'laurel':
        if plural == True:
            acc_display = 'laurel'
        if singular == True:
            acc_display = 'laurel plant'
    elif accessory == 'bluebells':
        if plural == True:
            acc_display = 'bluebells'
        if singular == True:
            acc_display = 'bluebell flower'
    elif accessory == 'nettle':
        if plural == True:
            acc_display = 'nettles'
        if singular == True:
            acc_display = 'nettle'
    elif accessory == 'poppy':
        if plural == True:
            acc_display = 'poppies'
        if singular == True:
            acc_display = 'poppy flower'
    elif accessory == 'lavender':
        if plural == True:
            acc_display = 'lavender'
        if singular == True:
            acc_display = 'lavender flower'
    elif accessory == 'herbs':
        if plural == True:
            acc_display = 'herbs'
        if singular == True:
            acc_display = 'herb'
    elif accessory == 'petals':
        if plural == True:
            acc_display = 'petals'
        if singular == True:
            acc_display = 'petal'
    elif accessory == 'dry herbs':
        if plural == True:
            acc_display = 'dry herbs'
        if singular == True:
            acc_display = 'dry herb'
    elif accessory == 'oak leaves':
        if plural == True:
            acc_display = 'oak leaves'
        if singular == True:
            acc_display = 'oak leaf'
    elif accessory == 'catmint':
        if plural == True:
            acc_display = 'catnip'
        if singular == True:
            acc_display = 'catnip leaf'
    elif accessory == 'maple seed':
        if plural == True:
            acc_display = 'maple seeds'
        if singular == True:
            acc_display = 'maple seed'
    elif accessory == 'juniper':
        if plural == True:
            acc_display = 'juniper berries'
        if singular == True:
            acc_display = 'juniper berry'
    elif accessory == 'red feathers':
        if plural == True:
            acc_display = 'cardinal feathers'
        if singular == True:
            acc_display = 'cardinal feather'
    elif accessory == 'blue feathers':
        if plural == True:
            acc_display = 'crow feathers'
        if singular == True:
            acc_display = 'crow feather'
    elif accessory == 'jay feathers':
        if plural == True:
            acc_display = 'jay feathers'
        if singular == True:
            acc_display = 'jay feather'
    elif accessory == 'moth wings':
        if plural == True:
            acc_display = 'moth wings'
        if singular == True:
            acc_display = 'moth wing'
    elif accessory == 'cicada wings':
        if plural == True:
            acc_display = 'cicada wings'
        if singular == True:
            acc_display = 'cicada wing'

    if plural is True and singular is False:
        return acc_display
    elif singular is True and plural is False:
        return acc_display

def accessory_display_name(accessory):
    if not accessory:
        return ''
    accessory = accessory.lower()
    acc_display = accessory
    if accessory != None:
        if accessory in collars:
            collar_color = None
            if accessory.startswith('crimson'):
                collar_color = 'crimson'
            elif accessory.startswith('blue'):
                collar_color = 'blue'
            elif accessory.startswith('yellow'):
                collar_color = 'yellow'
            elif accessory.startswith('cyan'):
                collar_color = 'cyan'
            elif accessory.startswith('red'):
                collar_color = 'red'
            elif accessory.startswith('lime'):
                collar_color = 'lime'
            elif accessory.startswith('green'):
                collar_color = 'green'
            elif accessory.startswith('rainbow'):
                collar_color = 'rainbow'
            elif accessory.startswith('black'):
                collar_color = 'black'
            elif accessory.startswith('spikes'):
                collar_color = 'spiky'
            elif accessory.startswith('pink'):
                collar_color = 'pink'
            elif accessory.startswith('purple'):
                collar_color = 'purple'
            elif accessory.startswith('multi'):
                collar_color = 'multi'
            if accessory.endswith('bow') and not accessory == 'rainbow':
                acc_display = collar_color + ' bow'
            elif accessory.endswith('bell'):
                acc_display = collar_color + ' bell collar'
            else:
                acc_display = collar_color + ' collar'

    elif accessory in wild_accessories:
        if acc_display == 'blue feathers':
            acc_display = 'crow feathers'
        elif acc_display == 'red feathers':
            acc_display = 'cardinal feathers'
        else:
            acc_display = acc_display
    else:
        acc_display = acc_display
    if accessory == None:
        acc_display = None
    return acc_display

# ---------------------------------------------------------------------------- #
#                                init functions                                #
# ---------------------------------------------------------------------------- #

def init_eyes(cat):
    if cat.eye_colour != None:
        return
    hit = randint(0, 200)
    if hit == 1:
        cat.eye_colour = choice(["BLUEYELLOW", "BLUEGREEN"])
    else:
        if cat.parent1 is None:
            cat.eye_colour = choice(eye_colours)
        elif cat.parent2 is None:
            par1 = cat.all_cats[cat.parent1]
            cat.eye_colour = choice(
                [par1.eye_colour, choice(eye_colours)])
        else:
            par1 = cat.all_cats[cat.parent1]
            par2 = cat.all_cats[cat.parent2]
            cat.eye_colour = choice([
                par1.eye_colour, par2.eye_colour,
                choice(eye_colours)
            ])

def init_pelt(cat):
    if cat.pelt != None:
        return

    if cat.parent2 is None and cat.parent1 in cat.all_cats.keys():
        # 1 in 3 chance to inherit a single parent's pelt
        par1 = cat.all_cats[cat.parent1]
        cat.pelt = choose_pelt(cat.gender, choice([par1.pelt.colour, None]), choice([par1.pelt.white, None]), choice([par1.pelt.name, None]),
                                choice([par1.pelt.length, None]))
    if cat.parent1 in cat.all_cats.keys() and cat.parent2 in cat.all_cats.keys():
        # 2 in 3 chance to inherit either parent's pelt
        par1 = cat.all_cats[cat.parent1]
        par2 = cat.all_cats[cat.parent2]
        cat.pelt = choose_pelt(cat.gender, choice([par1.pelt.colour, par2.pelt.colour, None]), choice([par1.pelt.white, par2.pelt.white, None]),
                                choice([par1.pelt.name, par2.pelt.name, None]), choice([par1.pelt.length, par2.pelt.length, None]))                  
    else:
        cat.pelt = choose_pelt(cat.gender)

def init_sprite(cat):
    if cat.pelt == None:
        init_pelt(cat)
    cat.age_sprites = {
        'kitten': randint(0, 2),
        'adolescent': randint(3, 5),
        'elder': randint(3, 5)
    }
    cat.reverse = choice([True, False])
    cat.skin = choice(skin_sprites)
    if cat.pelt is not None:
        if cat.pelt.length != 'long':
            cat.age_sprites['adult'] = randint(6, 8)
        else:
            cat.age_sprites['adult'] = randint(0, 2)
        cat.age_sprites['young adult'] = cat.age_sprites['adult']
        cat.age_sprites['senior adult'] = cat.age_sprites['adult']
        cat.age_sprites['dead'] = None

def init_scars(cat):
    scar_choice = randint(0, 15)
    if cat.age in ['kitten', 'adolescent']:
        scar_choice = randint(0, 50)
    elif cat.age in ['young adult', 'adult']:
        scar_choice = randint(0, 20)
    if scar_choice == 1:
        cat.specialty = choice([
            choice(scars1),
            choice(scars2),
            choice(scars4),
            choice(scars5)
        ])
    else:
        cat.specialty = None

    scar_choice2 = randint(0, 30)
    if cat.age in ['kitten', 'adolescent']:
        scar_choice2 = randint(0, 100)
    elif cat.age in ['young adult', 'adult']:
        scar_choice2 = randint(0, 40)
    if scar_choice2 == 1:
        cat.specialty2 = choice([
            choice(scars1),
            choice(scars2),
            choice(scars4),
            choice(scars5)
        ])
    else:
        cat.specialty2 = None

def init_accessories(cat):
    accessory_choice = randint(0, 35)
    if cat.age in ['kitten', 'adolescent']:
        accessory_choice = randint(0, 15)
    elif cat.age in ['young adult', 'adult']:    
        accessory_choice = randint(0, 50)
    if accessory_choice == 1:
        cat.accessory = choice([
            choice(plant_accessories),
            choice(wild_accessories)
        ])
    else:
        cat.accessory = None

def init_pattern(cat):
    if cat.pelt == None:
        init_pelt(cat)
    if cat.pelt.name in ['Calico', 'Tortie']:
        cat.tortiecolour = cat.pelt.colour
        cat.tortiebase = choice(['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled'])
        if cat.tortiebase == 'tabby':
            cat.tortiepattern = 'tortietabby'
        elif cat.tortiebase == 'bengal':
            cat.tortiepattern = 'tortiebengal'
        elif cat.tortiebase == 'marbled':
            cat.tortiepattern = 'tortiemarbled'
        elif cat.tortiebase == 'ticked':
            cat.tortiepattern = 'tortieticked'
        elif cat.tortiebase == 'rosette':
            cat.tortiepattern = 'tortierosette'
        elif cat.tortiebase == 'smoke':
            cat.tortiepattern = 'tortiesmoke'
        elif cat.tortiebase == 'speckled':
            cat.tortiepattern = 'tortiespeckled'
        else:
            cat.tortiepattern = 'tortietabby'
    else:
        cat.tortiebase = None
        cat.tortiepattern = None
        cat.tortiecolour = None
    if cat.pelt.name in ['Calico', 'Tortie'] and cat.pelt.colour != None:
        if cat.pelt.colour in ["BLACK", "DARKBROWN"]:
            cat.pattern = choice(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
                                    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR'])
        elif cat.pelt.colour in ["DARKGREY", "BROWN"]:
            cat.pattern = choice(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR'])
        elif cat.pelt.colour in ["SILVER", "GREY", "LIGHTBROWN"]:
            cat.pattern = choice(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR'])
    else:
        cat.pattern = None

def init_white_patches(cat):
    if cat.pelt == None:
        init_pelt(cat)
    non_white_pelt = False
    if cat.pelt.colour != 'WHITE' and cat.pelt.name in\
    ['Tortie', 'TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked', 'Smoke', 'Rosette']:
        non_white_pelt = True
    little_white_poss = little_white * 6
    mid_white_poss = mid_white * 4
    high_white_poss = high_white * 2
    mostly_white_poss = mostly_white
    if cat.pelt.white is True:
        pelt_choice = randint(0, 10)
        vit_chance = randint(0, 40)
        direct_inherit = randint(0, 10)
        # inheritance
        # one parent
        if cat.parent1 is not None and cat.parent2 is None and cat.parent1 in cat.all_cats:
            par1 = cat.all_cats[cat.parent1]
            if direct_inherit == 1:
                if par1.pelt.white is False:
                    cat.pelt.white = False
                else:
                    cat.white_patches = par1.white_patches
            elif vit_chance == 1:
                cat.white_patches = choice(vit)
            else:
                if par1.white_patches in point_markings and non_white_pelt is True:
                    cat.white_patches = choice(point_markings)
                elif par1.white_patches in vit:
                    cat.white_patches = choice(vit)
                elif par1.white_patches in [None] + little_white + mid_white + high_white:
                    cat.white_patches = choice([None] + little_white_poss + mid_white_poss + high_white_poss + mostly_white_poss)
                elif par1.white_patches in mostly_white:
                    cat.white_patches = choice(mid_white + high_white + mostly_white + ['FULLWHITE'])
            if par1.white_patches == None and cat.pelt.name == 'Calico':
                cat.pelt.name = 'Tortie'
            # two parents
        elif cat.parent1 is not None and cat.parent2 is not None and\
            cat.parent1 in cat.all_cats and cat.parent2 in cat.all_cats:
            # if 1, cat directly inherits parent 1's white patches. if 2, it directly inherits parent 2's
            par1 = cat.all_cats[cat.parent1]
            par2 = cat.all_cats[cat.parent2]
            if direct_inherit == 1:
                if par1.pelt.white is False:
                    cat.pelt.white = False
                else:
                    cat.white_patches = par1.white_patches
            elif direct_inherit == 2:
                if par2.pelt.white is False:
                    cat.pelt.white = False
                else:
                    cat.white_patches = par2.white_patches
            elif vit_chance == 1:
                cat.white_patches = choice(vit)
            else:
                if par1.white_patches in point_markings and non_white_pelt is True\
                or par2.white_patches in point_markings and non_white_pelt is True:
                    cat.white_patches = choice(point_markings)
                elif par1.white_patches in vit and non_white_pelt is True\
                or par2.white_patches in vit and non_white_pelt is True:
                    cat.white_patches = choice(vit)
                elif par1.white_patches is None:
                    if par2.white_patches is None:
                        cat.white_patches = None
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white_poss + [None])
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(little_white_poss + mid_white_poss)
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(little_white + mid_white_poss * 2 + high_white)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss + mostly_white)
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(little_white_poss + mid_white_poss + high_white_poss + mostly_white_poss + ['FULLWHITE'])
                    else:
                        cat.white_patches = choice(little_white)
                elif par1.white_patches in little_white:
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + [None])
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white_poss * 2 + mid_white_poss + [None])
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(little_white_poss + mid_white_poss + high_white)
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(little_white + mid_white_poss * 2 + high_white_poss + mostly_white)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(mid_white + high_white_poss + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(high_white_poss + mostly_white_poss + ['FULLWHITE'])
                    else:
                        cat.white_patches = choice(little_white)
                elif par1.white_patches in mid_white:
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + mid_white + [None])
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white_poss + mid_white_poss + high_white)
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(little_white + mid_white_poss * 3 + high_white)
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss * 3 + mostly_white)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(mid_white + high_white_poss * 2 + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(high_white_poss + mostly_white_poss + ['FULLWHITE'])
                    else:
                        cat.white_patches = choice(mid_white)
                elif par1.white_patches in high_white:
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + mid_white_poss + high_white + [None])
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white_poss + mid_white_poss + high_white)
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(little_white + mid_white_poss + high_white_poss)
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss * 2 + mostly_white)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(mid_white + high_white_poss + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(high_white_poss + mostly_white_poss + ['FULLWHITE'])
                    else:
                        cat.white_patches = choice(high_white)
                elif par1.white_patches in mostly_white:
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + mid_white + high_white + mostly_white)
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white + mid_white_poss + high_white_poss + mostly_white)
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(high_white_poss + mostly_white + mostly_white + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(high_white + mostly_white * 4 + ['FULLWHITE'])
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(mostly_white * 5 + ['FULLWHITE', 'FULLWHITE', 'FULLWHITE'])
                    else:
                        cat.white_patches = choice(mostly_white)
                elif par1.white_patches == 'FULLWHITE':
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + mid_white + high_white + mostly_white + [None] + ['FULLWHITE'])
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss * 2 + mostly_white * 2)
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(mid_white + high_white_poss * 3 + mostly_white * 3 + ['FULLWHITE'])
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(high_white_poss + mostly_white * 4 + ['FULLWHITE'] * 3)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(high_white + mostly_white * 4 + ['FULLWHITE'] * 4)
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(mostly_white + ['FULLWHITE'] * 6)
                    else:
                        cat.white_patches = choice(mostly_white)
            if cat.pelt.name == 'Calico' and par1.white_patches not in mid_white + high_white + mostly_white\
            and par2.white_patches not in mid_white + high_white + mostly_white:
                cat.pelt.name = 'Tortie'
                
        # regular non-inheritance white patches generation
        else:
            if pelt_choice == 1 and non_white_pelt is True:
                cat.white_patches = choice(point_markings)
            elif pelt_choice == 1 and cat.pelt.name == 'TwoColour' and cat.pelt.colour != 'WHITE':
                cat.white_patches = choice(point_markings + ['POINTMARK'])
            elif pelt_choice == 2 and cat.pelt.name in ['Calico', 'TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked', 'Smoke', 'Rosette']:
                cat.white_patches = choice(mostly_white_poss)
            elif pelt_choice == 3 and cat.pelt.name in ['TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked', 'Smoke', 'Rosette']\
            and cat.pelt.colour != 'WHITE':
                cat.white_patches = choice(['EXTRA', None, 'FULLWHITE'])
            else:
                if cat.pelt.name in ['TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked', 'Smoke', 'Rosette']:
                    cat.white_patches = choice(little_white_poss + mid_white_poss + high_white_poss)
                elif cat.pelt.name in ['Tortie']:
                    cat.white_patches = choice(little_white_poss + mid_white_poss)
                elif cat.pelt.name in ['Calico']:
                    cat.white_patches = choice(high_white_poss)
                elif pelt_choice == 1 and vit_chance == 1 and cat.pelt.name in ['Tortie', 'TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked', 'Smoke', 'Rosette']\
                and cat.pelt.colour != 'WHITE':
                    cat.white_patches = choice(vit)
                else:
                    cat.white_patches = None
    else:
        cat.white_patches = None
