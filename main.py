# take create_app from __init__.py
from website import create_app

app = create_app()

# ensure that you only run this main.py directly not open from another link
if __name__ == '__main__':
    # debug = true means whenever we change the code, it will rerun the web server 
    app.run(debug = True)
    