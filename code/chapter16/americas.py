import pygal

wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy',
       'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('G:/workstation/py_workstation/Data_Visualization/code/' \
                               'chapter16/json/americas.svg')