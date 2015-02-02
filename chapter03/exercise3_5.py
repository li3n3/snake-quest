'''
prints a two-by-two grid, with + at the intersections, and | for the edges
then prints a four-by-four grid
'''

def plus_line():               # this one does + - - - - + - - - - +
	print '+',
	print '-', '-', '-', '-',
	print '+',
	print '-', '-', '-', '-',
	print '+'

def line_line():               # this one does | - - - - | - - - - |
	print '|',
	print ' ', ' ', ' ', ' ',
	print '|',
	print ' ', ' ', ' ', ' ',
	print '|'

def four_times(f):             # can I not multiply functions, then?
	f()
	f()
	f()
	f()

def draw_box():
	plus_line()
	four_times(line_line)
	plus_line()
	four_times(line_line)
	plus_line()

draw_box()

print

# it ain't pretty, but it sure does get the job done:
def four_by_four():
	four_times(plus_column)
	print '+'

	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'

	four_times(plus_column)
	print '+'

	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'

	four_times(plus_column)
	print '+'

	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'

	four_times(plus_column)
	print '+'

	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'
	four_times(line_column)
	print '|'

	four_times(plus_column)
	print '+'

def plus_column():
	print '+',
	print '-', '-', '-', '-',

def line_column():
    print '|',
    print ' ', ' ', ' ', ' ',

four_by_four()