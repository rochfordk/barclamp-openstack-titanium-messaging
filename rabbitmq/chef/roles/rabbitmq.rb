name "rabbitmq"
description "RabbitMQ Multi-Node"
run_list(
        "recipe[rabbitmq::define_cluster]",
        "recipe[rabbitmq::default]",
        "recipe[rabbitmq::virtualhost_management]",
        "recipe[rabbitmq::user_management]",
        "recipe[rabbitmq::mgmt_console]",
        "recipe[rabbitmq::monitor]"
)
default_attributes()
override_attributes()
