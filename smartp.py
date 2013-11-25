import sys
import xml.etree.ElementTree as ET

def update_property(dstfile, key, value):
	print "modify " + dstfile + " update " + " key " + " with value '" + value + "'"

def delete_property(dstfile, key, value):
	print "modify " + dstfile + " delete " + " key " + " with value '" + value + "'"

def add_property(dstfile, key, value):
	print "modify " + dstfile + " add " + " key " + " with value '" + value + "'"

def apply_properties(srcfile, dstfile):
	tree = ET.parse(srcfile)
	root = tree.getroot()
	for property in root:
		if property.find("action").text == "update":
			update_property(dstfile, property.find("key").text, property.find("value").text)
		if property.find("action").text == "add":
			add_property(dstfile, property.find("key").text, property.find("value").text)
		if property.find("action").text == "delete":
			delete_property(dstfile, property.find("key").text, property.find("value").text)

def main(patchfile, dstpropertiesfile):
	try:
		with open(patchfile) as srcfile:
			try:
				with open(dstpropertiesfile) as dstfile:
					apply_properties(patchfile, dstpropertiesfile)
			except IOError:
				print "destination file does not exists"
				exit(-1)
	except IOError:
		print "destination file does not exists"
		exit(-1)


if __name__ == "__main__":

	if len(sys.argv) != 3:
		print "Error: usage smartp src.patch.xml dst.properties"
		exit(-1)

	main(sys.argv[1], sys.argv[2])