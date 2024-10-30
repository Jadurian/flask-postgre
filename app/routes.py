from flask import Blueprint, request, jsonify
from .models import db, Student
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student = Student(
        name=data['name'],
        birth_date=datetime.strptime(data['birth_date'], '%Y-%m-%d'),
        dni=data['dni']
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student added successfully"}), 201

@main.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"name": s.name, "birth_date": s.birth_date.strftime('%Y-%m-%d'), "dni": s.dni} for s in students])

# Endpoints adicionales para actualizar y eliminar estudiantes pueden ser añadidos aquí
