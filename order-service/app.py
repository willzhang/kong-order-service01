import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# 从环境变量获取Gateway URL，提供默认值
GATEWAY_URL = os.environ.get('GATEWAY_URL', 'http://192.168.73.11:8000')

@app.route("/order/create", methods=["POST"])
def create_order():
    print(f"收到创建订单请求，调用库存服务: {GATEWAY_URL}")
    try:
        # 通过Kong网关调用库存服务
        inventory_url = f"{GATEWAY_URL}/inventory/decrease"
        resp = requests.post(inventory_url, timeout=10)
        resp.raise_for_status()

        return jsonify({
            "msg": "订单创建成功", 
            "inventory_response": resp.json()
        })
    except Exception as e:
        print(f"调用库存服务失败: {str(e)}")
        return jsonify({
            "msg": "订单创建失败", 
            "error": str(e)
        }), 500

@app.route("/health", methods=["GET"])
def health_check():
    """健康检查接口，用于Consul注册"""
    return jsonify({
        "status": "healthy",
        "service": "order-service",
        "port": 5001
    }), 200

if __name__ == "__main__":
    print(f"启动订单服务，Gateway地址: {GATEWAY_URL}")
    app.run(host="0.0.0.0", port=5001)
