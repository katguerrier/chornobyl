from math import e, log
class Isotope:
    ''' Creates a new Isotope object given a name, a quantity (activity) in petabecquerels, and a half-life in days. '''
    
    def __init__(self, name, activity, half_life):
        self.name = name
        self.activity = activity * (10 ** 15)
        self.half_life = half_life

    def decay(self, time=None):
        ''' Prints the amount remaining after a given number of days. '''
        if (time == None): time = self.half_life
        
        # The lambda constant is the reciprocal of the tau constant, where tau is the mean lifetime of a given nucleus of a substance, varying with the half-life.
        decay_lambda = log(2,e) / self.half_life

        # N, activity of a substance at a given time, is equal to the initial activity N0 × e raised to the power of (-λt), where t is that given time.
        exponent = (decay_lambda * time) * -1
        remaining_amount = self.activity * pow(e, exponent)

        print(f'After {time} days, there are {round(remaining_amount * (10**-15), 2)} petabecquerels remaining of me. Oh no! I mean, yay!')

    def introduce(self):
        print(f'Hello! I am an isotope named {self.name}. In 1986, {round(self.activity * (10 ** -15), 2)} petabecquerels of me were released into the environment. I have a half-life of {round(self.half_life)} days. Nice to meet you!')

# These are the various radioisotopes released on April 26, 1986 in the Chornobyl disaster, and the quantity released.
krypton_85 = Isotope("Krypton-85", 33, (10.72 * 365.25))
xenon_133 = Isotope("Xenon-133", 6500, 5.25)
tellurium_129 = Isotope("Tellurium-129m", 240, 33.6)
tellurium_132 = Isotope("Tellurium-132", 1150, 3.26)
iodine_131 = Isotope("Iodine-131", 1760, 8.04)
iodine_133 = Isotope("Iodine-133", 910, (20.8 / 24))
cesium_134 = Isotope("Cesium-134", 47, (2.06 * 365))
cesium_136 = Isotope("Cesium-136", 36, 13.1)
cesium_137 = Isotope("Cesium-137", 85, (30.0 * 365))
strontium_89 = Isotope("Strontium-89", 115, 50.5)
strontium_90 = Isotope("Strontium-90", 10, (29.12 * 365))
ruthenium_103 = Isotope("Ruthenium-103", 168, 39.3)
ruthenium_106 = Isotope("Ruthenium-106", 73, 368)
barium_140 = Isotope("Barium-140", 240, 12.7)
zirconium_95 = Isotope("Zirconium-95", 84, 64)
molybdenum_99 = Isotope("Molybdenum-99", 72, 2.75)
cerium_141 = Isotope("Cerium-141", 84, 32.5)
cerium_144 = Isotope("Cerium-144", 50, 284)
neptunium_239 = Isotope("Neptunium-239", 400, 2.35)
plutonium_238 = Isotope("Plutonium-239", 0.015, 87.74 * 365)
plutonium_239 = Isotope("Plutonium-239", 0.013, 24065*365)
plutonium_240 = Isotope("Plutonium-240", 0.018, 6537*365)
plutonium_241 = Isotope("Plutonium-241", 2.6, 14.4*365)
plutonium_242 = Isotope("Plutonium-242", 0.00004, 376000*365)
curium_242 = Isotope("Curium-242", 0.4, 18.1*365)

isotopes = [krypton_85, xenon_133, tellurium_129, tellurium_132, iodine_131, iodine_133, cesium_134, cesium_136, cesium_137, strontium_89, strontium_90, ruthenium_103, ruthenium_106, barium_140, zirconium_95, molybdenum_99, cerium_141, cerium_144, neptunium_239, plutonium_238, plutonium_239, plutonium_240, plutonium_241, plutonium_242, curium_242]

# Taking a look at each isotope's remaining activity now.
for i in isotopes:
    if (i.half_life > 365): # The isotopes with short half-lives (under 1 year) are now completely negligible in quantity.
        i.introduce()
        i.decay(13128) # days since April 26, 1986 at time of writing