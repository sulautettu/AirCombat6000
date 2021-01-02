from flask import Flask,render_template,request

import threading


def initServer(controlDataToPyGame):


    app = Flask(__name__)
    app.debug= False
    

    @app.route('/')

    def index():
        print("index")
        return render_template('controller.html')
        print("index")


    @app.route("/Control/")
    def UP():
        x = request.args.get('joyX')
        y = request.args.get('joyY')

        controlDict = {"name":"ice", "x":x,"y":y}
        controlDataToPyGame.put(controlDict)


        #print("x: " + x + "y: " + y )

        #print("putted")
        return ("nothing")



    threading.Thread(target = app.run).start()


