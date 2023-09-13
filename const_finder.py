import astropy.units as u
from astropy.coordinates import SkyCoord
import astropy.coordinates
ra = str(input("Enter the Star's RA in hh:mm:ss format: "))
dec = str(input("Enter the Star's Dec in dd:mm:ss format: "))
coords = SkyCoord(ra, dec, unit = (u.hourangle, u.deg))
const = astropy.coordinates.get_constellation(coords, short_name=False, constellation_list = 'iau')
print('Your star is in {} constellation'.format(const))