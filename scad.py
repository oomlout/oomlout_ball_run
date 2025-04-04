import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

shift_up = 1
clear_6_mm_diameter = 0.5/2
radius_ball_6_mm = 6/2 + clear_6_mm_diameter
radius_6_mm  = 6/2

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    oomp_mode = "project"
    #oomp_mode = "oobb"

    test = True
    #test = False

    if typ == "all":
        #test true
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = True
        #default
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        #test
        if True:
            extras = []
            extras.append("6_mm")
            extras.append("8_mm")
            extras.append("10_mm")

            for extra in extras:
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = 3
                p3["height"] = 3
                p3["thickness"] = 9
                if extra != "":
                    p3["extra"] = extra
                part["kwargs"] = p3
                nam = "test"
                part["name"] = nam
                if oomp_mode == "oobb":
                    p3["oomp_size"] = nam#
                if not test:
                #if test or not test:
                    parts.append(part)
                

        #flats
        if True:
            lengths = []
            lengths.append(3)
            lengths.append(6)

            for length in lengths:
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = length
                p3["height"] = 1
                p3["thickness"] = 6
                part["kwargs"] = p3
                nam = f"flat"
                part["name"] = nam
                if oomp_mode == "oobb":
                    p3["oomp_size"] = nam
                #if not test:
                if test or not test:
                    parts.append(part)

        #backboard
        if True:
            sizes = []
            sizes.append([3,3]) 
            sizes.append([5,5])   
            sizes.append([7,7])
            sizes.append([9,9])
            sizes.append([11,11])

            for size in sizes:
                wid, hei = size
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = wid
                p3["height"] = hei
                p3["thickness"] = 4
                part["kwargs"] = p3
                nam = f"backboard"
                part["name"] = nam
                if oomp_mode == "oobb":
                    p3["oomp_size"] = nam
                if not test:
                #if test or not test:
                    parts.append(part)

        #uturn
        if True:
            sizes = []
            sizes.append([1.5,3])    

            for size in sizes:
                wid, hei = size
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = wid
                p3["height"] = hei
                p3["thickness"] = 6
                part["kwargs"] = p3
                nam = f"u_turn"
                part["name"] = nam
                if oomp_mode == "oobb":
                    p3["oomp_size"] = nam
                #if not test:
                if test or not test:
                    parts.append(part)

    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    

    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_backboard(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    #oobb_base.append_full(thing,**p3)
    
    #add nuts
    start_x = -width/2 * 15 + 15/2
    start_y = -height/2 * 15 + 15/2
    for col in range(width):
        for row in range(height):
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oobb_nut"                
            p3["radius_name"] = "m3"
            p3["extra_clearance"] = -0.5
            #p3["m"] = "#"
            p3["hole"] = True
            pos1 = copy.deepcopy(pos)         
            pos1[0] += start_x + 15 * col
            pos1[1] += start_y + 15 * row
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)
            # add cylinder in same spot
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "positive"
            p3["shape"] = f"rounded_rectangle"
            wid = 10
            hei = 10
            dep = depth
            size = [wid, hei, dep]
            p3["size"] = size            
            #p3["m"] = "#"
            pos11 = copy.deepcopy(pos1)
            #pos11[2] += depth
            p3["pos"] = pos11
            oobb_base.append_full(thing,**p3)

    #add joiners
    if True:
        beam_height = 2
        beam_depth = 2
        for col in range(width):
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "positive"
            p3["shape"] = f"rounded_rectangle"
            p3["radius"] = 1
            wid = (width * 15)
            hei = beam_height
            dep = beam_depth
            size = [wid, hei, dep]
            p3["size"] = size
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)
            pos1[0] += 0
            pos1[1] += -height/2 * 15 + 15/2 + col * 15
            pos1[2] += 0
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)

        for row in range(height):
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "positive"
            p3["shape"] = f"rounded_rectangle"
            p3["radius"] = 1
            hei = (height * 15)
            wid = beam_height
            dep = beam_depth
            size = [wid, hei, dep]
            p3["size"] = size
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)
            pos1[0] += -width/2 * 15 + 15/2 + row * 15
            pos1[1] += 0
            pos1[2] += 0
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)




    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    #oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_test(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    #oobb_base.append_full(thing,**p3)

    #add ball run tests
    if True:
        rad = 3
        gap = 10
        clear = 0.25/2
        rad_full = 5
        times = 4
        if "6_mm" in extra:
            rad = 6/2
            clear = 0.35/2
            rad_full = rad + clear
            gap = 7.5
            times = 5
        
        
        
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_cylinder"
        dep = 45
        p3["depth"] = dep
        p3["m"] = "#"
        rot1 = copy.deepcopy(rot)
        rot1[0] += 90
        p3["rot"] = rot1
        start_y = -times/2 * gap + gap/2
        for i in range(times):
            p4 = copy.deepcopy(p3)
            pos1 = copy.deepcopy(pos)
            pos1[0] += start_y + i * gap
            pos1[1] += dep/2
            pos1[2] += dep/2 + i * 1
            p4["pos"] = pos1
            p4["radius"] = rad_full
            oobb_base.append_full(thing,**p4)


        
    
    




    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_u_turn(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos) 
    pos1[0] += width/2 * 15
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    

    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    #oobb_base.append_full(thing,**p3)

    #add hole
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_hole"         
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        p3["m"] = "#"
        poss = []

        pos1 = copy.deepcopy(pos)         
        
        pos11 = copy.deepcopy(pos1)
        pos11[0] += 7.5
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += 15
        pos12[1] += 15
        poss.append(pos12)
        pos13 = copy.deepcopy(pos1)
        pos13[0] += 15
        pos13[1] += -15
        poss.append(pos13)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

    #add oring
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oring"         
        p3["depth"] = radius_ball_6_mm * 2
        p3["id"] = 15 - radius_6_mm/2#15 - radius_ball_6_mm/2        
        p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[0] += 0
        pos1[2] += depth - 6/2 + shift_up
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_flat(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    size_ball = kwargs.get("size_ball", "6_mm")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add plate uppies
    shift_left = width/2 * 15 - 15/2
    shift_right = -width/2 * 15 + 15/2
    shift_z = 15/2
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_plate"    
        p3["width"] = 1
        p3["height"] = 2
        p3["depth"] = depth
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[1] += shift_z
        #pos1[2] += depth
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[0] += shift_left
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += shift_right
        poss.append(pos12)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

    #add holes
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_hole"         
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[1] += 15
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[0] += shift_left
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += shift_right
        poss.append(pos12)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    #oobb_base.append_full(thing,**p3)

    #add ball run
    if True:  
        if size_ball == "6_mm":  
            rad = 6/2
            clear = clear_6_mm_diameter #0.35/2 2 mm push fell out 1 mm push too tight #0.25/2 worked on the 2 mm push one
            rad_full = rad + clear
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_cylinder"
        dep = width * 15
        p3["depth"] = dep
        #p3["m"] = "#"
        rot1 = copy.deepcopy(rot)
        rot1[1] += 90
        p3["rot"] = rot1
        pos1 = copy.deepcopy(pos)
        pos1[0] += -dep/2
        pos1[1] += 0
        pos1[2] += dep/2 + depth - rad + shift_up
        p3["pos"] = pos1
        p3["radius"] = rad_full
        oobb_base.append_full(thing,**p3)


        
    
    




    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)