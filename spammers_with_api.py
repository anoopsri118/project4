def find_spammers(n, hasMessaged):
    spammers = []

    for account in range(1, n + 1):
        sent_to_everyone = True
        received_any = False

        for other in range(1, n + 1):
            if other == account:
                continue

            if not hasMessaged(account, other):
                sent_to_everyone = False

            if hasMessaged(other, account):
                received_any = True

            if not sent_to_everyone and received_any:
                break

        if sent_to_everyone and not received_any:
            spammers.append(account)

    return spammers if spammers else -1


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
            "expected": [2],
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
            "expected": [1],
        },
        {
            "name": "two-way messaging means no spammer",
            "n": 2,
            "messages": {(1, 2), (2, 1)},
            "expected": -1,
        },
    ]

    for case in test_cases:
        actual = find_spammers(case["n"], build_has_messaged(case["messages"]))
        assert actual == case["expected"], (
            f'{case["name"]}: expected {case["expected"]}, got {actual}'
        )
        print(f'{case["name"]}: {actual}')

    print("All sample tests passed.")


if __name__ == "__main__":
    run_sample_tests()
