import logging.config
import yaml


with open("task_1.yaml", 'r', encoding='utf-8') as f:
    dict_config = yaml.safe_load(f)

logging.config.dictConfig(dict_config)

handler = logging.getHandlerByName("queue_handler")  # имя из конфигурации
queue_listener = handler.listener
queue_listener.start()
try:
    main()
finally:
    queue_listener.stop()