

denoms = (100, 50, 20, 10, 5, 2, 1)


# find all the ways to make change given infinite coins
def make_change(amount, coins=denoms, partial_sum=[]):
    if amount is 0:
        return [partial_sum]
    elif amount < 0 or not coins:
        return []
    else:
         c = coins[0]
         return (make_change(amount - c, coins, partial_sum + [c])
                 + make_change(amount, coins[1:], partial_sum))

# how many ways are there?
def count_make_change(amount, coins=denoms):
    return len(make_change(amount, coins))


#what if you don't have infinite coins?
def make_change_limited(amount, coins=denoms, partial=[]):
    if amount is 0:
        return [partial]
    elif amount < 0 or not coins:
        return []
    else:
        ci = coins[0]
        left = [c for c in coins if c != ci]
        return (make_change_limited(amount - ci, coins[1:], partial + [ci]) +
                make_change_limited(amount, left, partial))


# can be done in a generator like this, a bit cleaner i think
# unlike the other this code works from the bottom up
# (in my limited checks this seems to be quite a bit faster, I guess python prefers generators)
def make_change_generator(amount, coins=denoms, partial=[], partial_sum=0):
    if partial_sum == amount:
        yield partial
    if partial_sum >= amount:
        return
    for i, n in enumerate(coins):
        left = coins[i + 1:]
        yield from make_change_generator(amount, left, partial + [n], partial_sum + n)
