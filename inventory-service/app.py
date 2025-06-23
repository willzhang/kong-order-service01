from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/inventory/decrease", methods=["POST"])
def decrease_inventory():
    print("库存扣减成功")
    return jsonify({"msg": "库存扣减成功"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
