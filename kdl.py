# Kenan A. Masri 2018 (C)
#
# CODER: KENAN MASRI

# Imports
import sys
import os
import filecmp

version = 1.0

def showHelp():
	print "Kduplister ", version, " - Kenan A. Masri 2018 (C)"
	print "Syntax: kdr.py [-h] dir"
	print ""
	print " <blank>, --help, -h:  Displays this help."
	print " \"directory\": Process the directory files (including subdirs)."
	sys.exit(0)

# Get passed arguments
arglist = sys.argv
directory = os.getcwd()

if (__file__ in arglist):
	arglist.remove(__file__)

if "--help" in arglist or "-h" in arglist:
	if ("-h" in arglist):
		arglist.remove("-h")
	else:
		arglist.remove("--help")
	showHelp()

if os.path.isdir(arglist[0]):
	directory = arglist[0]

def getFilesFromDir(directory):
	file_paths = []
	for root, directories, files in os.walk(unicode(directory, 'utf-8')):
		for filename in files:
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)
	return file_paths

def findDetections(detections, file):
	for d in detections:
		if file in d:
			return detections.index(d)
	return -1

class Kdl():
	""" Class for removing duplicates """

	# Initialization constructor
	def __init__(self, directory):

		self.code = -1
		self.info = True
		self.directory = directory
		self.execute()

	# Execution!
	def execute(self):
		# Find files in directory
		all_files = getFilesFromDir(self.directory)
		compared_files = list(all_files) # New
		detections = []

		# Group Duplicates
		for f in all_files:
			for c in compared_files:
				if f != c:
					if (filecmp.cmp(f, c)):
						if (findDetections(detections, f)==-1 and findDetections(detections, c)==-1):
							detections.append([f,c])
						else:
							i = findDetections(detections, f)
							if findDetections(detections, c)==-1:
								detections[i].append(c)

			compared_files.remove(f)

		i = 0
		print "Results: ", len(detections), " Duplications:\n"
		while i<len(detections):
			print " - ", len(detections[i]), " Files:\n"
			for d in detections[i]:
				print "    - ", d
				i += 1
			print ""

kdl = Kdl(directory)