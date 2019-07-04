import pygal.maps.world
wm = pygal.maps.world.World()

wm.title = 'test'
wm.add('North America',{'ca':34126000,'us':30934000})

wm.render_to_file('test.svg')