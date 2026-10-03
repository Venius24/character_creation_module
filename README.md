# Создание персонажа RPG

Небольшая консольная учебная игра на Python. Выберите воина, мага или лекаря и попробуйте команды атаки, защиты и специального умения. Значения атаки и защиты случайны в диапазонах выбранного класса; сохранения персонажа и полноценной боевой системы нет.

## Запуск

Клонируйте проект с вложенным модулем и установите библиотеки для анимированного баннера:

```powershell
git clone --recurse-submodules https://github.com/Venius24/character_creation_module.git
cd character_creation_module
python -m pip install asciimatics pyfiglet
python main.py
```

Для уже клонированного репозитория: `git submodule update --init --recursive`.

Введите имя, затем `warrior`, `mage` или `healer`. Подтвердите выбор буквой `y`. В тренировке доступны `attack`, `defence`, `special` и `skip` для выхода.

Для проверки установите pytest:

```powershell
python -m pip install pytest
python -m pytest
```

Баннер загружается из вложенного репозитория `graphic_arts`. Указатель родительского репозитория на его commit не менялся. Локальные незакоммиченные правки вложенного проекта будут доступны при запуске этой копии, но отсутствуют в свежем клоне до их отдельной публикации.

Репозиторий: https://github.com/Venius24/character_creation_module
