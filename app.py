from flask import Flask, jsonify

todo = Flask(__name__)
students = [
    {
        'id':1,
        'name':'gowtham',
        'age':3
    },
{
        'id':2,
        'name':'charan',
        'age':2
    },
{
        'id':3,
        'name':'prashanth',
        'age':5
    }
]
@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_student_by_id(id):
    print(id)
    for std in students:
        if std['id'] == id:
            return jsonify(std)
        print(std)



if __name__ == '__main__':
    todo.run(

        debug=True)