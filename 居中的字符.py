#!/usr/bin/python
text=input("word:")

screen_width=100
text_width=len(text)
box_width=text_width+6
left_margin=(screen_width-box_width)//2
print(" ")
print (' '*left_margin+'+'+'-'*(box_width-4)+'+')
print (' '*left_margin+'|'+ ' '*(text_width+1) +' |')
print (' '*left_margin+'|'+ ' ' +  text    +' |')
print (' '*left_margin+'|'+ ' '*(text_width+1)+' |')
print (' '*left_margin+'+'+'-'*(box_width-4)+'+')
print ("\n")
input("Press <enter>")












