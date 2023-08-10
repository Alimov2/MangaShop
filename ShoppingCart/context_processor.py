def total_price(request):
    total = 0

    if request.user.is_authenticated:
        if "cart" in request.session:
            for key, value in request.session["cart"].items():
                total += float(value["price"])

    return {"total_price": total}
