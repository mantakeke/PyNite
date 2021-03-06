# Example of a simply supported beam with a point load.
# Units used in this example are inches, and kips

# Import `FEModel3D` from `PyNite`
from PyNite import FEModel3D

# Create a new finite element model
SimpleBeam = FEModel3D()

# Add nodes (14 ft apart)
SimpleBeam.AddNode('N1', 0, 0, 0)
SimpleBeam.AddNode('N2', 14*12, 0, 0)

# Add a beam with the following properties:
# E = 29000 ksi, G = 11400 ksi, Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
SimpleBeam.AddMember('M1', 'N1', 'N2', 29000, 11400, 100, 150, 250, 20)

# Provide simple supports
SimpleBeam.DefineSupport('N1', True, True, True, True, False, False)  # Constrained for torsion at 'N1'
SimpleBeam.DefineSupport('N2', True, True, True, False, False, False) # Not constrained for torsion at 'N2'

# Add a downward point load of 5 kips at the midspan of the beam
SimpleBeam.AddMemberPtLoad('M1', 'Fy', -5, 7*12)

# Analyze the beam and perform a statics check
SimpleBeam.Analyze(check_statics=True)

# Print the shear, moment, and deflection diagrams
SimpleBeam.GetMember('M1').PlotShear('Fy')
SimpleBeam.GetMember('M1').PlotMoment('Mz')
SimpleBeam.GetMember('M1').PlotDeflection('dy')

# Print reactions at each end of the beam
print('Left Support Reaction:', SimpleBeam.GetNode('N1').RxnFY, 'kip')
print('Right Support Reacton:', SimpleBeam.GetNode('N2').RxnFY, 'kip')

# Print the max/min shears and moments in the beam
print('Maximum Shear:', SimpleBeam.GetMember('M1').MaxShear('Fy'), 'kip')
print('Minimum Shear:', SimpleBeam.GetMember('M1').MinShear('Fy'), 'kip')
print('Maximum Moment:', SimpleBeam.GetMember('M1').MaxMoment('Mz')/12, 'kip-ft')
print('Minimum Moment:', SimpleBeam.GetMember('M1').MinMoment('Mz')/12, 'kip-ft')

# Print the max/min deflections in the beam
print('Maximum Deflection:', SimpleBeam.GetMember('M1').MaxDeflection('dy'), 'in')
print('Minimum Deflection:', SimpleBeam.GetMember('M1').MinDeflection('dy'), 'in')