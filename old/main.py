#python3.7.3

import yaml

with open(r'./tops.yaml') as f:
    tops = yaml.safe_load(f)

    for key in tops:
        print('key: ', key)
        if tops[key] is not None:
            for keys in key: 
            #print(key + ': ', tops[key]) 
                if tops[key][keys] is not None:
                    print(key, ' reverse: ', tops[key]['reverse'])
                if tops[key][keys] is not None:
                    print(key, ' band: ', tops[key]['band'])
        else:
            print('it\'s None!!!')
#    print(tops)
#    print('except reverse: ', tops['topA']['reverse'][0])
#    print('except band: ', tops['topB'])

with open(r'./bands.yaml') as g:
    bands = yaml.safe_load(g)

#    print(bands)

with open(r'./reverses.yaml') as h:
    reverses = yaml.safe_load(h)

#    print(reverses)
