#!/usr/bin/env python3

# TODO: support for derivative words

from fbs_runtime.application_context import ApplicationContext
import json

# TODO: solve absolute path issue in the scr/.../rdict.py file
appctxt = ApplicationContext()
datafile = appctxt.get_resource('rdict.json')
jdict = None

# reads json file 'datafile' into 'jdict' list
def parse():
    global jdict
    df = open(datafile)
    raw = df.read()
    df.close()
    jdict = json.loads(raw)

# recursively adds lines of formatted 'val' to 'outlist'
def _fstr(val, outlist, offstr = '', tabstr = '&nbsp;' * 4):
    if type(val) == dict:
        for k, v in val.items():
            outlist.append('{}{}:'.format(offstr, '<b>' + k + '</b>'))
            _fstr(v, outlist, offstr + tabstr, tabstr)
    elif type(val) == list:
        if len(val) == 1:
            _fstr(val[0], outlist, offstr, tabstr)
        elif type(val[0]) == str:
            outlist.append(offstr + ', '.join(val))
        else:
            for i in range(len(val)):
                outlist.append('{}({})'.format(offstr, i + 1))
                _fstr(val[i], outlist, offstr + tabstr, tabstr)
    else:
        outlist.append('{}{}'.format(offstr, val))

# returns the formatted string for 'val'
def fstr(val):
    l = []
    _fstr(val, l)
    return '<br/>'.join(l); # no additional ending '\n'

# returns formatted word definition for w
def define(w):
    global jdict
    nf_msg = '<span style="color:red">Sorry! Word not found.</span>'
    # linear search
    val = [x for x in jdict if x['word'] == w]
    if len(val):
        val = val[0]['meaning']
    else:
        val = nf_msg
    return fstr(val)

# cli dictionary when run directly
def main():
    parse()
    # print(repr(sorted(jdict, key = lamda x: x['word'])).replace('\': ', '\':').replace('}, ', '},').replace('], ', '], '))
    # print(sorted(set([x['word'] for x in jdict])))
    res=[]
    s = set()
    for x in jdict:
        if x['word'] not in s:
            s.add(x['word'])
            res.append(x)
    # print(sorted([x['word'] for x in res]))
    res = sorted(res, key = lambda x: x['word'])
    # print([x['word'] for x in res])
    print(json.dumps(res).replace('": ', '":').replace('}, ', '},').replace('", ', '",').replace('", ', '",').replace('], ', '],'))
    # while True:
    #     print("Enter a word:")
    #     w = input()
    #     print(define(w))

if __name__ == '__main__':
    main()
