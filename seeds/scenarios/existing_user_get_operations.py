from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который совершает 5 операций покупки,
    1 операцию пополнения счета, 1 операцию снятия наличных.
    Создаём 300 пользователей, каждому из которых открывается кредитный счёт.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Мы создаём 300 пользователей, каждый получит кредитный счёт.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Создаём 300 пользователей
                credit_card_accounts=SeedAccountsPlan(
                    count=1,  # Кредитный счёт на пользователя
                    virtual_cards=SeedCardsPlan(count=1),  # Виртуальная карта для счёта
                    purchase_operations=SeedOperationsPlan(count=5),  # 5 операций покупки
                    top_up_operations=SeedOperationsPlan(count=1),  # 1 операция пополнения
                    cash_withdrawal_operations=SeedOperationsPlan(count=1)  # 1 операция снятия наличных
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    # Если файл запускается напрямую, создаём объект сценария и запускаем его.
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()  # Стартуем процесс сидинга