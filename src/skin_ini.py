import json

def generate(ver):
    with open("assets/skin.json","r") as f:
        skin =  json.loads(f.read())

    final = [   "#            guhw's characterless skin            #",
                "# https://github.com/grhw/guhw-characterless-skin #"]

    def center_lanes(lanes):
        return int((480/(1080/1920))/2 - ((lanes*skin["Mania"]["AllKey"]["ColumnWidth"])/2))

    def copy_for_ini(string,amount):
        return (f"{string},"*(amount)).strip(",")

    
    for category_name in skin["Copy"].keys():
        final.append(f"\n[{category_name}]")
        category = skin["Copy"][category_name]
        for key in category.keys():
            if key == "Author":
                final.append(f"Name: {ver} {skin["Name"]}")
            value = category[key]
            final.append(f"{key}: {str(value).strip("[]")}")

    for keys in range(1,19):
        final.append(f"\n[Mania]")
        final.append(f"Keys: {keys}")
        
        for key in skin["Mania"]["Copy"].keys():
            value = skin["Mania"]["Copy"][key]
            final.append(f"{key}: {value}")
        
        final.append(f"ColumnWidth: {copy_for_ini(skin["Mania"]["AllKey"]["ColumnWidth"],keys)}")
        final.append(f"ColumnLineWidth: {copy_for_ini(skin["Mania"]["AllKey"]["ColumnLineWidth"],keys+1)}")
        final.append(f"ColumnStart: {center_lanes(keys)}")
        for i in range(keys):
            final.append(f"Colour{i+1}: {str(skin["Mania"]["AllKey"]["Colour"]).strip("[]")}")

    with open("build/skin.ini","w+") as f:
        f.write("\n".join(final))