from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/order/create", methods=["POST"])
def create_order():
    print("收到创建订单请求，调用库存服务扣减库存")
    try:
        # 通过Kong调用库存服务
        resp = requests.post("http://192.168.73.11:8000/inventory/decrease")
        return jsonify({"msg": "订单创建成功", "inventory_response": resp.json()})
    except Exception as e:
        return jsonify({"msg": "订单创建失败", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
