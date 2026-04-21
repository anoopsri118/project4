from collections import defaultdict


def find_spammer(n, messages):
    """Return the spammer's account ID, or None if no spammer exists."""
    if n <= 0:
        return None

    received = [False] * (n + 1)
    sent_to = defaultdict(set)

    for sender, receiver in messages:
        if not (1 <= sender <= n and 1 <= receiver <= n):
            continue

        if sender == receiver:
            continue

        sent_to[sender].add(receiver)
        received[receiver] = True

    for account in range(1, n + 1):
        if not received[account] and len(sent_to[account]) == n - 1:
            return account

    return None


def run_tests():
    test_cases = [
        {
            "name": "basic spammer",
            "n": 4,
            "messages": [(2, 1), (2, 3), (2, 4), (1, 3), (3, 4)],
            "expected": 2,
        },
        {
            "name": "no spammer because receives a message",
            "n": 3,
            "messages": [(1, 2), (1, 3), (2, 1)],
            "expected": None,
        },
        {
            "name": "duplicates do not matter",
            "n": 3,
            "messages": [(1, 2), (1, 2), (1, 3), (1, 3)],
            "expected": 1,
        },
        {
            "name": "self messages ignored",
            "n": 3,
            "messages": [(1, 1), (1, 2), (1, 3), (2, 2)],
            "expected": 1,
        },
        {
            "name": "missing one recipient",
            "n": 4,
            "messages": [(3, 1), (3, 2)],
            "expected": None,
        },
        {
            "name": "single account",
            "n": 1,
            "messages": [],
            "expected": 1,
        },
    ]

    for case in test_cases:
        actual = find_spammer(case["n"], case["messages"])
        assert actual == case["expected"], (
            f'{case["name"]}: expected {case["expected"]}, got {actual}'
        )

    print("All tests passed.")


def run_examples():
    examples = [
        {
            "n": 5,
            "messages": [(4, 1), (4, 2), (4, 3), (4, 5), (2, 3), (5, 2)],
        },
        {
            "n": 3,
            "messages": [(1, 2), (1, 3), (3, 1)],
        },
    ]

    for index, example in enumerate(examples, start=1):
        result = find_spammer(example["n"], example["messages"])
        print(
            f"Example {index}: n={example['n']}, "
            f"messages={example['messages']} -> spammer={result}"
        )


if __name__ == "__main__":
    run_tests()
    run_examples()
