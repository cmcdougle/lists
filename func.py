# python 3.7.3

import yaml


with open(r'./tops.yaml') as f:
    tops = yaml.safe_load(f)

    for k in tops:
        for j in tops[k]['reverse']:
            for i in tops[k]['band']:
                print('Top: ', k, ' Reverse: ', j, ' Band: ', i)
                # convert print statement into write to text file
                with open('output.txt', 'a') as g:
                    write = 'Top: ' + k + ', Reverse: ' + j + ', Band: ' + i + '\n'
                    g.write(write)
