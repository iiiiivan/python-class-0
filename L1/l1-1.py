from pycat.core import Window

answer=input('What animal you want to see:')
size=input('Which sizedo you want big or small?')

window = Window()
animal= window.create_sprite()

if answer =='elephant':
    animal.image ='elephant.png'
if answer =='pig':
    animal.image ='pig.png'
if answer =='owl':
    animal.image ='owl.png'
if answer =='owl.gif':
    animal.image ='owl.gif'
if answer =='rat':
    animal.image ='rat.png'    
if answer =='rooster':
    animal.image ='rooster.png'
if answer =='tiger':
    animal.image ='tiger.png'
if answer =='wildcat':
    animal.image ='wildcat.png'

if size =='big':
    animal.scale = 2.5
if size =='small':
    animal.scale = 1

animal.x = 650    
animal.y = 300   

window.run()