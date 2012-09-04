# -*- coding: utf-8 -*-
#!/usr/bin/env python

from lettuce import *

WOLF_FORCE = 5

MATERIAL_RESISTANCES = {
    'paille': 1,
    'bois': 4,
    'briques': 6
}

@step('cochon a construit une maison de (paille|bois|briques)')
def get_house_material(step, material):
    world.resistance = MATERIAL_RESISTANCES[material]

@step('le loup souffle sur la maison')
def blow_on_house(step):
    world.force = WOLF_FORCE

@step(u"la maison est (détruite|intacte)")
def check_house_state(step, state):
    if state == u"détruite":
        # The wolf force is greater than the house resistance
        assert world.force > world.resistance, \
            "La force %d n'est pas superieure a %d" % (world.force, world.resistance)
    else:
        assert world.force <= world.resistance, \
            "La force %d n'est pas inferieure ou egale a %d" % (world.force, world.resistance)
