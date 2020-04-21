import math
import sys
ab=int(input())
bc=int(input())
rad=math.atan2(ab,bc)
deg=math.degrees(rad)
sys.stdout.write("{0:.0f}".format(deg)+'°')
