from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/inventory/decrease", methods=["POST"])
def decrease_inventory():
    print("库存扣减成功")
    return jsonify({"msg": "库存扣减成功"}), 200

@app.route("/health", methods=["GET"])
def health_check():
    """健康检查接口，用于Consul注册"""
    return jsonify({
        "status": "healthy",
        "service": "inventory-service",
        "port": 5002
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
