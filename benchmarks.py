import sys
import requests
import json


baseUrl = "http://localhost:3000/api"


def run_specific_agent(task: str) -> None:
    print("not implemented")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <task>")
        sys.exit(1)
    task = sys.argv[1]
    run_specific_agent(task)
