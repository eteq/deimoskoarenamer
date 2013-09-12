"""
Renames DEIMOS observation files from the Keck Archive to the names they had
when originally created.

Requires `astropy` (for FITS-reading)
"""

from sys import argv, exit
from os import system
from glob import glob

from astropy.io import fits


def hdrtofn(h):
    return h['OUTFILE'] + '%04i' % h['FRAMENO'] + '.fits.gz'


if len(argv) > 1:
    oldfns = glob(argv[1])
elif len(argv) > 2:
    print 'Usage: deimoskoarenamer.py [inputpattern]'
    exit(1)
else:
    oldfns = glob('DE.*.fits.gz')
    
print 'Found', len(oldfns), 'Files to rename')
    
for i,fn in enumerate(oldfns):
    newfn = hdrtofn(fits.getheader(fn, 0))
    print 'Moving',fn ,'to',newfn,i+1,'of',len(oldfns)
    system(u'mv $fn $newfn')
    
