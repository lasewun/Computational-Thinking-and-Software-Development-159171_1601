##Exercise B. - Roger Gilbertson 17.03.16

#math module
import math

#functions
def VolumeOfSphere():                               #defining/function name
    VolumeOfSphere = (((4/3.0)*math.pi)*2**3)       #calculation of sphere
    return VolumeOfSphere                           #returning/saving of value

#print(VolumeOfSphere())                            #commented out code to test that value was saved

def CombinedResistance():                           #defining/function name
    R1 = (5)                                        #resistance values
    R2 = (10)
    R3 = (20)
    CombinedResistance = (1/((1/R1)+(1/R2)+(1/R3))) #calculation of resistance
    return CombinedResistance                       #returning/saving of value

#print(str(CombinedResistance()))                   #commented out code to test that value was saved

def CovertCdegreeToFdegree():                       #defining/function name
    Cvalue = 20                                     #centigrde value
    Fdegree = (Cvalue * 9 / 5 + 32)                 #calculation for conversion
    print(Fdegree)                                  #printing of converted value

#CovertCdegreeToFdegree()                           #commented out call of function for testing

def EqnFunction():                                  #defining/function name
    Num1 = float(input('enter numeric value : '))   #input of user value
    EqnFunction = (3*Num1**2-5*Num1+10)             #calculation/equation
    print(EqnFunction)                              #print function of value

#EqnFunction()                                      #commented out call of function for testing