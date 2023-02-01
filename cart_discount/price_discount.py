def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    amount = len(item_prices)
    if amount == 0:
        return 'Enter one or more dollar values'
    elif amount < 3:
        return f'You\ve only bought {amount} item(s), so you are not eligible for a discount'
    elif amount >= 3:
        cheapest = item_prices[0]
        for item in item_prices:
            if item < cheapest:
                cheapest = item

        return cheapest


if __name__ == '__main__':
    main()
