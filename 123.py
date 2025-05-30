import importlib

module_name = "math"
function_name = "sqrt"

try:
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    result = func(16)
    print(f"Результат виклику {function_name}(16): {result}")
except ModuleNotFoundError:
    print(f"Модуль '{module_name}' не знайдено.")
except AttributeError:
    print(f"Функція '{function_name}' не знайдена в модулі '{module_name}'.")
except Exception as e:
    print(f"Помилка при виклику функції: {e}")
