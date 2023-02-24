# Knobelwürfel

![](/blog/images/)

```scad
cube([3,1,1]);
translate([1,1,0])
    cube(1,1,1);
translate([0,4,0])
    cube([2,1,1]);
translate([0,5,0])
    cube([1,1,1]);
translate([0,10,0])
    cube([3,1,1]);
translate([0,11,0])
    cube([1,1,1]);
translate([5,1,0])
    cube([2,1,1]);
translate([5,0,0])
    cube([1,1,1]);
translate([5,0,1])
    cube([1,1,1]);
translate([10,0,0])
    cube([2,1,1]);
translate([11,1,0])
    cube([1,1,1]);
translate([11,0,1])
    cube([1,1,1]);
translate([5,6,0])
    cube([2,1,1]);
translate([5,5,0])
    cube([1,1,1]);
translate([5,6,1])
    cube([1,1,1]);
translate([5,10,0])
    cube([2,1,1]);
translate([6,11,0])
    cube([2,1,1]);