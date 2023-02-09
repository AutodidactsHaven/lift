#pragma once

typedef enum {
    FIREBALL = 0,
    WATER_BLAST = 1,
    GRAVITY_WELL = 2,
} spell_tag;

typedef struct fireball_data {
    int damage;
} fireball_data;
typedef struct water_blast_data {
    int damage;
    int duration_ms;
} water_blast_data;
typedef struct gravity_well_data {
    float x; float y;
    int gravitational_pull;
} gravity_well_data;

typedef union spell_data {
    fireball_data fireball;
    water_blast_data water_blast;
    gravity_well_data gravity_well;
} spell_data;

/**
 * @brief tagged union of spells
 */
typedef struct spell {
    spell_tag tag;
    const char* name;
    int cooldown;
    union spell_data data;
} spell;

void cast_spell(spell spell);