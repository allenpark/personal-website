import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader(
 searchpath='templates/')
 )
template = env.get_template('index.jinja')

dispdict = {}

fout = open('index.html', 'w')
fout.write(template.render(dispdict))
fout.close()
