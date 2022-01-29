'''
Michael Balestriere
Week 2 - Eggs
URL - https://www.saudereggs.com/blog/egg-sizing-guide/
'''

while (True):
    weight=float(input("How much does the egg weigh in ounces? between 0.0 and 2.5 ounces."))
    if weight<=1.5:
        print("This is a size small egg!")
    elif weight<=1.75:
        print("This is a size medium egg!")
    elif weight<=2:
        print("This is a size large egg!")
    elif weight<=2.25:
        print("This is a size extra large egg!")
    elif weight<=2.5:
        print("This is a size jumbo egg!")
    else:
        print("enter a valid egg size in ounces")
        
                       
