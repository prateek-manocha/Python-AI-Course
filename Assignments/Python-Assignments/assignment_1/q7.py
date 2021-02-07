'''7. Write a function mean_calculator() to take two floats as input from command line and print the
AM,GM,HM of those numbers.
'''

import math
import arg

def am_gm_hm(f,s):
    am = (f+s)/2
    gm = math.sqrt(f*s) #gm = (f*s)**(1/2)
    hm = (f*s)/(f+s)
    print('AM:'+str(am))
    print('GM: '+str(gm))
    print('HM: '+str(hm))
    return am, gm, hm

args = arg.parser.parse_args()
am_gm_hm(args.f, args.s)
