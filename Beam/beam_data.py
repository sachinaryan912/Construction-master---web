#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python.exe

# Import modules for CGI handling 
import cgi

 

import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

table4_1 = pd.read_excel('C:/xampp/htdocs/projects/construction master/Beam/Table 4_1.xlsx')
table4_4 = pd.read_excel('C:/xampp/htdocs/projects/construction master/Beam/Table 4_4.xlsx')
table5_1 = pd.read_excel('C:/xampp/htdocs/projects/construction master/Beam/Table 5_1.xlsx')
table20 = pd.read_excel('C:/xampp/htdocs/projects/construction master/Beam/Table 20.xlsx')
table19 = pd.read_excel('C:/xampp/htdocs/projects/construction master/Beam/Table 19.xlsx')
clause26_2_1_1 = pd.read_excel('C:/xampp/htdocs/projects/construction master/Beam/clause 26_2_1_1.xlsx')


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ('<meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0">')

print ('<link rel="shortcut icon" type="image/x-icon" href="../images/favicon.png" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet"><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js"></script>')
print ('<link rel="stylesheet" href="../plugins/bootstrap/bootstrap.min.css"><link rel="stylesheet" href="../plugins/themify-icons/themify-icons.css"><link rel="stylesheet" href="../plugins/slick/slick.css"><link rel="stylesheet" href="../plugins/slick/slick-theme.css"><link rel="stylesheet" href="../plugins/fancybox/jquery.fancybox.min.css"><link rel="stylesheet" href="../plugins/aos/aos.css"><link href="../css/style.css" rel="stylesheet"><link href="../css/style2.css" rel="stylesheet">')
print ('<title>Beam result</title>')
print ('<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>')
print ("</head>")
print ("<body>")
print ('<nav class="navbar main-nav navbar-expand-lg px-2 px-sm-0 py-2 py-lg-0"><div class="container"><a class="navbar-brand" href="../index.html"><img src="../images/logo.png" alt="logo"></a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span class="ti-menu"></span></button><div class="collapse navbar-collapse" id="navbarNav"><ul class="navbar-nav ml-auto"><li class="nav-item dropdown active"><a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown">Home</a></li><li class="nav-item dropdown @@pages"><a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown">Teams<span><i class="ti-angle-down"></i></span></a><ul class="dropdown-menu"><li><a class="dropdown-item @@team" href="">Sachin kumar</a></li><li><a class="dropdown-item @@career" href="">Shanu anand</a></li><li><a class="dropdown-item @@blog" href="">Aman raj</a></li><li><a class="dropdown-item @@blogSingle" href="">Shashank Bhushan</a></li></ul></li><li class="nav-item @@about"><a class="nav-link" href="about.html">About</a></li><li class="nav-item @@contact"><a class="nav-link" href="contact.html">Contact</a></li><li class="nav-item @@login" ><a class="nav-link" href="cgitestfile/test.html">Login</a></li></ul></div></div></nav><div class="container-fluid pt-5" style="background-color: #f9f9f9;"><div class="container"><h2 class="text-center">Beam Result data</h2>')

# Create instance of FieldStorage 
form = cgi.FieldStorage()

#get data from form

beam_span = form.getvalue('beam_span')
depth_beam = form.getvalue('depth_beam')
width_beam = form.getvalue('width_beam')
live_load = form.getvalue('live_load')
imp_load = form.getvalue('imp_load')
floor_finish = form.getvalue('floor_finish')

# Get data from fields
if form.getvalue('steel_grade'):
   st_grade = form.getvalue('steel_grade')
else:
   st_grade = "Not set"

if form.getvalue('concrete_grade'):
   concrete_grade = form.getvalue('concrete_grade')
else:
   concrete_grade = "Not set"

if form.getvalue('evendia_bar'):
   drc = form.getvalue('evendia_bar')
else:
   drc = "Not set"

if form.getvalue('tensiondia_bar'):
   drt = form.getvalue('tensiondia_bar')
else:
   drt = "Not set"

if form.getvalue('single_tension_bar'):
   drts = form.getvalue('single_tension_bar')
else:
   drts = "Not set"


beam_span = float(beam_span)
overall_depth_beam = float(depth_beam)
width_beam = float(width_beam)
live_load = float(live_load)
imposed_load = float(imp_load)
floor_finish = float(floor_finish)
fy = int(st_grade)
fck = int(concrete_grade)

