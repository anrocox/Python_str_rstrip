#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2014

@author: anroco

In python how to remove one or more trailing characters of a string?

En python ¿como remover uno o varios caracteres del final de un string?
'''

#create a str
s = '-+-+I thought a thought+-+-'
print(s)

#generates a copy of the string with the trailing characters removed.
s_new = s.rstrip('+-')
print(s_new)

#create a str
s = '\tI thought a thought\t'
print(s)

#if the character is not defined, by defaults to removing whitespace.
#Whitespace characters are those defined in the system Unicode as
#'Other' or 'Separator'.
s_new = s.rstrip()
print(s_new)
