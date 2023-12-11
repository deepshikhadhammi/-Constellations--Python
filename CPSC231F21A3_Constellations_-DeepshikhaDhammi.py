# CLASS CPSC 231 FALL 2021
# NAME: DEEPSHIKHA DHAMMI
# TUTORIAL :T08
#STUDENT ID :30140157
#DATE : NOVEMBER 23,2021
#DESCRIPTION : #The program draws xaxis and y axis o the turtle scree window
# The program asks user to enter valid stars input files until the user enters''. Once a valid stars file is given the program
#asks user to enter a constellation file. Thereafter read stars function read constellation function and draw constellation
#function is called to draw the constellations and stars on the turtle window.
# If the user enters -names as an argument then name of stars is also displayed on the screen



import sys
import turtle
import os
BACKGROUND_COLOR = "black"
WIDTH = 600
HEIGHT = 600
# AXIS CONSTANTS
AXIS_COLOR = "blue"
RATIO=300
INITIAL_VALUE=-1
STEP=0.25
X_ORIGIN=300
Y_ORIGIN=300
# STAR CONSTANTS
STAR_COLOR = "white"
STAR_COLOR2 = "grey"
# X AXIS OFFSETS
OFFSET_X_TICK=8
OFFSET_X1_LABEL=1
OFFSET_X2_LABEL=23
# Y AXIS OFFSETS
OFFSET_Y_TICK=8
OFFSET_Y_LABEL1=28
OFFSET_Y_LABEL2=10

