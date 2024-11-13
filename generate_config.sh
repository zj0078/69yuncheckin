#!/bin/bash

# 创建 config.json 文件并初始化
cat <<EOF > config.json
{
    "domain": "https://69yun69.com",
    "BotToken": "${BOT_TOKEN}",
    "ChatID": "${CHAT_ID}",
    "accounts": [
EOF

# 初始化用户索引
index=1
first_account=true

# 循环遍历所有用户
while true; do
  # 获取USER和PASS变量的名称
  user_var="USER${index}"
  pass_var="PASS${index}"

  # 从环境变量中获取用户名和密码
  user="${!user_var}"
  pass="${!pass_var}"

  # 如果没有找到有效的用户，跳出循环
  if [ -z "$user" ] || [ -z "$pass" ]; then
    break
  fi

  # 如果这是第一个用户，不添加逗号，否则添加逗号以保持JSON格式
  if [ "$first_account" = true ]; then
    first_account=false
  else
    echo "," >> config.json
  fi

  # 将当前用户的信息写入JSON格式
  cat <<EOF >> config.json
        {
            "user": "${user}",
            "pass": "${pass}"
        }
EOF

  # 增加索引，继续下一个用户
  index=$((index + 1))
done

# 结束 JSON 文件内容
echo "]" >> config.json
echo "}" >> config.json

echo "config.json has been generated."
