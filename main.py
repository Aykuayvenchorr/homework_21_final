from classes import Shop, Store, Request, Courier

store = Store(items={
    "торт": 5,
    "эклер": 10,
    "слойка": 20
})

shop = Shop(items={
    "торт": 2,
    "эклер": 2,
    "слойка": 2
})


def main():
    print('Добрый день!')

    while True:
        print(f"На складе {store.get_items()}")
        print(f"В магазине {shop.get_items()}")

        user_input = input(
            "Введите запрос в формате: Доставить 3 торт из склад в магазин\n"
            "Введите стоп или stop, если хотите закончить\n"
        )

        if user_input in ("стоп", "stop"):
            break

        request = Request(user_input)
        courier = Courier(request=request, store=store, shop=shop)
        courier.move()


if __name__ == "__main__":
    main()

