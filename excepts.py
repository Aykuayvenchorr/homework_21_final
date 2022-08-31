class BaseError(Exception):
    message = 'Неожиданная ошибка'


class NotEnoughSpaceStore(BaseError):
    message = 'Недостаточно места на складе'


class NotEnoughProductStore(BaseError):
    message = 'Недостаточно товара на складе'


class NoProductInStore(BaseError):
    message = 'Такого товара нет на складе'


class TooManyDifferentProduct(BaseError):
    message = 'Слишком много разных товаров'


class InvalidRequest(BaseError):
    message = "Неправильный запрос"