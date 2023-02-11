import math

#K=77164
#N=2**32
K=1.1775*2**64
N=2**128
exponent = (-K * (K - 1) / (2 * N))

unique_probability = math.exp(exponent)
collision_probability = 1 - unique_probability
print ("Prawdopodobieństwo urodzinowe K:",K,"z N:",N," wynosi:", collision_probability)
