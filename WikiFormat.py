#!/usr/bin/python -u

"""
Tool to convert unformatted strings to DokuWiki strings.
Allows to convert DokuWiki strings in a certain format to
another DokuWiki format.
"""

import sys

"""
converts multiple whitespaces to a single whitespace
"""
def single_ws():
  s = ''
  for l in sys.stdin:
    s += replace_ws(l)
  # Several newlines result in multiple whitespaces. Remove them!
  s = replace_ws(s)
  return s

"""
turns a glossary with headings into a list
"""
def glossary_to_list():
  s = ''
  for l in sys.stdin:
    l = l.strip()
    l = heading_to_list(l)
    s += l
    if (l != ''):
      s += ' '
  s = s.rstrip()
  return s

"""
turns passages without headings into a list
"""
def passages_to_list():
  s = '  * '
  for l in sys.stdin:
    l = l.strip()
    if (l != ''):
      s += l + ' '
    else:
      s = s.rstrip() + '\n  * '
  s = s.rstrip()
  return s

"""
turns a heading into a list heading
"""
def heading_to_list(l):
  if l.startswith('=') and l.endswith('='):
    return '\n  * **' + l.strip('= ') + '**:'
  else:
    return l

"""
turns lines into a list
"""
def lines_to_list():
  s = ''
  for l in sys.stdin:
    l = l.strip()
    s += '  * ' + l + '\n'
  s = s.rstrip()
  return s

"""
replace multiple whitespaces with a single white space
"""
def replace_ws(s):
  ignore = False
  result = ''

  for c in s:
    if len(c.strip()) == 0:
      if not ignore:
        if (c == '\n'):
          result += '\n'
        else:
          result += ' '
        ignore = True
    else:
      result += c
      ignore = False

  return result

"""
print the given string on stdout
"""
def print_string(s):
  print "\n-------------------------------"
  print s,

"""
parse command-line parameters and go ahead
"""
def main():
  args = sys.argv

  if len(args) != 2:
    print 'Syntax: python -u ' + args[0] + ' s/g/p\n'
    print 's: multiple whitespace to single whitespace'
    print 'g: glossary to list'
    print 'p: passages to list'
    print 'l: lines to list'
    print '\nCtrl-D starts the conversion'
  else:
    s = ''

    if args[1] == 's':
      s = single_ws()
    elif args[1] == 'g':
      s = glossary_to_list()
    elif args[1] == 'p':
      s = passages_to_list()
    elif args[1] == 'l':
      s = lines_to_list()
    else:
      s = 'unknown parameter ' + args[1]

    print_string(s)

if  __name__ =='__main__':
  main()
