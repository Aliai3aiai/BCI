import numpy as np
from scipy import signal
from scipy.signal import butter, sosfilt, sosfreqz


def bandpass_filter(signal_in, f_band_nom):
    order = 2
    sos = butter(order, f_band_nom, analog=False, btype='band', output='sos')
    sig_filter = sosfilt(sos, signal_in)

    return sig_filter


def load_bands(bandwidth, f_s, max_freq=40):
    f_bands = np.zeros((99,2)).astype(float)
    band_counter = 0
    for bw in bandwidth:
        start_freq = 8
        while (start_freq + bw <= max_freq):
            f_bands[band_counter] = [start_freq, start_freq + bw]
            if bw == 1:
                start_freq = start_freq + 1
            elif bw == 2:
                start_freq = start_freq + 2
            else:
                start_freq = start_freq + 4
            band_counter += 1
    f_bands_nom = 2*f_bands[:band_counter]/f_s
    return f_bands_nom


def load_filterbank(bandwidth, fs, order=2, max_freq=40, ftype='butter'):
    f_band_nom = load_bands(bandwidth, fs, max_freq)
    n_bands = f_band_nom.shape[0]
    if ftype == 'butter':
        filter_bank = np.zeros((n_bands, order, 6))
    elif ftype == 'fir':
        filter_bank = np.zeros((n_bands, order))

    for band_idx in range(n_bands):
        if ftype == 'butter':
            filter_bank[band_idx] = butter(order, f_band_nom[band_idx], analog=False, btype='band', output='sos')
        elif ftype == 'fir':
            filter_bank[band_idx] = signal.firwin(order, f_band_nom[band_idx], pass_zero='False')
    return filter_bank


def butter_fir_filter(signal_in, filter_coeff):
    if filter_coeff.ndim == 2:  # butter worth
        return sosfilt(filter_coeff, signal_in)
    elif filter_coeff.ndim == 1:  # fir filter

        NO_channels, NO_samples = signal_in.shape
        sig_filt = np.zeros((NO_channels, NO_samples))

        for channel in range(0, NO_channels):
            sig_filt[channel] = signal.convolve(signal_in[channel, :], filter_coeff,
                                                mode='same')  # signal has same size as signal_in (centered)

        return sig_filt


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = butter(order, [low, high], analog=False, btype='band', output='sos')
    return sos


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    sos = butter_bandpass(lowcut, highcut, fs, order=order)
    y = sosfilt(sos, data)
    return y