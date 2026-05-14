"""Utilities for loading EEG data."""

from __future__ import annotations

import numpy as np
import os

def load_raw(path: str):
    """
    Load raw THINGS-EEG2 dataset from a .npy file and extract EEG + stimulus events.

    Parameters
    path : str
        Path to .npy file containing a dictionary with keys:

    Returns
    dict
        Dictionary containing:
        - eeg : np.ndarray
            EEG signals (63 channels, time samples)
        - stim : np.ndarray
            Stimulus channel (event markers over time)
        - event_idx : np.ndarray
            Sample indices where events occur (stim != 0)
        - event_values : np.ndarray
            Event IDs corresponding to each event_idx
        - ch_names : list
            Channel names (including 'stim' last)
        - ch_types : list
            Channel types (EEG or stim)

    Raises
    FileNotFoundError
        If the provided path does not exist.
    KeyError
        If expected keys are missing in the dataset.
    ValueError
        If data shape is invalid (not 64 channels).
    """

    if not path or not isinstance(path, str):
        raise ValueError("Path must be a non-empty string")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    d = np.load(path, allow_pickle=True).item()
    raw = d["raw_eeg_data"]

    if raw.shape[0] != 64:
        raise ValueError("Channel size is not 64")

    eeg = raw[:-1]
    stim = raw[-1]

    event_idx = np.where(stim != 0)[0]
    event_values = stim[event_idx].astype(int)

    return {
        "eeg":eeg,
        "stim":stim,
        "event_idx":event_idx,
        "event_values":event_values,
        "ch_names":d["ch_names"],
        "ch_types":d["ch_types"],
    }