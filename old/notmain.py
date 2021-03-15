# python 3.7.3

#def csv_file(list):
    # print list to CSV

#def create_phrases():
    # creates the phrases based on .yaml file

# okay i'm in over my head

import yaml

with open(r'./tops.yaml') as f:
    tops = yaml.safe_load(f)

    # make list
    list = []
    for key in tops:
        list.append(key)
    print(list)
    for key in tops:    
        if tops[key] is not None:
            if 'reverse' in tops[key]:
                #print(tops[key]['reverse'])
                for i in tops[key]['reverse']:
                    #print(key, 'reverse: not ', i)
                    if i is not 'A':

            #print(tops[key], ' tops[key]')

