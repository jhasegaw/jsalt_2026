import numpy as np

def voiced_excitation(duration, F0, Fs):
    '''
    Create voiced speeech excitation.
    
    @param:
    duration (scalar) - length of the excitation, in samples
    F0 (scalar) - pitch frequency, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    excitation (np.ndarray) - the excitation signal, such that
      excitation[n] = -1 if n is an integer multiple of int(np.round(Fs/F0))
      excitation[n] = 0 otherwise
    '''
    raise RuntimeError("You need to write this part!")

def resonator(x, F, BW, Fs):
    '''
    Generate the output of a resonator.
    
    @param:
    x (np.ndarray(N)) - the excitation signal
    F (scalar) - resonant frequency, in Hertz
    BW (scalar) - resonant bandwidth, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    y (np.ndarray(N)) - resonant output
    '''
    raise RuntimeError("You need to write this part!")

def synthesize_vowel(duration,F0,F1,F2,F3,F4,BW1,BW2,BW3,BW4,Fs):
    '''
    Synthesize a vowel.
    
    @param:
    duration (scalar) - duration in samples
    F0 (scalar) - pitch frequency in Hertz
    F1 (scalar) - first formant frequency in Hertz
    F2 (scalar) - second formant frequency in Hertz
    F3 (scalar) - third formant frequency in Hertz
    F4 (scalar) - fourth formant frequency in Hertz
    BW1 (scalar) - first formant bandwidth in Hertz
    BW2 (scalar) - second formant bandwidth in Hertz
    BW3 (scalar) - third formant bandwidth in Hertz
    BW4 (scalar) - fourth formant bandwidth in Hertz
    Fs (scalar) - sampling frequency in samples/second
    
    @returns:
    speech (np.ndarray(samples)) - synthesized vowel
    '''
    raise RuntimeError("You need to write this part!")

def lpc(speech, frame_length, frame_skip, order):
    '''
    Perform linear predictive analysis of input speech.
    
    @param:
    speech (duration) - input speech waveform
    frame_length (scalar) - frame length, in samples
    frame_skip (scalar) - frame skip, in samples
    order (scalar) - number of LPC coefficients to compute
    
    @returns:
    A (nframes,order+1) - linear predictive coefficients from each frames
    excitation (nframes,frame_length) - linear prediction excitation frames
      (only the last frame_skip samples in each frame need to be valid)
    '''
    raise RuntimeError("You need to write this part!")

def synthesize(e, A, frame_skip):
    '''
    Synthesize speech from LPC residual and coefficients.
    
    @param:
    e (duration) - excitation signal
    A (nframes,order+1) - linear predictive coefficients from each frames
    frame_skip (1) - frame skip, in samples
    
    @returns:
    synthesis (duration) - synthetic speech waveform
    '''
    raise RuntimeError("You need to write this part!")

def robot_voice(excitation, T0, frame_skip):
    '''
    Calculate the gain for each excitation frame, then create the excitation for a robot voice.
    
    @param:
    excitation (nframes,frame_length) - linear prediction excitation frames
    T0 (scalar) - pitch period, in samples
    frame_skip (scalar) - frame skip, in samples
    
    @returns:
    gain (nframes) - gain for each frame
    e_robot (nframes*frame_skip) - excitation for the robot voice
    '''
    raise RuntimeError("You need to write this part!")

