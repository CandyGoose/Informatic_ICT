# -*- coding: utf-8 -*-
import os
TESTS = [
    '\n',
    'Dmitriy\n',
    'to ITMO University\n',
    'Michael Christopher Jessica Matthew Ashley Jennifer Joshua Amanda Daniel David James Robert John Joseph Andrew Ryan Brandon Jason Justin Sarah William Jonathan Stephanie Brian Nicole Nicholas Anthony Heather Eric Elizabeth Adam Megan Melissa Kevin Steven Thomas Timothy Christina Kyle Rachel Laura Lauren Amber Brittany Danielle Richard Kimberly Jeffrey Amy Crystal Michelle Tiffany Jeremy Benjamin Mark Emily Aaron Charles Rebecca Jacob Stephen Patrick Sean Erin Zachary Jamie Kelly Samantha Nathan Sara Dustin Paul Angela Tyler Scott Katherine Andrea Gregory Erica Mary Travis Lisa Kenneth Bryan Lindsey Kristen Jose Alexander Jesse Katie Lindsay Shannon Vanessa Courtney Christine Alicia Cody Allison Bradley Samuel Shawn April Derek Kathryn Kristin Chad Jenna Tara Maria Krystal Jared Anna Edward Julie Peter Holly Marcus Kristina Natalie Jordan Victoria Jacqueline Corey Keith Monica Juan Donald Cassandra Meghan Joel Shane Phillip Patricia Brett Ronald Catherine George Antonio Cynthia Stacy Kathleen Raymond Carlos Brandi Douglas Nathaniel Ian Craig Brandy Alex Valerie Veronica Cory Whitney Gary Derrick Philip Luis Diana Chelsea Leslie Caitlin Leah Natasha Erika Casey Latoya Erik Dana Victor Brent Dominique Frank Brittney Evan Gabriel Julia Candice Karen Melanie Adrian Stacey Margaret Sheena Wesley Vincent Alexandra Katrina Bethany Nichole Larry Jeffery Curtis Carrie Todd Blake Christian Randy Dennis Alison Trevor Seth Kara Joanna Rachael Luke Felicia Brooke Austin Candace Jasmine Jesus Alan Susan Sandra Tracy Kayla Nancy Tina Krystle Russell Jeremiah Carl Miguel Tony Alexis Gina Jillian Pamela Mitchell Hannah Renee Denise Molly Jerry Misty Mario Johnathan Jaclyn Brenda Terry Lacey Shaun Devin Heidi Troy Lucas Desiree Jorge Andre Morgan Drew Sabrina Miranda Alyssa Alisha Teresa Johnny Meagan Allen Krista Marc Tabitha Lance Ricardo Martin Chase Theresa Melinda Monique Tanya Linda Kristopher Bobby Caleb Ashlee Kelli Henry Garrett Mallory\n']

def run(param):
    stream = os.popen('bash ./labs/1_lab/script.bash ' + param)
    return stream.read()

flag = True
for test in TESTS:
    output = run(test)
    if output.lower() != ('welcome, ' + test).lower():
        flag = False
        continue
        if flag:
            print('PASSED')
        else:
            print('NOT PASSED')
