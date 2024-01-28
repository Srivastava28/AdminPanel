from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


employees = {
    "employees": [
          {
      "employee_id": 1,
      "name": "Atif Hussain",
      "position": "Data Analyst",
      "salary": 75000
    },
    {
      "employee_id": 2,
      "name": "Somitav Mishra",
      "position": "Business Analyst",
      "salary": 65000
    },
    {
      "employee_id": 3,
      "name": "Bob Johnson",
      "position": "Project Manager",
      "salary": 85000
    },
    {
      "employee_id": 4,
      "name": "John Doe",
      "position": "Software Engineer",
      "salary": 70000
    },
    {
      "employee_id": 5,
      "name": "Michael Brown",
      "position": "Quality Assurance Engineer",
      "salary": 72000
    },
    {
      "employee_id": 6,
      "name": "Jane Smith",
      "position": "UI/UX Designer",
      "salary": 78000
    },
    {
      "employee_id": 7,
      "name": "Chris Miller",
      "position": "Systems Administrator",
      "salary": 68000
    },
    {
      "employee_id": 8,
      "name": "Megan Wilson",
      "position": "Marketing Specialist",
      "salary": 60000
    },
    {
      "employee_id": 9,
      "name": "Kevin Lee",
      "position": "Network Engineer",
      "salary": 82000
    },
    {
      "employee_id": 10,
      "name": "Sara Martinez",
      "position": "Financial Analyst",
      "salary": 75000
    },
    {
      "employee_id": 11,
      "name": "Daniel Taylor",
      "position": "Product Manager",
      "salary": 88000
    },
    {
      "employee_id": 12,
      "name": "Laura Hall",
      "position": "Human Resources Specialist",
      "salary": 65000
    },
    {
      "employee_id": 13,
      "name": "Alex Turner",
      "position": "IT Support Technician",
      "salary": 62000
    },
    {
      "employee_id": 14,
      "name": "Grace Adams",
      "position": "Customer Support Representative",
      "salary": 58000
    },
    {
      "employee_id": 15,
      "name": "Jordan White",
      "position": "Sales Executive",
      "salary": 70000
    }
    ]
}

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def add_employee():
    new_employee = request.get_json()
    employees['employees'].append(new_employee)
    return jsonify({"message": "Employee added successfully"})

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for index, employee in enumerate(employees['employees']):
        if employee['employee_id'] == employee_id:
            del employees['employees'][index]
            return jsonify({"message": f"Employee with ID {employee_id} deleted successfully"})
    return jsonify({"error": f"Employee with ID {employee_id} not found"}), 404



if __name__ == '__main__':
    app.run(debug=True)
