import capsule_vacuum_vessel
import pytest
import math
import paramak

'''This test evaluates the perimeter of the resultant points and asserts them agaist the known value'''

def perimeter(outer_start_point,radius,thickness):

    test_shape = paramak.CapsuleVacuumVessel(
        outer_start_point = outer_start_point,
        radius = radius,
        thickness = thickness
    )
    point1 = test_shape.points[0]
    point2 = test_shape.points[1]
    point3 = test_shape.points[2]
    point4 = test_shape.points[3]
    point5 = test_shape.points[4]
    point6 = test_shape.points[5]
    point7 = test_shape.points[6]
    point8 = test_shape.points[7]
    point9 = test_shape.points[8]
    point10 = test_shape.points[9]
    point11 = test_shape.points[10]
    point12 = test_shape.points[11]
    
    straightedges = float((point12[1]-point1[1]) + (point6[1]-point7[1]) + (point4[1]-point3[1]) + (point9[1]-point10[1]))
    curvededges = float((math.pi*radius) + (math.pi*(radius-thickness)))
    total = float(straightedges + curvededges)

    return total

def test_perimeter1():
    testp = round(perimeter(
        outer_start_point=(0,0),
        radius = 300,
        thickness = 10),2)
    assert testp == 3073.54

def test_perimeter2():
    testp = round(perimeter(
        outer_start_point=(100,-100),
        radius=400,
        thickness = 25)
        ,2)
    assert testp == 4084.73

def test_perimeter3():
    testp = round(perimeter(
        outer_start_point=(1000,-500),
        radius=5000,
        thickness = 50),
        2)
    assert testp == 51358.85

'''this tests if the number of points returned are correct'''
def test_pointnum1():
     shape = paramak.CapsuleVacuumVessel(
          outer_start_point=(0,0),
          radius= 300,
          thickness = 10)
     pointnum = len(shape.points)
     
     assert pointnum == 13

def test_pointnum2():
     shape = paramak.CapsuleVacuumVessel(
          outer_start_point=(100,-100),
          radius=400,
          thickness = 25)
     pointnum = len(shape.points)
     assert pointnum == 13

def test_pointnum3():
     shape = paramak.CapsuleVacuumVessel(
     outer_start_point=(1000,-500),
     radius=5000,
     thickness = 50)
     pointnum = len(shape.points)
     assert pointnum == 13

'''this tests the volume of the created component and asserts it agaist the known value'''
def volume(outer_start_point,radius,thickness,angle):

    test_shape = paramak.CapsuleVacuumVessel(
        outer_start_point = outer_start_point,
        radius = radius,
        thickness = thickness,
        rotation_angle = angle
    )
    
    point3 = test_shape.points[2]
    point4 = test_shape.points[3]
    
    point9 = test_shape.points[8]
    point10 = test_shape.points[9]
    

    outer_volume_cylinder = float(math.pi * (radius**2) * (point4[1]-point3[1]))
    inner_volume_cylinder = float(math.pi * ((radius-thickness)**2) * (point9[1]-point10[1]))
    outer_volume_sphere = float((4/3)*math.pi*(radius**3))
    inner_volume_sphere = float((4/3)*math.pi*((radius-thickness)**3))
    outer_volume = outer_volume_sphere + outer_volume_cylinder
    inner_volume = inner_volume_cylinder + inner_volume_sphere
    total_volume = (angle/360) * (outer_volume-inner_volume)
    
    return total_volume

volume((0,0),300,10,180)

def testvolume1():
    testvol = round(volume(
        outer_start_point = (0,0),
        radius = 300,
        thickness = 10,
        angle= 180),
        2)
    assert testvol == 11029084.61

def testvolume2():
    testvol = round(volume(
        outer_start_point = (100,-100),
        radius = 400,
        thickness = 25,
        angle= 360),
        2)
    assert testvol == 95884025.78

def testvolume3():
    testvol = round(volume(
        outer_start_point=(1000,-500),
        radius=5000,
        thickness = 50,
        angle = 90),
        2)
    assert testvol == 7795207671.41