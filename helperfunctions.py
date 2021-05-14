import math
def dbm2watt(dbm):
    '''
    Converts input power in dBm to Watts.
    Input: dbm
    Output: Watts

    dbm = 10*log10(Power/1milliWatt)
    dbm/10 = log10(Power/1milliWatt)
    10**(dbm/10) = Power/1milliWatt
    1milliWatt = 0.001 Watt
    Power = 0.001 * 10**(dbm/10)
    '''

    Power = 0.001 * 10**(dbm/10)
    return Power

def dbm2vrms(dbm, r=50):
    '''
    Converts input power in dBm to Volt RMS.
    Input: dbm
    Output: Volt RMS across a load r, 50 Ohm default

    Power = dbm2watt(dbm)
    Power = V**2/r
    r*Power = v**2
    volt = math.sqrt(r*Power)
    '''
    Power = dbm2watt(dbm)
    volt = math.sqrt(r*Power)
    return volt

def dbm2vpp(dbm, r=50):
    '''
    Converts input power in dBm to Volt pp
    Input: dbm
    Output: Volt pp across a load r, 50 Ohm default

    vp = dbm2vp(dbm)
    vpp = 2 * vp
    '''
    vp = dbm2vp(dbm, r)
    vpp = 2 * vp
    return vpp

def dbm2vp(dbm, r=50):
    '''
    Converts input power in dBm to Volt peak.
    Input: dbm
    Output: Volt peak across a load r, 50 Ohm default

    vrms = dbm2vrms(dbm)
    vrm = vp/math.sqrt(2)
    vp = math.sqrt(2) * vrms
    '''
    vrms = dbm2vrms(dbm, r)
    vp = vrms * math.sqrt(2)
    return vp
    
if __name__ == "__main__":
    dbms = [30, 27, 20,18, 10, 0, -10, -20, -30, -40, -50, -60, -80, -90, -100, -110, -118, 3, -3]
    for dbm in dbms:
        power = dbm2watt(dbm)
        print(f'{dbm} dBm -> power = {power}')
