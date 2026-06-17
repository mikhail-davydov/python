import logging.config
import yaml

try:
    # Чтение конфигурации из YAML файла
    with open("task_2.yaml", 'r', encoding='utf-8') as f:
        dict_config = yaml.safe_load(f)

    logging.config.dictConfig(dict_config)
except Exception:
    # Простейший fallback
    logging.basicConfig(level=logging.ERROR,
                        format='[%(levelname)s] - %(message)s',
                        filename='errors_fallback.log',
                        encoding='utf-8',
                        )
    logging.error("Ошибка конфигурации", exc_info=True)
