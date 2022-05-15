# Story Generation in Python
import random #importing random
when = ['A few years ago','Yesterday','Last night','A long time ago','On 20th Jan']
who = ['a rabbit','an elephant','a mouse','a turtle','a cat']
name = ['name Ali','name Miriam','name daniel','name Sara','name Mike']
residence = ['in Barcelona','in Lonawala','in Gopeshwar','in Nanital','in India']
went = ['went a cinema','went a university','went a seminar','went a school','went a laundry']
happend = ['made a lot of friends','Eats a burger','found a secret key','solved a mistery','wrote a book']
print(random.choice(when)+','+random.choice(who)+','+random.choice(name)+','+random.choice(residence)+','+random.choice(went)+','+random.choice(happend)+'.')