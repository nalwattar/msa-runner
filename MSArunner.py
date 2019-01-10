import sys 
import Bio.SeqIO
import csv
import subprocess
import Bio.SeqRecord
import unittest

def readMetadata(gbFnameList):
    sequenceMetadataList = []
    for gbFname in gbFnameList:
        #print(gbFname)
        record = Bio.SeqIO.read(gbFname, 'genbank')
        sequenceMetadata = SequenceMetadata(record)
        sequenceMetadataList.append(sequenceMetadata)
    return sequenceMetadataList

def test_readMetadata():
    test = readMetadata(sys.argv[3:])
    print(test)
    
def writeMetadataToCsv(sequenceList, csvFile):
    sequenceMetadataFieldnameList = ['idNumber', 'organism', 'accessionNumber']
    writer = csv.DictWriter(csvFile, fieldnames = sequenceMetadataFieldnameList, restval='no info available')
    writer.writeheader()
    for sequenceMetadata in sequenceList:
        #print('loop is running')
        writer.writerow(sequenceMetadata.makeRowDict())

def test_writeMetadataToCsv():
	sequenceMetadataList = []
	sequenceMetadata = SequenceMetadata('1234', 'palm', '5678')
	sequenceMetadataList.append(sequenceMetadata)
	with open(sys.argv[1], 'w') as csvFile:
		writeMetadataToCsv(sequenceMetadataList, csvFile)
#test_writeMetadataToCsv()

def runWriteMetadataToCsv():
	sequenceMetadataList = []
	sequenceMetadata = SequenceMetadata()
	sequenceMetadataList.append(sequenceMetadata)
	with open(sys.argv[1], 'w') as csvFile:
		writeMetadataToCsv(sequenceMetadataList, csvFile)

def mergeSequencesAndConvertToFasta(sequenceList, fastaFile):
    sequenceList = []
    for sequence in sequenceList:
        line = Bio.SeqIO.write(gbFname.seqRecord, fastaFile, 'fasta')
        sequenceList.append(sequence)
    return sequenceList

def containSequenceListInSeqIOObject():
    sequenceList = mergeSequencesAndConvertToFasta(sequenceList, fastaFile)

class MultipleSequenceAlignmentRunner(object):
	"""Wrapper class for running Multiple Sequence Alignment (MSA) programs
	 such as Clustal Omega and MAFFT.

This is a base class for runners that wrap specific MSA programs.

"""

	def __init__(self, SeqRecord=None):
		self.SeqRecord = SeqRecord

	def __str__(self):
    	return '(\'%s\',\'%s\',\'%s\')' % (self.seqRecord.id, self.seqRecord.annotations['organism'], self.seqRecord.annotations['accessions'][0], self.seq)

    def makeRowDict(self):
    	return {'idNumber': self.seqRecord.id, 'organism': self.seqRecord.annotations['organism'], 'accessionNumber': self.seqRecord.annotations['accessions'][0]}

class MAFFTRunner(MultipleSequenceAlignmentRunner):

	def __init__(self,):
		pass

	def pOpenForGuidetree():
    mergedSequences = mergeSequencesAndConvertToFasta(sequenceList, fastaFile)
    p = subprocess.Popen(['mafft', '--auto', '--reorder', mergedSequences], stdin = subprocess.PIPE, stdout = subprocess.PIPE, universal_newlines = True)
    records = list(Bio.SeqIO.parse(p.stdout, 'fasta'))

class ClustaloRunner(MultipleSequenceAlignmentRunner):

	def __init__(self,):
		pass

	def clustalo():
    mergedSequences = mergeSequencesAndConvertToFasta(sequenceList, fastaFile)
    p = subprocess.Popen(['clustalo' '-i' mergedSequences], stdin = subprocess.PIPE, stdout = subprocess.PIPE, universal_newlines = True)



