import pdxpy
import json

with open('mr_chars.json','r') as f:
    mr_chars = json.load(f)

# with open('bpm_vanilla_chars.json','r') as f:
#     bpm_vanilla_chars = json.load(f)

# with open('ecchi_chars.json','r') as f:
#     ecchi_chars = json.load(f)

mr_effect = [{"trigger":"has_character_template"}]
bpm_vanilla_effect = [{"trigger":"has_character_template"}]

for char, ig in mr_chars.items():
    mr_effect.append(pdxpy.PdxObject(
        {char:ig})
    )


def switch_effect(location,name,effect):
    with open(location ,"w+",encoding="utf-8-sig") as f:
        f.write(
            str(
                pdxpy.PdxObject(
                    {
                        name:pdxpy.PdxUtil.if_statement(
                                {'is_historical':True},
                                {"switch":effect}
                            )
                    }
                )
            )
        )

switch_effect("common/scripted_effects/bpm_mr_set_igs_effect.txt",'set_bpm_mr_ideology',mr_effect)
