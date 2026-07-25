# =========================================================================
# DSP MATH: SIGNAL METADATA CHANNEL
# =========================================================================

def process(signal):
    length = len(signal) if signal else 0
    return {
        "type": "dsp",
        "length": length,
        "status": "OK",
    }
