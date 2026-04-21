def find_one_spammer(n, hasMessaged):
    """Return one spammer in O(N) time, or -1 if no spammer exists."""
    if n <= 0:
        return -1

    candidate = 1

    for other in range(2, n + 1):
        if not hasMessaged(candidate, other):
            candidate = other

    for other in range(1, n + 1):
        if other != candidate and (
            not hasMessaged(candidate, other) or hasMessaged(other, candidate)
        ):
            return -1

    return candidate


def build_has_messaged(messages):
    sent = set(messages)

    def hasMessaged(sender, receiver):
        return (sender, receiver) in sent

    return hasMessaged


def run_sample_tests():
    test_cases = [
        {
            "name": "one spammer",
            "n": 4,
            "messages": {(2, 1), (2, 3), (2, 4), (1, 3), (3, 4)},
            "expected": 2,
        },
        {
            "name": "no spammer because receives a message",
            "n": 3,
            "messages": {(1, 2), (1, 3), (2, 1)},
            "expected": -1,
        },
        {
            "name": "single account",
            "n": 1,
            "messages": set(),
            "expected": 1,
        },
        {
            "name": "two-way messaging means no spammer",
            "n": 2,
            "messages": {(1, 2), (2, 1)},
            "expected": -1,
        },
        {
            "name": "candidate misses one account",
            "n": 4,
            "messages": {(3, 1), (3, 2)},
            "expected": -1,
        },
        {
            "name": "candidate receives one message",
            "n": 4,
            "messages": {(2, 1), (2, 3), (2, 4), (1, 2)},
            "expected": -1,
        },
    ]

    for case in test_cases:
        actual = find_one_spammer(case["n"], build_has_messaged(case["messages"]))
        assert actual == case["expected"], (
            f'{case["name"]}: expected {case["expected"]}, got {actual}'
        )
        print(f'{case["name"]}: {actual}')

    print("All sample and edge-case tests passed.")


if __name__ == "__main__":
    run_sample_tests()
