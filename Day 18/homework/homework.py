#```1. შექმენი პროგრამა, სადაც მომხმარებელს შემოატანინებ თავის, შემდეგ კი მეგობრის  ასაკს, თუ მეგობრის ასაკი მეტია მის ასაკზე, დაუპრინტე რომ პატარაა, თუ მისი ასაკი მეტია მეგობრის ასაკზე, დაუპრინტე რომ დიდია.

#2. შექმენი პროგრამა, სადაც მომხმარებელს შემოატანინებ მის დაბადების წელს, თუ ის იქნება 2010 წელზე მეტი, დაუპრინტე, რომ gen alpha თაობის წარმომადგენელია, სხვა შემთხვევაში არაფერი არ დაუპრინტო.

#3. შექმენი პროგრამა, სადაც მომხმარებელს შემოატანინებ მის ასაკს, თუ მისი ასაკი მეტია 10-ზე, დაუპრინტე რამდენი წლის იქნება 15 წლის შემდეგ, თუ მისი ასაკი ნაკლებია 10-ზე დაუპრინტე რამდენი წლის იყო 5 წლის წინ.

#4. შექმენი პროგრამა, სადაც მომხმარებელს შეეკითხები რამდენი წლით უნდა დროში წინ მოგზაურობა, შემდეგ შემოატანინე მისი დაბადების თარიღი, და დაუპრინტე რამდენი რომელი წელი იქნება, როდესაც მომავალში მისი სასურველი წლით გადავა.

#5. კომენტარების მეშვეობით ახსენი, რა არის for loop, რა არის while loop, რა განსხვავებაა მათ შორის და რა დროს რომლის გამოყენება სჯობს.```


import math
import turtle
 
def square(t, len):
    """Draws a sqare with sides of given length.
 
    Returns the Turtle to the starting position and location.
    """
     
    for i in range(4):
        t.fd(len)
        t.lt(90)
 
def polyline(t, n, len, angle):
    """Draws n line sgments.
 
    t: Turtle object
    n: number of line segments
    len: length of each segment
    angle: degrees betwen segments
    """
    for i in range(n):
        t.fd(len)
        t.lt(angle)
 
def polygon(t, n, len):
    """Drwaws a polygon with sides.
 
    t: Turtle object
    n: number of sides
    len: length of each side
    """    
    angle = 360.0 / n
    polyline(t, n, len, angle)
 
def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
 
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_len = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_len / 3) + 1
    step_len = arc_len / n
    step_angle = float(angle) / n
 
    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
 
    t.lt(step_angle / 2)
    polyline(t, n, step_len, step_angle)
    t.rt(step_angle / 2)
 
def circle(t, r):
    """Draws a circle with the given radius.
 
    t: Turtle object
    t: radius
    """
    arc(t, r, 360)
 
# the following condition checks whther we are
# running as a script, in which cas run the test code
# or being imported, in which cas dont't.
 
if __name__ == '__main__':
    bob = turtle.Turtle()
 
    # draw a circle centered on the origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)
 
    # wait for the user to close the window
    turtle.mainloop()
    