import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import ShuffleSplit, cross_val_score

import mne
from mne import Epochs, pick_types, find_events, pick_types, set_eeg_reference
from mne.channels import read_layout
from mne.io import concatenate_raws, read_raw_edf
from mne.datasets import eegbci
from mne.decoding import CSP
from mne import viz


def main():
    raw = mne.io.read_raw_gdf('.gdf', stim_channel=-1, preload=True)
    raw2= mne.io.read_raw_gdf('.gdf', stim_channel=-1, preload=True)
    # events = mne.read_events('BCICIV_2a_gdf/A01E.gdf')
    print(raw.ch_names)
    print(raw.info)
    # raw.set_eeg_reference('average', projection=True)
    # sfreq = raw.info['sfreq']
    # data, times = raw[:5, int(sfreq * 1):int(sfreq * 3)]
    # _ = plt.plot(times, data.T)
    # _ = plt.title('Sample channels')
    # plt.show()
    # picks = mne.pick_types(raw.info, meg=True, eeg=False, stim=True, eog=True,
    #                    exclude='bads')
    # event_id, tmin, tmax = 1, -0.2, 0.5
    # # myPath= r'C:\Users\krad1\Documents\BCI4'
    # epochs = Epochs(raw, events, event_id, tmin, tmax, proj=True, picks=picks,
    #                 baseline=None, preload=True, reject=dict(grad=4000e-13, mag=4e-12, eog=150e-6))
    # evoked = epochs.average()
    # evoked.plot()
    # plt.show()


if __name__ == '__main__':
    main()
