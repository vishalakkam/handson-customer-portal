from flask import Flask, request, jsonify

app = Flask(__name__)

customers = []


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"})


@app.route("/register", methods=["POST"])
def register_customer():
    data = request.get_json()

    customer = {
        "id": len(customers) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }

    customers.append(customer)

    return jsonify(customer), 201


@app.route("/customers", methods=["GET"])
def get_customers():
    return jsonify(customers)


@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    for customer in customers:
        if customer["id"] == customer_id:
            return jsonify(customer)

    return jsonify({"error": "Customer not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)