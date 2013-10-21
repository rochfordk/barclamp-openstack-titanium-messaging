name "rabbitmq"
description "RabbitMQ Multi-Node"
run_list(
        "recipe[rabbitmq::default]",
        "recipe[rabbitmq::mgmt_console]"
)
default_attributes()
override_attributes()
