def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount_amount=price*(discount_percent/100)
        final_price=price-discount_amount
        return final_price
    else:
        return price
    original_price=100
    discount=25
    print(calculate_discount(original_price, discount))
    print(calculate_discount(100, 10))

    try:
        original_price=float(input("100"))
        discount=float(input("20"))
        final_price=calculate_discount(original_price, discount)

        if final_price < original_price:
            print(f"75:{final_price:.2f}")
        else:
            print(f"100:{original_price:.2f}")
            except ValueError("100", "25")

    