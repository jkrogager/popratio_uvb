# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from glob import glob

HM2012 = np.loadtxt('/Users/krogager/coding/popratio_uvb/UVB_HM2012.txt')

z_HM12 = HM2012[0, 1:]
data = HM2012[1:, :]
wl_HM12 = data[:,0]
spec_HM12 = data[:, 1:].T

# -- plot spectra for different redshifts:
z_to_plot = [0., 3.]
colors = ['k-', 'b--']

path = '/Users/krogager/Downloads/KS_2018_EBL/Fiducial_Q18/'
all_files = np.sort(glob(path+'*.txt'))
all_z = [fname.split('_')[-1].strip('.txt').strip() for fname in all_files]

plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(111)
for z, col in zip(z_to_plot, colors):
    idx = np.argmin(np.abs(z_HM12 - z))
    ax.loglog(wl_HM12, spec_HM12[idx], col, label='Haardt & Madau (2012), z=%.1f'%z)
    nu_HM12 = 2.99e18 / wl_HM12
    Jnu_HM12 = spec_HM12[idx]
    UV = (wl_HM12 > 911.76) & (wl_HM12 < 2066.67)
    Iuv_HM12 = np.abs(np.trapz(Jnu_HM12[UV], nu_HM12[UV])) * 4*np.pi

    # -- load Khaire & Srianand 2019 for comparison
    fid = all_z.index('%.1f'%z)
    fname = all_files[fid]
    KS19 = np.loadtxt(fname)
    wl_KS19 = KS19[:, 0]
    Jnu = KS19[:, 1]
    ax.loglog(wl_KS19, Jnu, col[0]+':', label='Khaire & Srianand (2019), z=%.1f'%z)
    nu = 2.99e18 / wl_KS19
    UV = (wl_KS19 > 911.76) & (wl_KS19 < 2066.67)
    Iuv = np.abs(np.trapz(Jnu[UV], nu[UV])) * 4*np.pi

ax.set_xlabel(u"Wavelength  [Å]", fontsize=14)
ax.set_ylabel(r"$J_{\nu}$  [erg s$^{-1}$ cm$^{-2}$ Sr$^{-1}$ Hz$^{-1}$]", fontsize=14)
ax.set_xlim(xmin=1.e-7)
ax.set_ylim(ymin=1.e-35)
ax.legend()
fig.tight_layout()
plt.savefig("UVB_comparison.pdf")

