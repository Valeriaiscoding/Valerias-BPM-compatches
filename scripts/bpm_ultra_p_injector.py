#INJECT at home workaround for BPM replacing stuff
import regex
import pdxpy
import json

with open("injecting.json",'r') as f:
    template = json.load(f)

with open("bpm_leader_ideologies.txt",'r') as f:
    lines = f.read()


with open("zzzzz_bpm_ultra_p_leader_ideologies.txt","w+", encoding = "utf-8-sig") as f:
    for key,value in template.items():
        template = regex.compile(fr'{key} =\s*(\{{(?:[^{{}}]++|(?1))*\}})')
        match = regex.search(template,lines).group()
        if match:
            match = match.replace(
                "interest_group_leader_trigger = {",
                f"{pdxpy.PdxObject(value)}\n\tinterest_group_leader_trigger = {{", 1
            )
            f.write(match +str('\n'))
