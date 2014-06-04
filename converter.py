__author__ = 'carsten'

import start

import os
import re
import locale
from datetime import datetime

SEPARATOR = ';'

def analyze(path):
    base = os.path.basename(path)
    mod_filename = '{base}_converted{ext}'.format(base=os.path.splitext(base)[0], ext=os.path.splitext(base)[1])
    mod_base = os.path.join(os.path.dirname(path), mod_filename)
    print 'selected: {original}; converted: {converted}'.format(original=base, converted=mod_base)

    with open(path, 'rb') as in_file, open(mod_base, 'w') as out_file:
        for line in in_file:
            line = line.replace(' ,', ',')
            line = line.replace('null', '')
            line = line.rstrip(';\r\n')
            line += os.linesep

            #line = convert_numbers(line)
            ## set separator
            line = line.replace(',', SEPARATOR)

            out_file.write(line)
        out_file.close()
        print 'done.'


def convert_numbers(line):
    loc = locale.getlocale(locale.LC_NUMERIC)
    print loc

    converted_line = line


    exit(0)
    return converted_line

def convert_datetime(line):
    ## date/time conversion
    tokens = []
    dt = re.compile('(?P<date>\d{,2}/\d{,2}/\d{4})( (?P<time>\d{2}:\d{2}))*')
    for token in line.split(','):
        result = dt.match(token)
        if result:
            result = result.groupdict()
            #print '------- {0}: {1}'.format(token, result)
            if None != result['date'] and None != result['time']:
                token = datetime.strptime(token, '%d/%m/%Y %H:%M').isoformat()
            elif None != result['date']:
                token = datetime.strptime(token, '%d/%m/%Y').isoformat()
            elif None != result['time']:
                token = datetime.strptime(token, '%H:%M').time()

            #print '---- new: {0}\n'.format(token)
        tokens.append(token)

    # write the line
    line = '\t '.join(tokens)
    return line
