echo 'deb http://www.rabbitmq.com/debian/ testing main' | tee /etc/apt/sources.list.d/rabbitmq.list

wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add -

apt-get update -y --force-yes && apt-get install rabbitmq-server -y \
&& rabbitmq-plugins enable rabbitmq_management \
&& rabbitmqctl add_user admin admin \
&& rabbitmqctl set_user_tags admin administrator \
&& rabbitmqctl  set_permissions -p "/" admin '.*' '.*' '.*' \