# inputs to be taken
# beam_span = float(input("Enter beam span in  meter: "))
# overall_depth_beam = float(input("Enter depth of beam(mm): "))
# width_beam = float(input("Enter the width of beam(mm): "))
# live_load = float(input("Enter live load in kN/m: "))
# imposed_load = float(input("Enter imposed load in kN/m: "))
# floor_finish = float(input("Enter floor finish in kN/m: "))
# fy = int(input("Enter the value of steel grade(250,415,500): "))
# fck = int(input("Enter the value of concrete grade(20, 25, 30, 35, 40): "))


self_weight_beam = 25* (overall_depth_beam/1000) * (width_beam/1000)
total_load = live_load + imposed_load + floor_finish + self_weight_beam
factored_load = 1.5* total_load
design_moment = (factored_load * (beam_span**2))/8
design_shear_force = (factored_load * beam_span)/2
effective_cover = table4_4.iloc[0,int(fck/5)-3]
effective_depth_beam = overall_depth_beam - effective_cover
if (fy==250):
    x_u = 0.53 * (effective_depth_beam/1000)
elif (fy==415):
    x_u = 0.48 * (effective_depth_beam/1000)
else:
    x_u = 0.46 * (effective_depth_beam/1000)


limiting_moment_resistance = 0.36 * fck * (width_beam) * x_u * ((effective_depth_beam/1000) - (x_u *0.42))


# print(f"limiting moment: {limiting_moment_resistance}, design _moment: {design_moment}")
print ('<p><span>Limiting Moment : </span> <span style="font-weight: bold; color: #2e7eed;">%s</span></p>' %limiting_moment_resistance)
print ('<p><span>Design Moment : </span> <span style="font-weight: bold; color: #2e7eed;">%s</span></p>' %design_moment)

