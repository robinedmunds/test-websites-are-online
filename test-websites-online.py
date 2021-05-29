#!/usr/bin/env python3
import json
from class_domain import Domain

def import_domains_from_json(dicts):
    domains = []
    for d in dicts:
        domains.append(
            Domain(
                domain=d["domain"],
                https=d["https"],
                www=d["www"],
            )
        )
    return domains


def main():
    f = open("domains.json", "r")
    dicts = json.loads(f.read())
    f.close()
    domains = import_domains_from_json(dicts)

    for domain in domains:
        domain.test()


if __name__ == "__main__":
    main()
