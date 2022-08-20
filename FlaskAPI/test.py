from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc', methods=['POST','GET'])
def test():
    result = 0
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
    return result

if __name__ == '__main__':
    app.run()


#Task
 # 1. Write a program to insert a record in sql table via api
 # 2. Write a program to update a record via api
 # 3. Write a program to delete a record via api
 # 4. Write a program to fetch a record via api
 # 5. Create same for mango DB as well