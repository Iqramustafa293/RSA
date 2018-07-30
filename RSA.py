import hashlib
from fpylll import *
from hashlib import md5
import numpy as np
from numpy.linalg import linalg
from numpy.linalg import inv
import math
import time
#import matplotlib.pyplot as plt
#from livelossplot import PlotLosses

def matrix_reduction(matrix):    
    LLL.reduction(matrix)
    return SVP.shortest_vector(matrix)

def compute_vector1(shortestvector):
    return GaussSieve(shortestvector, algorithm=2)()

def gauss_sieve(vector1, y):
    
    [l,m,n] = np.cross(vector1, y)
    return [l,m,n]

def compute_magnitude(c0, vector1, y, magnitude):    
    magnitude1 = round(math.sqrt(sum(v**2 for v in vector1)))
    vector2 = (y)
    magnitude2 = round(math.sqrt(sum(v**2 for v in vector2)))
    sin_theta = magnitude/(magnitude1*magnitude2)
    return round(np.degrees(np.arcsin(sin_theta)))

def compute_theta(c0):
    [l, m, n] = c0
    y_x = m/l
    theta=round(np.degrees(np.arctan(y_x)))
    return int(theta)

def compute_phi(c0, magnitude):
    [l, m, n] = c0
    z_r = n/magnitude
    phi = round(np.degrees(np.arccos(z_r)))
    return int(phi)

def caculate_matrix2(theta, phi, totient):
    x_ct= np.cos(np.radians(theta))
    x_st= np.sin(np.radians(theta))
    y_cp= np.cos(np.radians(phi))
    y_sp= np.sin(np.radians(phi))
    x1 = int (round(totient * x_ct * y_sp))
    y2 = int(round(totient * x_st* y_sp))
    z2 = int(round(totient* y_cp))
    return [x1, y2, z2]    

def calculate_matrix3(matrix2, c0):
    [l, m, n] = c0
    return IntegerMatrix.from_matrix([[l.item(),m.item(),n.item()],matrix2])

def private_key(vector1,c0,result3):
    d=np.array((vector1,c0,result3))
    return d.transpose()

def public_key(d1, k): 
   
   kd= k*d1
   return inv(np.matrix(kd))
 
def encryption(pub_key):
    m = np.array([[1,2,3],[4,5,6],[7,8,9]])
    return np.dot(m, pub_key)

def decryption(d1, k, encrypted_msg):
    decrypted_msg = (encrypted_msg*k)
    return np.dot(decrypted_msg,d1)

y = [11,23,5]
matrix = IntegerMatrix.from_matrix([[1,-3,7],[11,23,5],[19,13,2]])
shortestvector = matrix_reduction(matrix)
vector1 = compute_vector1(matrix)
c0 = gauss_sieve(vector1, y)
magnitude = round(math.sqrt(sum(v**2 for v in c0)))
angle = compute_magnitude(c0, vector1, y, magnitude)
totient = magnitude-1
theta=  compute_theta(c0)
phi = compute_phi(c0, magnitude)
matrix2 = caculate_matrix2(theta, phi, totient)   
matrix3 = calculate_matrix3(matrix2, c0)
shortestvector = matrix_reduction(matrix3)
result3 = compute_vector1(matrix3)    
d1= private_key(vector1,c0,result3)
k = 2
pub_key = public_key(d1, k)
encrypted_msg = encryption(pub_key)
print ("encrypted_msg =" , encrypted_msg)
decrypted_ms = decryption(d1, k, encrypted_msg)
print ("decrypted_msg =" , decrypted_ms)