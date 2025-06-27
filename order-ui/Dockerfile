FROM nginx:alpine

# 复制HTML模板文件
COPY index.html /usr/share/nginx/html/index.html.template

# 设置默认环境变量
ENV GATEWAY_URL=http://192.168.73.11:8000

# 创建启动脚本
RUN cat <<EOF > /docker-entrypoint.sh
#!/bin/sh
envsubst '\$GATEWAY_URL' < /usr/share/nginx/html/index.html.template > /usr/share/nginx/html/index.html
exec "\$@"
EOF
RUN chmod +x /docker-entrypoint.sh


EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