def setup():
    """
    Setup the turtle window and return drawing pointer
    :return: Turtle pointer for drawing
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.delay(delay=0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer

def read_star(filename):


    infile = open(filename, 'r')  #read the stars file  entered by the user
    lines = infile.readlines()   #read every line of the file
    name=[]
    dict={}
    star_list=[]
    for line in lines:  #read every line in lines
      sline=line.strip()   #remove whitespaces
      sline = sline.split(',') # separates line into a list of items.  ',' tells it to split the lines at the commas
      for i in sline:   # split names from the sline list
        name=i.split(';')   #name [] stores the list of the names splitted at ';'
      x=sline[0]        #stores x coordinate of star location
      y=sline[1]        #stores y coordinate of star location
      mag=sline[4]      #stores magnitude of stars
      stars=[]          #list to store x,y, magnitude and name of stars
      stars.append(x)   #add x location to the list
      stars.append(y)   #add y location to the list
      stars.append(mag)  #add magnitude to the list
      stars.append(name)  #add name to the list
      star_list.append(stars) #store star[] into another list
      if(len(name)>=1 and name[0]!=''):
          for j in range(len(name)): #store names into a dictionary
              str=name[j]
              dict[str]=stars      #stores star information as a value for every key which is the name of the star

      for key in dict:     #printing the information for named stars in a dictionary
         keyvalue=dict[key]
         print ("%s is at (%s,%s) with magnitude %s"%(key,keyvalue[0],keyvalue[1],keyvalue[2])) #prints the name of the constellation along with the name of stars

    infile.close()    #closing the file

    return star_list,dict

def draw_axis(pointer):
    """
    Draw the x axis and y axis by converting the coordinates, drawing ticks and labels with a step value of 0.25
    :return: None
    """
    pointer.color(AXIS_COLOR)  #draw axis in blue colour
    pointer.up()
    pointer.goto(0,HEIGHT/2) #drawing x axis starting from WIDTH=0
    pointer.down()
    pointer.goto(WIDTH,HEIGHT/2)#x axis drawn till WIDTH=600
    pointer.up()
    pointer.goto(WIDTH/2,0) #draw y axis
    pointer.down()
    pointer.goto(WIDTH/2,HEIGHT)# y axis drawn till HEIGHT=600
    pointer.up()
    value=-1.00   #value stores label position
    coordinate_x=X_ORIGIN+RATIO*value #converting x value into turtle screen coordinate
    while coordinate_x<=WIDTH:  #drawing x axis labels and ticks within the given screen
        pointer.goto(coordinate_x,Y_ORIGIN+OFFSET_X_TICK) #draw ticks
        pointer.down()
        pointer.goto(coordinate_x,Y_ORIGIN-OFFSET_X_TICK)
        pointer.up()
        pointer.goto(coordinate_x-OFFSET_X1_LABEL,Y_ORIGIN-OFFSET_X2_LABEL)
        if(value!=0.00):
         pointer.write("%.2f"%(value)) #write x axis label
        value=value+STEP #increase the value of label by adding step
        coordinate_x=X_ORIGIN+RATIO*value #converting x value into turtle screen coordinate
    value=-1.00  #value stores label position
    coordinate_y=Y_ORIGIN+RATIO*value #convert y value into turtle screen coordinate
    while coordinate_y<=HEIGHT:  #drawing y labels and ticks within a given screen
        coordinate_y=Y_ORIGIN+RATIO*value #converting y value into turtle screen coordinates
        pointer.goto(X_ORIGIN+OFFSET_Y_TICK,coordinate_y) #drawing ticks on y axis
        pointer.down()
        pointer.goto(X_ORIGIN-OFFSET_Y_TICK,coordinate_y)
        pointer.up()
        pointer.goto(X_ORIGIN-OFFSET_Y_LABEL1,coordinate_y-OFFSET_Y_LABEL2) # label
        if(value!=0):
         pointer.write("%.2f"%(value))  #writing label
        value=value+STEP  #increase the value of label

    pointer.up()
    return None
def draw_star(pointer,star_info,named_star,word):

     for k in range(len(star_info)): #looping through the list that contains star information(x,y,mag,names)
         diameter=10/(float((star_info[k][2]))+2)  #calculating diameter
         screen_x=X_ORIGIN+RATIO*float(star_info[k][0])   #converting x coordinate into turtle screen coordinate
         screen_y=Y_ORIGIN+RATIO*float(star_info[k][1]) #converting y coordinate into turtle screen coordinate


         pointer.goto(screen_x,screen_y)   #going to star location
         pointer.color(STAR_COLOR2)    #star is not named so it will be drawn in grey
         pointer.down()

         pointer.dot(diameter)       # draw filled star
         if(word=="-names" and star_info[k][3][0]!=''): #prints the first name of star
          pointer.color(STAR_COLOR)
          pointer.write(star_info[k][3][0],font=("Arial",5,"normal")) #writes the first name of star in white
         pointer.up()

     for key in named_star:   #looping through a dictionary to draw named stars in white
          keyvalues=named_star[key] #accessing the value of every key in a dictionary

          screen_x=X_ORIGIN+RATIO*float(keyvalues[0]) #converting the x coordinate into turtle screen coordinates
          screen_y=Y_ORIGIN+RATIO*float(keyvalues[1]) #converting the y coordinate into turtle screen coordinates
          diameter=10/(float((keyvalues[2]))+2)   #calculating diameter
          pointer.up()
          pointer.goto(screen_x,screen_y)  #going to x,y location of the star
          pointer.down()
          pointer.color(STAR_COLOR)         #draws the star in white

          pointer.dot(diameter)           #draws filled star

     pointer.up()
def read_constellation(const_file):   #function that reads constellation files entered by the user
     const_list=[]                   #list to store constellations

     const_star_list=[]             #list that contains the edges
     if(os.path.isfile(const_file)==True):
         c_file=open(const_file,'r')   #open constellation file
         line=c_file.readlines()       #read every line of the file

         name_cons=line[0].strip()     #stores the first name of every file that is a constellation name

         for item in line:             #looping through every line of the constellation file
            if(item!=line[0]):
             value=item.strip()        #removes spaces
             value= value.split(',')   #splits the string into a list
             const_list.append(value)  # list that stores another list of edges
         j=0
         for i in range(len(const_list)): #loop through utems in a constellation list
              star_name1=const_list[i][j]  #accessing the star names
              star_name2=const_list[i][j+1] #accessing star name
              j=0
              const_star_list.append(star_name1)  #adding the star name to constellation star list
              const_star_list.append(star_name2)   #adding the star name to constellation star list

         const_set=set(const_star_list)   #converting the constellation star list to set in order to remove duplicate values
         print("%s constellation contains %s"%(name_cons,const_set))  #print the name of constellation along with the stars
         c_file.close()            #close constellation file
     return const_list              #returns the constellation list to the main function

def draw_constellation(pointer,star_const_dict,star_const,counter):  #function to draw constellation
    for star in star_const:     #looping through star in star constellation
        for i in range(len(star)): #looping through items in a star []

          loc=star_const_dict[star[i]]          # finding the location of the star
          x_point=X_ORIGIN+RATIO*float(loc[0])  #converting the x coordinate into turtle screen cooordinates
          y_point=X_ORIGIN+RATIO*float(loc[1])  #converting the y coordinates into turtle screen coordinate
          if(counter%3==0):         #finds the remainder to use a colour for drawing constellation
              colour="red"          #1st will be drawn in red
          elif(counter%3==1):
              colour="yellow"        #2nd will be in yellow
          else:
              colour="green"         #3rd will be in green
          pointer.color(colour)      #changing the colour of the pointer
          pointer.goto(x_point,y_point)  #going to the desired location to draw the constellation
          pointer.down()
        pointer.up()
def main():
    """
    Main constellation program
    :return: None
    """
    # Handle arguments

    pointer=setup()  #pointer is used to call the setup function
    draw_axis(pointer)  #draws axis
    arguments=len(sys.argv) #calculates the length of the arguments entered by the user

    if(arguments==1): #if only when argument is entered that is the pythonCPSC231A2.py and no argument is entered
        filename=input("Enter the stars file:") #prompt the user to enter the filename as an argument
        if(filename==''): #filename is blank program will exit
            sys.exit()
        elif(os.path.exists(filename)==True): #if file entered by the user exists it will call read_star function
            star_info,named_star=read_star(filename) #calling read_star function to read the file
            draw_star(pointer,star_info,named_star,'') #calling draw star function to draw the star
            constellation=input("Enter constellation file:")  #user input for constellation file
            counter=0                     #counter that determines the colour in which constellation needs to be drawn
            while(constellation!=''):    #continue asking user for constellation files until the user enters''
                star_const=read_constellation(constellation) #read constellation file
                draw_constellation(pointer,named_star,star_const,counter) #calling draw constellation function that draws the constellation
                constellation=input("Enter constellation file:") #user input for constellation
                counter=counter+1   #updating counter value

        elif(os.path.exists(filename)==False): #if the filename entered by user doesnot exist
            filename=input("Enter a valid stars file:") #ask user for a valid filename
            if(filename==''):   #if filename is empty exit the program
                 sys.exit(1)
            if(os.path.exists(filename)==False): #continue asking user for a valid filename for stars
                   filename=input("Enter a valid stars file:")
                   while(os.path.exists(filename)==False):
                        filename=input("Enter a valid stars file:")
                        if(filename==''):
                             sys.exit()
            if(os.path.exists(filename)==True): #if file exists read stars file and draw stars
              star_info,named_star=read_star(filename)#function reads star information
              draw_star(pointer,star_info,named_star,'')# function draws stars
              constellation=input("Enter constellation file:") #ask user for constellation file
              counter=0   #counter to determine color of the constellation
              while(constellation!=''): #continue taking input from the user until the user enters blank
                star_const=read_constellation(constellation) #read constellation file
                draw_constellation(pointer,named_star,star_const,counter)#draw constellations
                constellation=input("Enter constellation file:") #user input for another constellation file
                counter=counter+1 #updates counter

    elif(arguments==2):  # if the user entered<arg1>
        if(sys.argv[1]=="-names"):  # if the argument is name
            filename=input("Enter the stars file:") #prompt the user for a stars input file
            if(filename==''):     #if filename is empty exit the program
                sys.exit(1)
            elif(os.path.exists(filename)==True): # if file exists
              star_info,named_star=read_star(filename) #read stars function to read the stars file
              draw_star(pointer,star_info,named_star,"-names") #call draw stars function to draw the stars
              constellation=input("Enter constellation file:") #ask user for constellation file
              counter=0    # counter to determine the colour of the constellation
              while(constellation!=''):   # if constellation is not '' continue asking user for the constellation files
                star_const=read_constellation(constellation)  # call read constellation function to read the constellation file entered by the user
                draw_constellation(pointer,named_star,star_const,counter) #call draw constellation function to draw the star
                constellation=input("Enter constellation file:") #ask for another constellation file
                counter=counter+1     #update the value of the counter
            elif(os.path.exists(filename)==False):  #if file doesnot exist prompt the user for valid stars file
              filename=input("Enter a valid stars file:") #ask user for a valid filename
              if(filename==''):   #if filename is empty exit the program
                 sys.exit(1)
              if(os.path.exists(filename)==False): #continue asking user for a valid filename for stars
                    filename=input("Enter a valid stars file:")
                    while(os.path.exists(filename)==False):
                         filename=input("Enter a valid stars file:")
                         if(filename==''):
                             sys.exit()
              if(os.path.exists(filename)==True):  #if file entered is valid
                  star_info,named_star=read_star(filename)  #call the read star function to read the file
                  draw_star(pointer,star_info,named_star,"-names")  #draws the star
                  constellation=input("Enter constellation file:") #asks user to enter constellation file
                  counter=0  #determine the colour of the constellation
                  while(constellation!=''): #if constellation is not equal to blank
                   star_const=read_constellation(constellation) #read constellation file
                   draw_constellation(pointer,named_star,star_const,counter) #draws constellations
                   constellation=input("Enter constellation file:") #user enters constellation file
                   counter=counter+1 #updates counter value
        elif(sys.argv[1]!="-names") : # if<arg1> is not names then it will be considered as the filename
            filename=sys.argv[1]
            if(filename==''): #if filename is empty program will exit
                sys.exit(1)
            elif(os.path.exists(filename)==True): #if filename exists
              star_info,named_star=read_star(filename) #read star file
              draw_star(pointer,star_info,named_star,'')# draw stars
              constellation=input("Enter constellation file:") #user enters constellation file
              counter=0 #determines colour of the constellation
              while(constellation!=''): #if constellation is not blank
                star_const=read_constellation(constellation) #read constellations file
                draw_constellation(pointer,named_star,star_const,counter) #draw constellation file
                constellation=input("Enter constellation file:") #user enters next constellation file
                counter=counter+1 #update counter value
            elif(os.path.exists(filename)==False): # if file doesnot exist
                filename=input("Enter a valid stars file:") #ask user for a valid filename
                if(filename==''):   #if filename is empty exit the program
                     sys.exit(1)
                if(os.path.exists(filename)==False): #continue asking user for a valid filename for stars
                     filename=input("Enter a valid stars file:")
                     while(os.path.exists(filename)==False):
                         filename=input("Enter a valid stars file:")
                         if(filename==''):
                            sys.exit()
                if(os.path.exists(filename)==True): #if filename exists
                  star_info,named_star=read_star(filename) #reads star file
                  draw_star(pointer,star_info,named_star,'') #draws stars
                  constellation=input("Enter constellation file:") #asks user for constellation file
                  counter=0 #determines colour of constellation
                  while(constellation!=''): #continue asking user for constellation file until the user enters ''
                   star_const=read_constellation(constellation) #read constellations file
                   draw_constellation(pointer,named_star,star_const,counter) #draw constellation
                   constellation=input("Enter constellation file:") #asks user for next constellation file
                   counter=counter+1 #updates counter value
    elif(arguments==3): #if user enters<arg1><arg2> and one of them is -names and the otheris filename
                if(sys.argv[1]=="-names") :
                    filename=sys.argv[2]
                    if(os.path.exists(filename)==True):#if file exists
                       star_info,named_star=read_star(filename) #read the stars file
                       draw_star(pointer,star_info,named_star,"-names") #draw the stars and their names on the window
                       constellation=input("Enter constellation file:") #ask user to enter consellation file
                       counter=0 #determines colour of the constellation
                       while(constellation!=''):#continue asking for constellations file
                        star_const=read_constellation(constellation) #read constellation file
                        draw_constellation(pointer,named_star,star_const,counter) #draw constellation
                        constellation=input("Enter constellation file:")#enter another constellation file
                        counter=counter+1 #updates counter
                    elif(os.path.exists(filename)==False): #if file doesnot exist
                      filename=input("Enter a valid stars file:") #ask user for a valid filename
                      if(filename==''):   #if filename is empty exit the program
                       sys.exit(1)
                      if(os.path.exists(filename)==False): #continue asking user for a valid filename for stars
                          filename=input("Enter a valid stars file:")
                          while(os.path.exists(filename)==False):
                               filename=input("Enter a valid stars file:")
                               if(filename==''):
                                   sys.exit(1)
                      if(os.path.exists(filename)==True):#if filename exists
                        star_info,named_star=read_star(filename)#read stars file
                        draw_star(pointer,star_info,named_star,"-names") #draw stars
                        constellation=input("Enter constellation file:") #asks user for constellation file
                        counter=0  #determines colour of constellation
                        while(constellation!=''): #continue asking user for constellation file until the user enters''
                         star_const=read_constellation(constellation) #read constellations file
                         draw_constellation(pointer,named_star,star_const,counter) #draw constellations
                         constellation=input("Enter constellation file:") #asks user for another constellation file
                         counter=counter+1 #updates counter value
                elif(sys.argv[2]=="-names") : #if second argument is names
                    if(os.path.exists(sys.argv[1])==True): #if file exists
                       filename=sys.argv[1] #filename will store 1st argument
                       star_info,named_star=read_star(filename)  # read stars file
                       draw_star(pointer,star_info,named_star,"-names") #draws the star and prints the name
                       constellation=input("Enter constellation file:") #asks user for constellation file
                       counter=0   #determines constellation colour
                       while(constellation!=''):  #continue asking user for constellation file until user enters''
                        star_const=read_constellation(constellation)  #read constellations file
                        draw_constellation(pointer,named_star,star_const,counter)  #draw constellation
                        constellation=input("Enter constellation file:")  #enter constellation file
                        counter=counter+1    #updates counter value
                    elif(os.path.exists(sys.argv[1])==False): # if file doesnot exist
                      filename=input("Enter a valid stars file:") #ask user for a valid filename
                      if(filename==''):   #if filename is empty exit the program
                       sys.exit(1)
                      if(os.path.exists(filename)==False): #continue asking user for a valid filename for stars
                          filename=input("Enter a valid stars file:")
                          while(os.path.exists(filename)==False):
                               filename=input("Enter a valid stars file:")
                               if(filename==''):
                                   sys.exit(1)
                      if(os.path.exists(filename)==True): #if filename exists
                        star_info,named_star=read_star(filename) #call read star function to read stars file
                        draw_star(pointer,star_info,named_star,"-names") #draw stars file
                        constellation=input("Enter constellation file:")  #ask for a constellation file
                        counter=0   #counter to determine colour of the constellation
                        while(constellation!=''):  #continue asking for constellation file until the user enters ''
                         star_const=read_constellation(constellation) #read stars constellation file
                         draw_constellation(pointer,named_star,star_const,counter) #draw stars
                         constellation=input("Enter constellation file:") #asks user to enter the constellation file
                         counter=counter+1  #updates counter value
                elif(sys.argv[1]!="-names"  or sys.argv[2]!="-names")  :
                    print("Invalid argument as neither input was -names")
                    sys.exit(1)

    elif(arguments>3): # If user enters too many arguments program will exit
        print("Error: Too many arguments")
        sys.exit(1)





main()

print("\nClick on window to exit!\n")
turtle.exitonclick()


