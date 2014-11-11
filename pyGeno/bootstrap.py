from pyGeno.importation.Genomes import importGenome
from pyGeno.importation.SNPs import importSNPs
import os

this_dir, this_filename = os.path.split(__file__)

def listDataWraps() :
	"""Lists all the datawraps pyGeno comes with"""
	l = []
	for f in os.listdir(os.path.join(this_dir, "bootstrap_data")) :
		if f.find(".tar.gz") > -1 :
			l.append(f)
	return l

def importHumanReferenceYOnly() :
	"Importing only the Y chromosome of the Human Reference Genome. Useful for playing a bit with pyGeno."
	path = os.path.join(this_dir, "bootstrap_data", "GRCh37.75_Y-Only.tar.gz")
	importGenome(path)

def importDummySRY() :
	"A dummy set of SNPs for the Gene SRY on the Y chromosome."
	path = os.path.join(this_dir, "bootstrap_data", "dummySRY.tar.gz")
	importSNPs(path)

def importHumanReference() :
	""""Importes the Human Reference Genome. This may take a while, depending on the computers and 
	indexes in the database. But it's done only once."""
	path = os.path.join(this_dir, "bootstrap_data", "GRCh37.75.tar.gz")
	importGenome(path)
