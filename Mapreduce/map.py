#!/usr/bin/env python
import itertools
from itertools import groupby
from operator import itemgetter
import sys
# from xml.etree import ElementTree
# from xml.dom import minidom
# import xml.parsers.expat

SOURCE_FILE = "/Users/heinam/Documents/big data/ass1/dblp.xml"
# SOURCE_FILE = "/Users/heinam/Documents/big data/ass1test.xml"
  



def read_input(file):
    """ iterates through particular tags of XML file."""
    first_round = True
    inText = False
    currentTag = ""
    #8 types of record tags according to http://dblp.org/faq/16154937
    tags = ['article','inproceedings','proceedings','book','incollection','phdthesis','mastersthesis','www']

    for line in file:

        line = line.strip()
        
        if(first_round):
            for tag in tags: 
                if line.find( '<' + tag) != -1: #begin line if find start of tag (first occurence)
                    inText = True
                    first_round = False #once found, no need check start of tag again
                    break
        
        for tag in tags: 
            if line.find('</' + tag + '>') != -1: #cut line if find end of tag
                inText = False
                break

            
        #still within current tag
        if inText == True:
            currentTag = currentTag + line

        if inText == False:

            yield(currentTag)
            currentTag = line #also to be start of next new tag (end of tag and begin of tag is on the same line in the original file)
            inText = True


def mapper():
    print "Reading data..."
    data = read_input(open(SOURCE_FILE))#.readlines()

    print "Start mapping..."
    for words in data:
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        words = words.replace("</author><author>","<author>")
        words = words.replace("</author>","<author>")
        words = words.replace("<author ","<author>???###") #author tags wsith attribute
        author_list_raw = words.split("<author>")[1:len(words.split("<author>"))-1] #only need middle elements
        author_list = [name.rstrip() for name in author_list_raw]
        author_list = [name for name in author_list if len(name) > 0]

        if len(author_list) <= 1: #only one author or none
            continue

        #remove attribute part before combination, sort author names
        name_list = sorted(name.split('">')[1] if name.find("???###") != -1 else name for name in author_list)
        comb_list = itertools.combinations(name_list,2)
        for subset in comb_list:
            # print("{}\t{}".format(' '.join('"'+name+'"' for name in subset), 1))
            yield (' '.join('"'+name+'"' for name in subset), 1)

    print "Finish mapping"


def read_mapper_output(file):
    for line in sorted(file): #sort before groupby in reducer
        yield line

def reducer_intermediate(mapped):
    for current_word, group in groupby(mapped, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            # print "%s%s%d" % (current_word, separator, total_count)
            yield(total_count, current_word)

        except ValueError:
            # count was not a number, so silently discard this item
            pass

def reducer():

    #sort before groupby in reducer
    data = read_mapper_output(mapper())
  
    #count frequency of each co-authorship
    counted_data = reducer_intermediate(data)

    #print top 100
    n = 0
    top = 100

    for line in sorted(counted_data, reverse=True): 
        print print("{}\t{}".format(line[1], line[0]))
        n = n + 1
        if (n==top):
            break


# class AllEntities:
#     def __getitem__(self, key):
#         #key is your entity, you can do whatever you want with it here
#         return key

if __name__ == "__main__":  
    reducer()
#give up loading into xml document tree since it is very time consuming and too many special characters
    # parser = xml.parsers.expat.ParserCreate()
    # p = parser.ParseFile(open('/Users/heinam/Documents/big data/dblp.xml', 'r'))
    # #xml method 1
    # xmldoc = minidom.parse('/Users/heinam/Documents/big data/dblp.xml')
    # articlelist = xmldoc.getElementsByTagName('article')

    # for s in articlelist:
    #     print(s.attributes['name'].value)


    #xml method 2
#     parser = ElementTree.XMLParser()
#     parser.parser.UseForeignDTD(True)
#     parser.entity = AllEntities()

#     etree = ElementTree.ElementTree()

#     tree = etree.parse("/Users/heinam/Documents/big data/dblp.xml", parser=parser)

# for node in tree.iter('author'):
#     print node.text




