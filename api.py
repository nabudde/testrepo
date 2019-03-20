#This enables me to import objects from Flask  
from flask import Flask, jsonify, request


app = Flask (__name__)

#creating ny diary enrties in form of a dictonary but in a list
diary = [
         {
           "Entry": "preparation",  
           "Time": "6:00-8:00am"
         },
         {
             "Entry": "church session",
             "Time":"8:00-9:00am"
         },
         {
             "Entry": "work hours" ,
             "Time": "9:00am-5:00pm",
           
        },
         {
             "Entry": "personal time",
             "Time": "5:00-8:00pm",
             
         }
         ]


#This route creates a url then returns message in a json form
@app.route('/' , methods = ['GET'])
def test():
    return jsonify({'message': 'my diary'})

#The route here then returns all my entries in the list above created in the above dictionary
@app.route('/API/v1/index', methods = ['GET'])
def return_all():
    return jsonify({'Entry': diary})

#Here i only request a return of only one entry
@app.route('/API/v1/index/<string:Entry>', methods = ['GET'])
def return_one(entry):
    dia = [item for item in diary if item['Entry']== entry]
    return jsonify({'Ent':dia[0]})

   


#The route here uses a post method returning anything added in my dictionary
@app.route('/API/v1/index', methods = ['POST'])
def add_one():
    task = {'Entry': request.json['Entry']}
    diary.append(task)
    return jsonify({'diary': diary})

# The route here uses a put method to modify my API
@app.route('/API/v1/index/<string:entry>', methods = ['PUT'])
def edit_one(entry):
    dia = [activity for activity in diary if activity['Entry']== entry]
    dia[0]['Entry'] = request.json['Entry']
    return jsonify({'Ent': dia[0]})




#Returning app port 5000 in debug mode
if __name__ == '__main__':
    app.run(debug = True, port = 5000)