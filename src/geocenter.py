import numpy as np
from scipy.optimize import minimize
from geopy.distance import geodesic

def geodesic_distance_sum(point, coords):
    """ Calculate the sum of geodesic distances from the point to all coordinates """
    lat, lon = point
    return sum(geodesic((lat, lon), coord).meters for coord in coords)

def geographic_median(coords):
    """
    Find the geographic median (point equidistant to all given coordinates)
    using geodesic distance.
    """
    # Start with the arithmetic mean as an initial guess
    initial_guess = np.mean(coords, axis=0)
    
    # Minimize the sum of geodesic distances to all points
    result = minimize(geodesic_distance_sum, initial_guess, args=(coords,), method='Nelder-Mead')
    
    return result.x  # Return the optimized latitude and longitude
