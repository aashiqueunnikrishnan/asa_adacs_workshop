# Determine Andromeda location in ra/dec degrees

# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'
import numpy as np
import argparse
def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser

def clip_to_radius(ra, dec, RA, DEC, radius):
    within_ra = []
    within_dec = []
    for i in range(len(ra)):
        dist = np.sqrt((ra[i]-RA)**2 + (dec[i] - DEC)**2)
        if dist< radius:
            within_ra.append(ra[i])
            within_dec.append(dec[i])
    return within_ra, within_dec
# convert to decimal degrees
from math import cos, sin, pi

d, m, s = DEC.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = RA.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/cos(dec*pi/180)

nsrc = 1_000_000

# make 1000 stars within 1 degree of Andromeda
from random import uniform
ras = []
decs = []
for i in range(nsrc):
    ras.append(ra + uniform(-1,1))
    decs.append(dec + uniform(-1,1))

ras, decs = clip_to_radius(ras, decs, ra, dec, 5)
# now write these to a csv file for use by my other program
with open('catalog.csv','w') as f:
    print("id,ra,dec", file=f)
    for i in range(len(ras)):
        print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
