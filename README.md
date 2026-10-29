# MiningASCII

> Public source preview: see [PUBLICATION.md](PUBLICATION.md) for actual checks, known failures and runtime limits.

## О проекте

`MiningASCII` — ASCII-игра про исследование мира, добычу ресурсов, развитие персонажа и столкновения с монстрами. По структуре это самый цельный проект в этой группе: отдельные модули отвечают за мир, игрока, крафт, интерфейс, рендеринг и игровые сущности.

## Основные механики

- запуск отдельного игрового объекта через `Game`;
- ASCII-рендеринг сцены;
- игровой мир и набор утилит для его обслуживания;
- игрок, предметы, навыки и крафт;
- монстры и базовые боевые взаимодействия;
- UI-слой поверх основной логики.

## Стек и структура

- Python
- `pygame`
- основные файлы: `main.py`, `game.py`, `world.py`, `player.py`, `crafting.py`, `monsters.py`, `ui.py`, `ascii_renderer.py`

## Запуск

```bash
python main.py
```

## Статус

Готовый игровой прототип. Проект уже выглядит как законченная база для дальнейшего расширения контента и баланса.


## Public source status — 2026-10-29

See [PUBLICATION.md](PUBLICATION.md) for the current verification scope, prototype limitations and runtime boundaries. Earlier audit checklists describe historical work.
