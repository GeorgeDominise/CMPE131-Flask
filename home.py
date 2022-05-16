from flask import Flask

obj = Flask(__name__)

@obj.route('/')
def home():
    name = 'George'
    city_names = ['Modesto', 'Sacramento', 'San Francisco']
    return '''

    <html>
    <body>
    <h1> Welcome ''' + name + '''</h1> 
    <a href ="https://www.google.com/"> not google </a>

    <ul style="list-style-type:circle">
        <li> ''' + city_names[0] + ''' </li>
        <li> ''' + city_names[1] + ''' </li>
        <li> ''' + city_names[2] + ''' </li>
    </body>
    </hmtl>
    '''
obj.run()
