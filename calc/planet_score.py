from calc.ESI import calc_esi

# calculates a score for a planet based on it's characteristics
# score is based on planet habitability and distance
def planet_score(dist, rad, mass, temp):
  # ESI is a measure related to habitability
  ESI = calc_esi(rad, mass, temp)
  
  # closer is better
  dist = max(100 - dist, 0)
  return dist * ESI