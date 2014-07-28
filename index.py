import jinja2
import sys, os
sys.path.append(os.getcwd())
import urls
reload(urls)

env = jinja2.Environment(loader=jinja2.FileSystemLoader(
 searchpath='templates/')
 )
for templateName, url in urls.urls.iteritems():
    template = env.get_template(templateName)
    dispdict = {}
    output = template.render(dispdict)
    print output
    print templateName, url

    fout = open(url, 'w')
    fout.write(output)
    fout.close()
