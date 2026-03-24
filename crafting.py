# crafting.py
from items import Chest, Key

class Crafting:
    def __init__(self):
        # Рецепты: название -> (список необходимых ресурсов, итоговый предмет)
        self.recipes = {
            "chest": ([("wood", 5), ("metal", 2)], Chest(locked=True)),
            "key": ([("metal", 1)], Key()),
        }

    def craft(self, recipe_name, inventory):
        if recipe_name not in self.recipes:
            return None
        requirements, result = self.recipes[recipe_name]
        # Проверка наличия необходимых ресурсов
        for item_name, quantity in requirements:
            count = sum(item.quantity for item in inventory if item.name == item_name)
            if count < quantity:
                print("Недостаточно ресурсов для крафта", recipe_name)
                return None
        # Удаляем использованные ресурсы из инвентаря
        for item_name, quantity in requirements:
            removed = 0
            for item in inventory:
                if item.name == item_name and removed < quantity:
                    if item.quantity > (quantity - removed):
                        item.quantity -= (quantity - removed)
                        removed = quantity
                    else:
                        removed += item.quantity
                        item.quantity = 0
            inventory[:] = [item for item in inventory if item.quantity > 0]
        # Возвращаем созданный предмет
        print(f"Создан предмет: {result.name}")
        return result
