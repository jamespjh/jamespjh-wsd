import urllib
import re
import yaml
import os
import sys
import argparse

config=yaml.load(open(os.path.expanduser(os.path.join("~",".wsd",'config.yml'))))

def getSequenceDiagram( text, outputFile, key=None, style = 'default' ):
    request = {}
    request["message"] = text
    request["style"] = style
    request["apiVersion"] = "1"
    if key:
        request["apikey"]=key
    print request
    url = urllib.urlencode(request)

    f = urllib.urlopen("http://www.websequencediagrams.com/", url)
    line = f.readline()
    f.close()
    print line
    expr = re.compile("(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")
    m = expr.search(line)

    if m == None:
        print "Invalid response from server."
        return False

    urllib.urlretrieve("http://www.websequencediagrams.com/" + m.group(0),
            outputFile )
    return True

def main():    
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument("--in", help="Input file")
    parser.add_argument("--out", help="Output file")
    parser.add_argument("--style",help="Style choice file",default=config['style'] or "qsd")
    options,extra = parser.parse_known_args(sys.argv)
    getSequenceDiagram( open(vars(options).get("in")).read() , options.out, config.get("key"), options.style )    

if __name__ == '__main__':
    main()       
