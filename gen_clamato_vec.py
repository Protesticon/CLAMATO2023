#  Generate pixel data from CLAMATO data, as 1D vectors in
# [x,y,z,delta_F, inverse covariance].
#
#  Similar to dachshund inputs but in a more easily parsable
# form. (actually this basically the 2014 version of gen_dach_input) 

datadir = '~/lya/3d_recon/data/cl2017_redux/'
specdir = datadir + 'spec_v0/' 

Om = 0.31
Olamb = 1. - Om

# This defines the Cartesian zeros for the output map
ra0 = 149.95
dec0 = 2.15  

zmin = 2.15
zmax = 2.55
waveminlya = 1215.67 * (1.+zmin)
wavemaxlya = 1215.67 * (1.+zmax)
zmid = avg([zmin, zmax])

# transverse comoving distance = angular separation(in rad) *
# comoving distance. So evaluate comoving distance
comdist = 2997. * comdis(zmid, Om, Olamb)
# For LOS distances we use a fixed dD/dz evaluated at zmid
dcomdist_dz = dcomdisdz(zmid, Om, Olamb) * 2997.

insp_fil =  datadir + 'cl2017_valueadded_20170426.txt'

insp_fil =  datadir + 'cl2017_valueadded_20170426.txt'

# Read in CLAMATO catalog
# cat_fil = '/Users/kheegan/lya/3d_recon/ts/pilot/' + $
#           'cosmos_ts_pilot_mastercat.fits'
# cat = mrdfits(cat_fil, 1, /silent)

# readcol, insp_fil, specfil, catnum, mag, zconf, zsp, ra, dec, $
#          snrlya1, snrlya2, f='a, l, f, f, f,f ,f , f,f', /silent

# qualcut = where((snrlya1 GE 1.2 OR snrlya2 GE 1.2) AND zconf GE 3., $
#                 nsel, complement=failcut) 

# remove, failcut, specfil, catnum, zsp, zconf, snrlya1,snrlya2, ra, dec, mag
