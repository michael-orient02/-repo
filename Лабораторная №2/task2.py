salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_spend = sum(spend * (1 + increase) ** month for month in range(months))
total_salary = salary * months
money_capital = total_spend - total_salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
