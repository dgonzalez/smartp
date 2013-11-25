import sys
import xml.etree.ElementTree as ET

""" 
	TODO: Check for property not found on update and delete
		  Check for duplicated properties
"""

def update_property(dstfile, key, value):
	data = ""
	print "modify " + dstfile + " update " + " key " + " with value '" + value + "'"

	with open(dstfile, "r+") as dstdescriptor:
		for line in dstdescriptor:
			if line.strip().startswith(key):
				data = data + key + "=" + value
			else:
				data = data + line
		dstdescriptor.seek(0)
		dstdescriptor.write(data)
		dstdescriptor.truncate()

def delete_property(dstfile, key, value):
	data = ""
	print "modify " + dstfile + " delete " + " key " + " with value '" + value + "'"

	with open(dstfile, "r+") as dstdescriptor:
		for line in dstdescriptor:
			if line.strip().startswith(key):
				pass
			else:
				data = data + line

		dstdescriptor.seek(0)
		dstdescriptor.write(data)
		dstdescriptor.truncate()

def add_property(dstfile, key, value):
	data = ""
	print "modify " + dstfile + " add " + " key " + " with value '" + value + "'"

	with open(dstfile, "r+") as dstdescriptor:
		allfile = dstdescriptor.read()
		allfile = allfile + "\n" + key + "=" + value
		print allfile
		data = allfile

		dstdescriptor.seek(0)
		dstdescriptor.write(data)
		dstdescriptor.truncate()

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
		with open(patchfile) as srcfile:
			with open(dstpropertiesfile) as dstfile:
				apply_properties(patchfile, dstpropertiesfile)


if __name__ == "__main__":

	if len(sys.argv) != 3:
		print "Error: usage smartp src.patch.xml dst.properties"
		exit(-1)

	main(sys.argv[1], sys.argv[2])