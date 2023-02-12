#include <stdio.h>
#include "magic.h"

void cast_spell(spell spell) {
    printf("You cast a %s (%d) spell!\n", spell.name, spell.tag);
}