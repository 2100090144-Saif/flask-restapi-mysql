from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'XXXXXXXXXX'
app.config['MYSQL_DB'] = 'restapi_db'

mysql = MySQL(app)

# -------------------- GET ALL --------------------
@app.route("/students", methods=["GET"])
def get_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    students = []
    for row in data:
        students.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    return jsonify(students)

# -------------------- GET SINGLE --------------------
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE id=%s", (id,))
    row = cur.fetchone()
    cur.close()

    if row:
        return jsonify({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })
    return jsonify({"message": "Student not found"}), 404

# -------------------- CREATE --------------------
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    name = data["name"]
    email = data["email"]

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO students(name,email) VALUES(%s,%s)", (name,email))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Student created"}), 201

# -------------------- UPDATE --------------------
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    name = data["name"]
    email = data["email"]

    cur = mysql.connection.cursor()
    cur.execute("UPDATE students SET name=%s,email=%s WHERE id=%s", (name,email,id))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Student updated"})

# -------------------- DELETE --------------------
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(debug=True)
