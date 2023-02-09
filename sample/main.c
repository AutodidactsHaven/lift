#include "magic.h"

int main() {
    spell quick_bar_spell_1 = {
        .tag = GRAVITY_WELL,
        .name = "Gravity Well",
        .cooldown = 5,
        .data.gravity_well = {
            .x = 4.0, .y = 5.0, .gravitational_pull = 100
        }
    };

    cast_spell(quick_bar_spell_1);

    return 0;
}