import sys
import math

# display usage if arguments are missing
if len(sys.argv) < 3:
	print 'usage: 3dna.py <input file> <resolution>'

	sys.exit(0)

# open specified genome file
filename=sys.argv[1]

# if specified, only process a subset of the file (default to 100)
chromosome_sample_count = 0
chromosome_sample_limit = 100
if len(sys.argv) > 2:
	chromosome_sample_limit = int(sys.argv[2])

# globals
current_chromosome = ""
current_chromosome_lines = 0
chromosomes = {}
points = []
vectors = []
radius = 200

# open file for analysis
gfile = open(filename)

for line in gfile:

	# ignore comments
	if line[0] != '#':

		# split line
		row = line.split('\t')

		# count chromosomes
		if row[1] != current_chromosome:

			# if this is the end of the interesting chromosomes, exit analysis
			if not row[1].isdigit():
				
				chromosomes[current_chromosome] = current_chromosome_lines
				break

			# skip output if this is the first chromosome
			if current_chromosome != "":
				chromosomes[current_chromosome] = current_chromosome_lines

			current_chromosome_lines = 0
			current_chromosome = row[1]

		# count lines
		if current_chromosome_lines > chromosome_sample_limit:
			current_chromosome_lines = current_chromosome_lines + 1
		else:
			current_chromosome_lines = chromosome_sample_limit


# close & reopen file for actual processing
gfile.close()
gfile = open(filename)

current_chromosome = ""
angle = 0

for line in gfile:

	# ignore comments
	if line[0] != '#':

		# split line
		row = line.split('\t')
		
		# increment chromosome
		if row[1] != current_chromosome:

			# output last chromosome
			if current_chromosome != "":
				print "hull(){"
				print "cylinder(r=50,h=10);"
				print "translate(v=[0,0,%d]){" % (int(current_chromosome) * 5)
				print "linear_extrude(height=%d,center=true,convexity=10){" % (int(current_chromosome) * 5)
				print "polygon(points=%s,paths=[%s]);" % (points, vectors)
				print "}}}"

			# reset the sample count
			chromosome_sample_count = 0

			# if the next row isn't a chromosome we handle, eject
			if not row[1].isdigit():

				break

			else:

				# create a new layer
				current_chromosome = row[1]
				points = []
				vector = 0
				vectors = []

				# get angle inc. from chromosome dictionary
				angle_inc = (3.14 * 2) / chromosomes[current_chromosome] 

		# if we've hit the sample limit, move along
		if chromosome_sample_count < chromosome_sample_limit:

			# turn marker into integer
			point_val = int(ord(row[3][0])) + int(ord(row[3][1]))

			# convert to x,y
			point_val_x = round((radius - point_val) * math.cos(angle),1)
			point_val_y = round((radius - point_val) * math.sin(angle),1)
			point = [point_val_x,point_val_y]

			points.append(point)
			vectors.append(vector)

			# increment angle
			angle = angle + angle_inc

			# increment vector
			vector = vector + 1

			# increment sample count
			chromosome_sample_count = chromosome_sample_count + 1