if (limiting_moment_resistance < design_moment):
    print('<p style="font-weight : bold;">Doubly reinforcement beam is required</p>')
    
    index_temp_y = int(np.floor(((effective_cover/ effective_depth_beam)*100)/5))
    if ((effective_cover/ effective_depth_beam)<0.05):
        fsc =min((( 0.0035 * (x_u * 1000 - effective_cover)*200000)/(x_u * 1000)), 0.87*fy)
    else:
        if (fy == 250):
            fsc = ((table5_1.iloc[1,index_temp_y] + (((effective_cover/ effective_depth_beam)-table5_1.iloc[0,index_temp_y])*(0.5/(table5_1.iloc[1,index_temp_y +1] - table5_1.iloc[1,index_temp_y])))),0.87*fy)

        elif (fy == 415):
            fsc = ((table5_1.iloc[2,index_temp_y] + (((effective_cover/ effective_depth_beam)-table5_1.iloc[0,index_temp_y])*(0.5/(table5_1.iloc[2,index_temp_y +1] - table5_1.iloc[2,index_temp_y])))),0.87*fy)

        else:
            fsc = ((table5_1.iloc[3,index_temp_y] + (((effective_cover/ effective_depth_beam)-table5_1.iloc[0,index_temp_y])*(0.5/(table5_1.iloc[3,index_temp_y +1] - table5_1.iloc[3,index_temp_y])))),0.87*fy)
    
    
    
    
    Asc = ((design_moment - limiting_moment_resistance)/(fsc * (effective_depth_beam - effective_cover)))*(10**6)
    # bars required to be taken
    if (Asc < 100):
        
        diameter_rod_compression = 8
        number_bars_compression = 2
        print('<p style="font-weight : bold;">you need <span style="font-weight: bold; color: #2e7eed;">%s</span> number of compression bars of diameter <span style="font-weight: bold; color: #2e7eed;">%s</span> mm</p>' %(number_bars_compression, diameter_rod_compression))
        # print(f"you need {number_bars_compression} compresssion bars of diameter {diameter_rod_compression}")
        
    else:
        bars_diameter = np.array([8,10,12,14,16,18,20,22,25,28,32,40])
            
        for i in range(len(bars_diameter)):
            number_bars_available = np.ceil((Asc/((np.pi)* (1/4) * (bars_diameter[len(bars_diameter)-i-1] **2))))
            
            if (number_bars_available >=2 and ((width_beam - (number_bars_available * bars_diameter[len(bars_diameter)-i-1]))/(number_bars_available-1)) >= 25 ):
                break
            else:
                continue
            i += 1
        print ('<div class="alert alert-info mt-1"><p style="color : #ff0000;">Area of steel in compression > 100..to get number of compression bar enter diameter of bar <a href="./beam_input2.html" style="font-weight : bold; color: #2e7eed;">click here</a></p></div>')
        diameter_rod_compression = int(drc)
        # diameter_rod_compression = int(input(f"Enter the the diameter of bar you want to take in mm{bars_diameter[:len(bars_diameter)-i-1]}: "))
        number_bars_compression = int(np.ceil((Asc/((np.pi)* (1/4) * (diameter_rod_compression **2)))))
        print('<p style="font-weight : bold;">you need <span style="font-weight: bold; color: #2e7eed;">%s</span> number of compression bars of diameter <span style="font-weight: bold; color: #2e7eed;">%s</span> mm</p>' %(number_bars_compression, diameter_rod_compression))
        # print(f"you need {number_bars_compression} compresssion bars of diameter {diameter_rod_compression}")
    
    
    Ast = (design_moment/(0.87*fy*(effective_depth_beam - 0.42*(x_u*1000))))*(10**6)
    
    #bars details required
    if (Ast < 226):
        diameter_rod_tension = 12
        number_bars_tension = 2
        print('<p style="font-weight : bold;">you need <span style="font-weight: bold; color: #2e7eed;">%s</span> tension bars of diameter <span style="font-weight: bold; color: #2e7eed;">%s</span></p>' %(number_bars_tension, diameter_rod_tension))
        # print(f"you need {number_bars_tension} tension bars of diameter {diameter_rod_tension}")
    else:
        bars_diameter = np.array([12,14,16,18,20,22,25,28,32,40])
            
        for i in range(len(bars_diameter)):
            number_bars_available = np.ceil((Ast/((np.pi)* (1/4) * (bars_diameter[len(bars_diameter)-i-1] **2))))
            
            if (number_bars_available >=2 and ((width_beam - (number_bars_available * bars_diameter[len(bars_diameter)-i-1]))/(number_bars_available-1)) >= 25 ):
                break
            else:
                continue
            i += 1

        print ('<div class="alert alert-info mt-1"><p style="color : #ff0000;">Area of steel in tension is greater than 226..To get number of tension bar enter diameter of bar <a href="./beam_input3.html" style="font-weight : bold; color: #2e7eed;">click here</a></p></div>')
        diameter_rod_tension = int(drt)
        # diameter_rod_tension = int(input(f"Enter the the diameter of bar you want to take in mm{bars_diameter[:len(bars_diameter)-i-1]}: "))
        number_bars_tension = int(np.ceil((Ast/((np.pi)* (1/4) * (diameter_rod_tension **2)))))
        print('<p style="font-weight : bold;">you need <span style="font-weight: bold; color: #2e7eed;">%s</span> number of tension bars of diameter <span style="font-weight: bold; color: #2e7eed;">%s mm</span></p>' %(number_bars_tension, diameter_rod_tension))
        # print(f"you need {number_bars_tension} tension bars of diameter {diameter_rod_tension}")
    
    
    #location of bent up bar
    i = 1
    position=np.array([])
    while(i * (np.sqrt(2)*(effective_depth_beam - (x_u*1000))) < (beam_span*1000)/4):
        
        position = np.append(position, i * (np.sqrt(2)*(effective_depth_beam - (x_u*1000))))
        i += 1
    parts_beam =i
    factored_shear_force = (factored_load * beam_span)/2
    
    nominal_shear_stress = (factored_shear_force / (width_beam*effective_depth_beam))*(10**3)
    max_shear_stress = table20.iloc[0,int((fck/5)-3)]
    if (nominal_shear_stress > max_shear_stress):
        print(f"M{fck} concrete can hold that please change concrete grade and calculations below are useless !!!\n\n\n")
    else :

        #for bars at position greater than 2
        percentage_reinforcement_support = ((number_bars_tension ) * (np.pi/4) * (diameter_rod_tension **2) *100)/(effective_depth_beam * width_beam)
        if (( fck - 10)/5 <= 6):
            concrete_index_y = int(( fck - 10)/5)
        else:
            concrete_index_y = 6
        if (percentage_reinforcement_support<= 0.15):
            concrete_index_x = 1
            torque_c = .28
        elif (percentage_reinforcement_support >= 3):
            concrete_index_x = 13
            torque_c = .71
        else:
            concrete_index_x = int((np.floor(percentage_reinforcement_support*100))//25) + (1)
            torque_c = (((percentage_reinforcement_support - table19.iloc[concrete_index_x,0])*(table19.iloc[concrete_index_x,concrete_index_y]-table19.iloc[concrete_index_x+ 1,concrete_index_y ]))/(table19.iloc[concrete_index_x,0]-table19.iloc[concrete_index_x+ 1,0 ])) + table19.iloc[concrete_index_x,concrete_index_y]
        v_cu = (torque_c* width_beam* effective_depth_beam)*(10**(-3))
        

        #looping the portions
        percentage_reinforcement_support = ((number_bars_tension - np.floor(number_bars_tension/3)) * (np.pi/4) * (diameter_rod_tension **2) *100)/(effective_depth_beam * width_beam)
        for i in range(0,parts_beam):
            if (i==0):
            
                if (( fck - 10)/5 <= 6):
                    concrete_index_y = int(( fck - 10)/5)
                else:
                    concrete_index_y = 6
                if (percentage_reinforcement_support<= 0.15):
                    concrete_index_x = 1
                    torque_c = .28
                elif (percentage_reinforcement_support >= 3):
                    concrete_index_x = 13
                    torque_c = .71
                else:
                    concrete_index_x = int((np.floor(percentage_reinforcement_support*100))//25) + (1)
                    torque_c = (((percentage_reinforcement_support - table19.iloc[concrete_index_x,0])*(table19.iloc[concrete_index_x,concrete_index_y]-table19.iloc[concrete_index_x+ 1,concrete_index_y ]))/(table19.iloc[concrete_index_x,0]-table19.iloc[concrete_index_x+ 1,0 ])) + table19.iloc[concrete_index_x,concrete_index_y]
                v_cu = (torque_c* width_beam* effective_depth_beam)*(10**(-3))
                v_u = factored_shear_force
                v_us = v_u - v_cu
                spacing = min((0.87* fy* 2*(np.pi/4)*(8**2) * effective_depth_beam)/(v_us/2), (0.87* fy* 2*(np.pi/4)*(8**2)/(0.4*width_beam)), min((00.75* effective_depth_beam), 300))
                print ('<p>For portion <span style="font-weight : bold; color: #2e7eed;">%s</span> provide 2 legged <span style="font-weight : bold; color: #2e7eed;">8mm </span> diameter bars at <span style="font-weight : bold; color: #2e7eed;">%s mm</span> of spacing.</p>' %(i+1, spacing))
                # print(f"for portion 1 provide 2 legged 8mm diameter bars at {spacing}mm")
                
            else:
                
                if (( fck - 10)/5 <= 6):
                    concrete_index_y = int(( fck - 10)/5)
                else:
                    concrete_index_y = 6
                if (percentage_reinforcement_support<= 0.15):
                    concrete_index_x = 1
                    torque_c = .28
                elif (percentage_reinforcement_support >= 3):
                    concrete_index_x = 13
                    torque_c = .71
                else:
                    concrete_index_x = int((np.floor(percentage_reinforcement_support*100))//25) + (1)
                    torque_c = (((percentage_reinforcement_support - table19.iloc[concrete_index_x,0])*(table19.iloc[concrete_index_x,concrete_index_y]-table19.iloc[concrete_index_x+ 1,concrete_index_y ]))/(table19.iloc[concrete_index_x,0]-table19.iloc[concrete_index_x+ 1,0 ])) + table19.iloc[concrete_index_x,concrete_index_y]
                v_cu = (torque_c* width_beam* effective_depth_beam)*(10**(-3))
                distance_v_cu = ((beam_span*1000)/2)*(v_cu / factored_shear_force)
                v_u= ((((beam_span*1000)/2) - position[0] - ((i-1) * ((((beam_span*1000)/2)- position[0])/parts_beam)) ) /((beam_span*1000)/2) ) * factored_shear_force
                v_us = v_u - v_cu 
                if (v_us > 0):
                    spacing = min((0.87* fy* 2*(np.pi/4)*(8**2) * effective_depth_beam)/(v_us), (0.87* fy* 2*(np.pi/4)*(8**2)/(0.4*width_beam)), min((00.75* effective_depth_beam), 300))

                    value_1 = (((beam_span*1000)/2) - position[0] - ((i-1) * ((((beam_span*1000)/2)- position[0])/parts_beam)) )

                    portion_no = i+1

                    print ('<p>Portion <span style="font-weight : bold; color: #2e7eed;">%s</span> starts at <span style="font-weight : bold; color: #2e7eed;">%s</span> from mid of span and provide 2 legged 8mm diameter bars at <span style="font-weight : bold; color: #2e7eed;">%s mm</span> of spacing</p>' %(portion_no, value_1, spacing))

                    # print(f"portion {i+1} starts at {(((beam_span*1000)/2) - position[0] - ((i-1) * ((((beam_span*1000)/2)- position[0])/parts_beam)) )} from mid of span and provide 2 legged 8mm diameter bars at {spacing}mm ")
                else:

                    value_2 = (((beam_span*1000)/2) - position[0] - ((i-1) * ((((beam_span*1000)/2)- position[0])/parts_beam)) )

                    portion_nos = i+1

                    print ('<p>Portion <span style="font-weight : bold; color: #2e7eed;">%s</span> starts at <span style="font-weight : bold; color: #2e7eed;">%s</span> from mid of span and provide 2 legged 8mm diameter bars at <span style="font-weight : bold; color: #2e7eed;">250 mm</span> of spacing</p>' %(portion_nos, value_2))

                    # print(f"portion {i+1} starts at {(((beam_span*1000)/2) - position[0] - ((i-1) * ((((beam_span*1000)/2)- position[0])/parts_beam)) )} from mid of span and provide 2 legged 8mm diameter bars at 250 mm ")

    #development length
    development_length_compression = (diameter_rod_compression * 0.87*fy)/(4*1.6*clause26_2_1_1.iloc[0,int ((fck/5)-3)])
    development_length_tension = (diameter_rod_tension * 0.87*fy)/(4*1.6*clause26_2_1_1.iloc[0,int((fck/5)-3)])
    print('<p>Development length compression in mm : <span style="font-weight : bold; color: #2e7eed;">%s mm</span></p>' %development_length_compression)
    # print(f"Development length compression in mm {development_length_compression}")
    print('<p>Development length tension in mm : <span style="font-weight : bold; color: #2e7eed;">%s mm</span></p>' %development_length_tension)
    # print(f"Development length tension in mm {development_length_tension}")
    
    #deflection check
    fs = 0.58 * fy *(Ast/(number_bars_tension * ((np.pi)* (1/4) * (diameter_rod_tension **2))))
            
    if((beam_span) > 10):
        beta =  10/beam_span
    else:
        beta = 1
    
    gamma = min(1/(0.225 + (0.0032 *fs) + (0.625/2.303)*np.log(percentage_reinforcement_support)),2)
    percentage_variable = (100*Asc)/(width_beam * effective_depth_beam)
    lmda = min(((1.6 * percentage_reinforcement_support)/(percentage_reinforcement_support + 0.275)),1.5)
    
    if(((beam_span *1000)/overall_depth_beam) > (26*beta*gamma*lmda)):
        print("sahi data lo na baby ji")


else:
    print('<p style="font-weight : bold;">Singly reinforcement beam is required</p>')
    # print("Singly reinforcement beam is required")
    Asc = 0
    print('<p style="font-weight : bold;">Area of steel in compression is zero. So We take 2 bars of 8mm diameter.</p>')
    # print("We take 2 8mm bars above as Asc =0 ")
    Ast = (0.362 * fck * width_beam * (x_u*1000))/(0.87*fy) 
    
    
    # bar details required
    if (Ast < 226):
        print('<p style="font-weight : bold;">Take 2 bars of 12mm diameter.</p>')
        # print("Take 2 12mm bars")
    else:
        bars_diameter = np.array([12,14,16,18,20,22,25,28,32,40])
            
        for i in range(len(bars_diameter)):
            number_bars_available = np.ceil((Ast/((np.pi)* (1/4) * (bars_diameter[len(bars_diameter)-i-1] **2))))
            
            if (number_bars_available >=2 and ((width_beam - (number_bars_available * bars_diameter[len(bars_diameter)-i-1]))/(number_bars_available-1)) >= 25 ):
                break
            else:
                continue
            i += 1

        print ('<div class="alert alert-info"><p style="color : #ff0000;">Area of steel in tension is greater than 226..To get number of tension bar enter diameter of bar <a href="./beam_singly.html" style="font-weight : bold; color: #2e7eed;">click here</a></p></div>')
        diameter_rod_tension = int(drts)
        # diameter_rod_tension = int(input(f"Enter the the diameter of bar you want to take in mm{bars_diameter[:len(bars_diameter)-i-1]}: "))
        number_bars_tension = np.ceil((Ast/((np.pi)* (1/4) * (diameter_rod_tension **2))))
        print('<p style="font-weight : bold;">you need <span style="font-weight : bold; color: #2e7eed;">%s</span> number of tension bars of diameter <span style="font-weight : bold; color: #2e7eed;">%s mm</span></p>' %(number_bars_tension, diameter_rod_tension))
        # print(f"you need {number_bars_tension} tension bars of diameter {diameter_rod_tension}")


print ('</div></div><div class="footer mt-5"></div>')

print ("</body>")

print ("</html>")