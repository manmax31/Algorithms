"""
We are given a list of prices of a stock for N number of days.
We need to find stock span for each day.
Span is defined as number of consecutive days before the given day where
the price of stock was less than or equal to price at given day.
For example, {100, 60, 70, 65, 80, 85} span for each day will be {1, 1, 2, 1, 4, 5}.

We need to check last price which was greater than price today
Hence we need to maintain a stack which contains prices seen in decreasing order.
So while scanning prices on given days, check if there are prices which are less than current price.
If yes, just pop them out.
When we encounter a price which is greater than current price,
stock span with maximum profit of current day is difference between day of that price and current day.
Hence, it becomes apparent that, storing index of last greatest seen price would make things easier as compared to storing actual price.
Hence day is store i on stack, price[i] will give us the price of stock on day i.

Algorithm:
1. Initialize span of day 1 as 1.
2. Put day 1 on to stack.
3. For all days starting from day[1:], repeat following steps.
   3.1 If price of stock on day at top of stack is <= price of stock on current day, Pop the index from stack.
   3.2 If price of stock on the day on top of stack is > than price of stock on current day, calculate span as current day - day at top of stack.
   3.3 Push current day index on to stack.

http://algorithmsandme.in/2014/02/stock-span-problem/
Time: O(n)


"""


def stock_span(prices):
    stack = [0]  # Create Stack and Push Index of First element.
    span = [1]   # Span of First element is always 1
    for cur_day, price in enumerate(prices[1:], start=1):
        print(stack)
        while len(stack) > 0 and prices[stack[0]] <= price:
            stack.pop(0)
        span.append(cur_day - stack[0])
        stack.insert(0, cur_day)
    return span


if __name__ == '__main__':
    prices = [100, 60, 70, 65, 80, 85]
    print(stock_span(prices))
